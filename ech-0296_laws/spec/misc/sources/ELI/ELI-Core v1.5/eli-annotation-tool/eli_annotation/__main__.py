# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import os
import os.path as osp
import datetime as dtm
import glob, json, logging, string
from operator import __and__, itemgetter
from functools import reduce
from urllib.request import urlopen, Request as urlRequest
from urllib.error import HTTPError, URLError
import rdflib
from rdflib.namespace import RDF, SKOS

from flask import (Flask, request, abort, send_file, session, redirect,
                   make_response, jsonify)
from flask_login import LoginManager, login_required, login_user, logout_user
from werkzeug import exceptions as HTTPCode

from eli_annotation import any2skos
from eli_annotation import auth
from eli_annotation import xslt_transform
from eli_annotation import any2eli
from eli_annotation import vocabs
from eli_annotation import form_configs
from eli_annotation import notices
from eli_annotation import eligraph
from eli_annotation import datamanager
from eli_annotation import errors
from eli_annotation import version
from eli_annotation import localizations


NAME_RESOURCES = {'act': eligraph.ACT_RESOURCE,
                  'journal': eligraph.JOURNAL_RESOURCE,
                  'consolidation': eligraph.CONSOLIDATION_RESOURCE}

# Cache max age for computed files (not the resource files)
CACHE_MAX_AGE = 0

# Defines the Flask application
app = Flask(__name__)
# Sets cache max age for resource files
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 3600

# Defines the data manager object onto the working directory
# Original code defaulted to /tmp/eli-annotation for development, which does not
# survive a reboot (or a well-meaning `rm -rf /tmp/*`). Point it at a persistent,
# project-local directory instead; ELI_ANNOTATION_DATA_DIR overrides both.
_DEV_DATA_DIR = osp.join(osp.dirname(osp.dirname(osp.abspath(__file__))), 'data')
if os.environ.get('ELI_ANNOTATION_DATA_DIR'):
    DATA_INDEX = datamanager.DataIndex(os.environ['ELI_ANNOTATION_DATA_DIR'])
elif osp.exists('/var/lib/eli-annotation'): # system install
    DATA_INDEX = datamanager.DataIndex('/var/lib/eli-annotation')
else:                                     # development
    DATA_INDEX = datamanager.DataIndex(_DEV_DATA_DIR)


# /index to serve the application ##############################################


@app.route('/')
def index():
    response = app.send_static_file('index.html')
    response.headers['Content-Location'] = '/index.html'
    if app.debug:
        response.headers['Cache-Control'] = 'no-cache'
    return response


@app.route('/about')
def about():
    action = best_route([
        ('GET',  '*/*', 'text/html', index),
    ])
    return action()


# Localizations ##############################################


@app.route('/localizations/<lang_code>')
def localization(lang_code):
    local = localizations.get_localization(DATA_INDEX.l10n_dir, lang_code)
    if local is not None:
        response = jsonify(local)
        response.cache_control.max_age = \
                                    app.get_send_file_max_age(lang_code+".json")
        response.cache_control.public = True
        return response
    raise abort(404)


@app.route('/resource/<resource_name>')
@app.route('/resource/<resource_name>/<lang_code>')
def localized_resource(resource_name, lang_code=None):
    data = localizations.get_localized_resource(
        DATA_INDEX.l10n_dir, resource_name, lang_code or "en")
    if data is not None:
        response = make_response(data)
        response.cache_control.max_age = \
            app.get_send_file_max_age(resource_name+(lang_code or "en")+".html")
        response.cache_control.public = True
        return response
    if lang_code is not None:
        return redirect("/resource/"+resource_name, 307)
    raise abort(404)


# helpers ######################################################################


def best_route(routes):
    """
    Take a list of routes: (METHOD, Req content-type, Accept resp content-type)

    return the best action or raise HTTP exception.
    """
    eligible = {}
    method_ok = False
    for method, type_in, type_out, action in routes:
        if method == request.method:
            method_ok = True
            if type_in in ('*/*', request.headers.get('Content-Type')):
                eligible[type_out] = action
    if eligible:
        best = request.accept_mimetypes.best_match(list(eligible))
        if best:
            return eligible[best]
        else:
            raise HTTPCode.NotAcceptable()
    elif method_ok:
        raise HTTPCode.UnsupportedMediaType()
    else:
        raise HTTPCode.MethodNotAllowed()


def jsonify_exceptions(func):
    def wrapped_func(*args):
        try:
            return func(*args)
        except errors.ELIError as exc:
            from traceback import format_exc
            logging.error(format_exc())
            response = jsonify(log_msg=[exc.to_json()])
            response.status_code = 400
            return response
        except Exception as exc:
            from traceback import format_exc
            logging.error(format_exc())
            response = jsonify(log_msg=[{"title": "serverError",
                                         "title_suffix": "",
                                         "details": str(exc)}])
            response.status_code = 500
            return response
    return wrapped_func


def admin_required(func):
    def wrapped_func(*args):
        user = get_current_user()
        if not user["user_admin"]:
            response = jsonify(log_msg=[
                {"title": "unauthorizedOperation",
                 "title_suffix": "",
                 "details": ("You don't have the necessary rights to perform "
                             "this operation.")
                }])
            response.status_code = 401
            return response
        return func(*args)
    return wrapped_func


def detect_filetype(inputfile):
    fname = inputfile.filename
    if fname.endswith('.xls') or fname.endswith('.xlsx'):
        return 'excel'
    elif fname.endswith('.xml') or fname.endswith('.rdf'):
        return 'xml'
    elif fname.endswith('.ttl'):
        return 'ttl'
    elif fname.endswith('.html') or fname.endswith('.xhtml'):
        return 'html'


def make_error_response(msg, status_code):
    return make_response((msg, status_code, {}))

@app.errorhandler(404)
def errorpage404(err):
    msg = 'ELI Annotation Tool. 404 Page not found. Please try <a href="/">home</a> instead.'
    return make_error_response(msg, 404)
@app.errorhandler(405)
def errorpage405(err):
    msg = 'ELI Annotation Tool. 405 Method not allowed. Please try <a href="/">home</a> instead.'
    return make_error_response(msg, 405)
@app.errorhandler(406)
def errorpage406(err):
    msg = 'ELI Annotation Tool. 406 Not acceptable. Please try <a href="/">home</a> instead.'
    return make_error_response(msg, 406)
@app.errorhandler(415)
def errorpage415(err):
    msg = 'ELI Annotation Tool. 415 Unsupported Media Type. Please try <a href="/">home</a> instead.'
    return make_error_response(msg, 415)


# Login ########################################################################


login_manager = LoginManager(app=app)
login_manager.users_database = osp.join(DATA_INDEX.basedir, 'users.json')

@login_manager.user_loader
def load_user(user_id):
    userdb_file = login_manager.users_database
    if not osp.exists(userdb_file):
        return None
    return auth.ELIUser.get(userdb_file, user_id)

def get_current_user():
    answer = dict(user_name='Anonymous', user_admin=False)
    if 'user_id' in session:
        user = load_user(session['user_id'])
        if user is not None:
            answer['user_name'] = user.username
            answer['user_admin'] = user.admin
    return answer

APP_CFG_FILE = osp.join(DATA_INDEX.basedir, 'config.json')
def get_app_config():
    with open(APP_CFG_FILE, encoding='utf-8') as fp:
        appcfg = json.load(fp)
    return appcfg

def _whoami():
    data = get_current_user()
    app_cfg = get_app_config()
    data['lang'] = app_cfg['lang']
    data['toolVersion'] = version.version
    return jsonify(data=data)


@app.route('/whoami', methods=['GET'])
def whoami():
    action = best_route([
        ('GET',  '*/*', 'application/json', _whoami),
    ])
    response = action()
    response.headers['Cache-Control'] = 'no-cache'
    return response

def _login():
    """Login handler for POST request"""
    user_id = request.form['username']
    user = auth.ELIUser.get(login_manager.users_database, user_id)
    if user is None:
        raise abort(401) # wrong user id
    password = request.form['password']
    if not user.check_password(password):
        raise abort(401) # wrong password
    if not user.enabled:
        raise abort(401) # user not enabled
    login_user(user)
    session['user_id'] = user_id
    return jsonify(data=get_current_user())

def _logout():
    logout_user()
    if 'user_id' in session:
        session.pop('user_id')
    return jsonify(data=get_current_user())

@app.route('/login', methods=['GET', 'POST'])
def login():
    action = best_route([
        ('GET', '*/*', 'text/html', index),
        ('POST',  '*/*', '*/*', _login),
    ])
    return action()

@app.route('/logout', methods=['GET', 'POST'])
#@login_required
def logout():
    action = best_route([
        ('GET', '*/*', 'text/html', index),
        ('POST',  '*/*', '*/*', _logout),
    ])
    return action()


# /vocabs ######################################################################


def vocabs_get():
    return jsonify(data=sorted(DATA_INDEX.vocab_index))

@admin_required
@jsonify_exceptions
def vocabs_post():
    # Converts to rdf and adds in vocabulary index
    inputfile = request.files['file']
    ftype = detect_filetype(inputfile)
    add_vocab = {"excel": vocabs.add_excel_vocab,
                 "xml": vocabs.add_xml_vocab,
                 "ttl": vocabs.add_turtle_vocab}
    try:
        add_func = add_vocab[ftype]
    except KeyError as exc:
        msg = ("Unknown file format. Expects Excel, RDF/xml or RDF/ttl for "
               "the input file.")
        raise errors.IncorrectResource("incorrectVocabulary", msg)
    app_cfg = get_app_config()
    uris, warnings = add_func(inputfile, DATA_INDEX.vocab_index,
                              DATA_INDEX.l10n_dir,
                              app_cfg["vocab_langs"], app_cfg["lang"],
                              app_cfg["html_rendering"])
    # http response
    for wrn in warnings:
        logging.warning(str(wrn))
    log_msg = [wrn.to_json() for wrn in warnings]
    if len(log_msg) == 0:
        log_msg = None
    msg = ['Resources created'] if len(uris) > 0 else None
    response = jsonify(log_msg=log_msg,
                       messages=msg)
    response.status_code = 201
    return response

def vocabs_name_get(uri):
    idx = DATA_INDEX.vocab_index
    if uri.endswith('.csv') or uri.endswith('.jsonld') or uri.endswith('.rdf') \
       or uri.endswith('.zip'):
        ext = uri[uri.rfind("."):]
        uri = uri[:uri.rfind(".")]
        if uri in idx:
            fpath = idx.path(uri)+ext
            if osp.exists(fpath):
                return send_file(
                    fpath,
                    max_age=0 if ext == ".jsonld" else CACHE_MAX_AGE)
    elif uri.endswith('.html') or uri.endswith("_html") \
         or uri.endswith("_html/"):
        if '_html/' in uri:
            uri, path = uri.split('_html/')
        else:
            uri, path = uri.split('_html')
        if path == "":
            path = "index.html"
        if uri in idx:
            fpath = osp.join(idx.path(uri)+'_html', path)
            if osp.exists(fpath):
                with open(fpath, encoding='utf-8') as fp:
                    content = fp.read()
                # Rewrites local links in index.html
                if path == "index.html":
                    esc_uri = uri.replace("#","%23").replace("/","%2F")\
                                                    .replace(":","%3A")
                    content = content.replace(
                        '<a href="',
                        '<a href="/vocabs/' + esc_uri + '_html/')
                import io
                response = send_file(
                    io.BytesIO(bytes(content, encoding='utf-8')),
                    mimetype='text/html', max_age=CACHE_MAX_AGE)
                return response
    raise HTTPCode.NotFound()

@admin_required
def vocabs_name_delete(uri):
    vocabs.delete_vocab(uri, DATA_INDEX.vocab_index)
    return jsonify(messages=['Resource deleted'])

# vocabs routes

@app.route('/vocabs', methods=['GET', 'POST'])
@login_required
def vocabs_route():
    action = best_route([
        ('GET',  '*/*', 'text/html', index),
        ('GET',  '*/*', 'application/json', vocabs_get),
        ('POST', '*/*', 'application/json', vocabs_post),
    ])
    response = action()
    response.headers['Vary'] = 'Accept'
    response.headers['Cache-Control'] = 'no-cache'
    return response

@app.route('/vocabs/<path:uri>', methods=['GET','DELETE'])
@login_required
def vocabs_item(uri):
    action = best_route([
        ('GET',    '*/*', '*/*', lambda: vocabs_name_get(uri)),
        ('DELETE', '*/*', 'application/json', lambda: vocabs_name_delete(uri)),
        ])
    return action()

# /notice ######################################################################

def notice_get():
    DATA_INDEX.notice_index.regenerate()
    notices = [ {'uri': uri,
                 'type': infos["type"],
                 'datetime': infos["datetime"] or ""}
                for uri, infos in DATA_INDEX.notice_index.items()]
    notices.sort(key=itemgetter("uri"), reverse=False)
    notices.sort(key=itemgetter("datetime"), reverse=True)
    return jsonify(data=notices)

@jsonify_exceptions
def notice_post():
    json_notice = request.get_json()
    app_cfg = get_app_config()
    user_uri = app_cfg["user_uri_prefix"] + session.get("user_id", "Anonymous")
    uri, rdf_notice = any2eli.form2eli(json_notice, DATA_INDEX.form_index,
                                       DATA_INDEX.vocab_index, user_uri)
    notices.write_notice(
        uri, rdf_notice, json_notice, DATA_INDEX.notice_index,
        DATA_INDEX.l10n_dir, app_cfg["lang"], app_cfg["html_rendering"])
    response = jsonify(messages=['Resource created'])
    response.status_code = 201
    response.headers['Location'] = '/notice/' + uri
    return response

@jsonify_exceptions
def notice_post_rdfa():
    rdf_notice = eligraph.ELIGraph()
    if request.files:
        source = request.files['file']
        if detect_filetype(source) not in ('html', 'xml'):
            msg = ("Unknown file format. Expects RDF/xml or HTML+RDFa for "
                   "the input file.")
            raise errors.IncorrectResource("incorrectEliGraph", msg)
        rdf_notice.parse(source,
                         format=detect_filetype(source),
                         media_type=source.content_type)
    else:
        source = request.form['url']
        rdf_notice.parse(source, format="rdfa")
    if not rdf_notice:
        msg = ("No RDF data found in the input file.")
        raise errors.IncorrectResource("incorrectEliGraph", msg)
    res_type = NAME_RESOURCES[request.form['resource_type']]
    # Builds the form values from the RDF graph and then the JSON data
    uri, form_values = any2eli.eli2form(
        rdf_notice, res_type, DATA_INDEX.form_index, DATA_INDEX.vocab_index)
    json_notice = form_values.json_export()
    any2eli.define_resource_type(rdf_notice, res_type)
    # Saves the notice in the index
    app_cfg = get_app_config()
    notices.write_notice(
        uri, rdf_notice, json_notice, DATA_INDEX.notice_index,
        DATA_INDEX.l10n_dir, app_cfg["lang"], app_cfg["html_rendering"])
    response = jsonify(messages=['RDFa imported'],
                       uri=uri)
    response.status_code = 201
    response.headers['Location'] = '/notice/' + uri
    return response

def notice_name_get(uri):
    idx = DATA_INDEX.notice_index
    if uri.endswith('.json') or uri.endswith('.rdf') or uri.endswith('.zip'):
        ext = uri[uri.rfind("."):]
        uri = uri[:uri.rfind(".")]
        if uri in idx:
            fpath = idx.path(uri)+ext
            if osp.exists(fpath):
                return send_file(
                    fpath,
                    max_age=0 if ext == ".json" else CACHE_MAX_AGE)
    elif uri.endswith('_html') or uri.endswith('_html/') \
         or uri.endswith('.html'):
        if 'legal-expression' in uri:
            uri, path = uri.split('/legal-expressions/')
            path = 'legal-expressions/'+path
        elif 'formats' in uri:
            uri, path = uri.split('/formats/')
            path = 'formats/'+path
        else:
            uri, _ = uri.split("_html")
            path = 'index.html'
        if uri in idx:
            fpath = osp.join(idx.path(uri)+'_html', path)
            if osp.exists(fpath):
                with open(fpath, encoding='utf-8') as fp:
                    content = fp.read()
                # Rewrites local links in index.html
                if path == "index.html":
                    esc_uri = uri.replace("#","%23").replace("/","%2F")\
                                                    .replace(":","%3A")
                    content = content.replace(
                        '<a href="', '<a href="/notice/' + esc_uri + '/')
                import io
                response = send_file(
                    io.BytesIO(bytes(content, encoding='utf-8')),
                    mimetype='text/html', max_age=CACHE_MAX_AGE)
                return response
    raise HTTPCode.NotFound()

@jsonify_exceptions
def notice_name_put(uri):
    assert uri.endswith('.json')
    old_uri = uri[:-5]
    # Deletes old notice files
    notices.delete_notice(old_uri, DATA_INDEX.notice_index)
    # Creates new notice files
    json_notice = request.get_json()
    app_cfg = get_app_config()
    user_uri = app_cfg["user_uri_prefix"] + session.get("user_id", "Anonymous")
    new_uri, rdf_notice = any2eli.form2eli(json_notice, DATA_INDEX.form_index,
                                           DATA_INDEX.vocab_index, user_uri)
    notices.write_notice(new_uri, rdf_notice, json_notice,
                         DATA_INDEX.notice_index, DATA_INDEX.l10n_dir,
                         app_cfg["lang"])
    response = jsonify(messages=['Resource updated'])
    response.status_code = 201 if old_uri != new_uri else 200
    response.headers['Location'] = '/notice/' + uri
    return response

def notice_name_delete(uri):
    notices.delete_notice(uri, DATA_INDEX.notice_index)
    return jsonify(messages=['Resource deleted'])

@app.route('/notice', methods=['GET', 'POST'])
@login_required
def notice():
    action = best_route([
        ('GET',  '*/*', 'text/html', index),
        ('GET',  '*/*', 'application/json', notice_get),
        ('POST', 'application/json', 'application/json', notice_post),
    ])
    response = action()
    response.headers['Vary'] = 'Accept'
    response.headers['Cache-Control'] = 'no-cache'
    return response

@app.route('/notice/import', methods=['GET'])
@login_required
def notice_import_get():
    action = best_route([
        ('GET', '*/*', 'text/html', index),
    ])
    return action()

@app.route('/notice/import', methods=['POST'])
@login_required
def notice_import():
    action = best_route([
        ('POST', '*/*', 'application/json', notice_post_rdfa),
    ])
    response = action()
    response.headers['Vary'] = 'Accept'
    response.headers['Cache-Control'] = 'no-cache'
    return response

@app.route('/notice/<path:uri>', methods=['GET','PUT','DELETE'])
@login_required
def notice_item(uri):
    action = best_route([
        ('GET',    '*/*', '*/*', lambda: notice_name_get(uri)),
        ('PUT',    '*/*', '*/*', lambda: notice_name_put(uri)),
        ('DELETE', '*/*', 'application/json', lambda: notice_name_delete(uri)),
        ])
    return action()

# /form ########################################################################

def form_get(name):
    fpath = DATA_INDEX.form_index.path(name)+'.json'
    if osp.exists(fpath):
        return send_file(fpath, max_age=0)
    elif name.endswith('-values'):
        raise abort(404)
    else:
        return app.send_static_file('forms/default-schema.json')

@admin_required
@jsonify_exceptions
def form_put(name):
    fpath_form = osp.join(DATA_INDEX.form_index.basedir, name + '.json')
    fpath_vals = osp.join(DATA_INDEX.form_index.basedir, name + '-values.json')
    data = request.get_json()
    data['form']['elix:resource_type'] = NAME_RESOURCES[name]
    data['default_values']['elix:resource_type'] = {'value': [NAME_RESOURCES[name]]}
    with open(fpath_form, 'w', encoding='utf-8') as out:
        json.dump(data['form'], out, indent=2, sort_keys=True)
    with open(fpath_vals, 'w', encoding='utf-8') as out:
        json.dump(data['default_values'], out, indent=2, sort_keys=True)
    return jsonify(messages=['Resource updated'])

@app.route('/form', methods=['GET'])
@login_required
def forms():
    action = best_route([
        ('GET', '*/*', 'text/html', index),
    ])
    return action()

@app.route('/form/<name>', methods=['GET','PUT'])
@app.route('/form/<name>/<path:uri>', methods=['GET'])
@login_required
def form(name, uri=None):
    action = best_route([
        ('GET', '*/*', 'text/html', index),
        ('GET', '*/*', 'application/json', lambda: form_get(name)),
        ('PUT', 'application/json', '*/*', lambda: form_put(name)),
    ])
    response = action()
    response.headers['Vary'] = 'Accept'
    response.headers['Cache-Control'] = 'no-cache'
    return response


@app.route('/formconfig', methods=['GET'])
@app.route('/formconfig/<name>', methods=['GET'])
@login_required
def formeconfig(name=None):
    action = best_route([
        ('GET', '*/*', 'text/html', index),
    ])
    return action()

# check_url ############################################################

@app.route('/check_url', methods=['GET'])
@login_required
def check_url():
    if 'application/json' not in request.accept_mimetypes:
        raise HTTPCode.NotAcceptable()
    # Gets the URL to be checked
    url_address = request.args.get("q", "")
    # Gets the user agent (browser) of the incoming request. If it is not
    # defined, chooses a generic recent Firefox
    user_agent = request.headers.get("User-Agent", "Mozilla/5.0")
    # Builds a request towards the URL to be checked and impersonates the
    # browser that has sent the incoming request
    try:
        try:
            req = urlRequest(
                url_address,
                headers={
                    "Accept": ("application/rdf+xml,"
                               "text/rdf+n3,"
                               "application/x-turtle,"
                               "application/xhtml+xml;q=0.9,"
                               "application/html;q=0.8,"
                               "*/*;q=0.5"),
                    "Accept-language": "en-US,en;q=0.9",
                    "Cache-Control": "no-cache",
                    "User-Agent": user_agent,
                })
        except ValueError as exc:
            # URL address is not correct
            code = 400
            msg = str(exc)
        else:
            try:
                with urlopen(req) as response:
                    code = response.getcode()
                    msg = 'URL is valid'
            except HTTPError as exc:
                code = exc.code
                msg = str(exc.reason)
            except URLError as exc:
                # Can't connect to URL address (no network, wrong domain, etc.)
                code = 400
                msg = str(exc.reason)
    except Exception as exc:
        code = 500
        msg = "Unexpected error on server: {0}".format(str(exc))
        from traceback import format_exc
        logging.error("Exception while getting URL: {0}\n{1}"
                      "".format(url_address, format_exc()))
    response = jsonify(url=url_address, http_code=code, msg=msg)
    response.cache_control.max_age = 10
    response.cache_control.public = True
    return response


# commands and main ############################################################

def serve(args):
    try:
        cfg = get_app_config()
    except Exception as exc:
        raise RuntimeError("Can't load configuration of application. Check "
                           "you have run \"configure\" command.") from exc
    app.debug = args.debug
    if "SECRET_KEY" in os.environ:
        app.secret_key = os.environ["SECRET_KEY"]
    else:
        print("no SECRET_KEY found in environment, authentication will not "
              "work")

    host = '0.0.0.0'
    if not app.debug:
        try:
            from raven.contrib.flask import Sentry
            sentry = Sentry(app) # do not forget to set SENTRY_DSN env var
        except ImportError as exc:
            logging.warning("Could not import raven. Sentry monitoring is "
                            "disabled:\n{0}".format(str(exc)))
    # Regenerates the indexes
    if args.regenerate:
        print("Regenerating notices and vocabularies indexes")
        DATA_INDEX.notice_index.regenerate(force=True)
        DATA_INDEX.vocab_index.regenerate(force=True)
    # Runs application server
    print("Starting server on http://{0}:{1}{2}"
          "".format(host, args.port, (" in debug mode" if args.debug else "")))
    app.run(host=host, port=args.port, threaded=True)


def create_user(args):
    try:
        cfg = get_app_config()
    except Exception as exc:
        print("\nCan't load configuration of application. Check "
              "you have run 'configure' command.")
        return
    userdb_file = login_manager.users_database
    if osp.exists(userdb_file):
        try:
            with open(userdb_file, encoding='utf-8') as users_db:
                users = json.load(users_db)
        except Exception as exc:
            from traceback import format_exc
            print("\nThe users file ({0}) is not a valid JSON file and could not "
                  "be loaded.\n{1}".format(userdb_file, format_exc()))
            return
    else:
        users = {}
    import getpass
    user_id = input('User ID: ')
    if user_id in users:
        print("\nA user with \"{}\" id already exists. You should use "
              "'update-user' command instead of 'create-user'.".format(user_id))
        return
    fullname = input("Full name: ")
    fullname = fullname.strip()
    password = getpass.getpass("Password: ")
    if len(password) == 0:
        print("\nEmpty password is not acceptable.")
        return
    password_conf = getpass.getpass("Password (confirm): ")
    if password_conf != password:
        print("\nPassword doesn't match with its confirmation.")
        return
    is_admin = input('Grant admin priviledges [y/N]: ')\
               .strip().lower().startswith('y')
    user_uri = cfg["user_uri_prefix"] + user_id
    print("User URI will be: {}".format(user_uri))
    users[user_id] = {
        'password': auth.hash_password(password),
        'admin': is_admin,
        'fullname': fullname,
        'enabled': True,
    }
    with open(userdb_file, 'w', encoding='utf-8') as users_db:
        json.dump(users, users_db, sort_keys=True)
    print("User {} has been created.".format(user_id))


def edit_user(args):
    try:
        cfg = get_app_config()
    except Exception as exc:
        print("\nCan't load configuration of application. Check "
              "you have run 'configure' command.")
        return
    userdb_file = login_manager.users_database
    if osp.exists(userdb_file):
        try:
            with open(userdb_file, encoding='utf-8') as users_db:
                users = json.load(users_db)
        except Exception as exc:
            from traceback import format_exc
            print("\nThe users file ({0}) is not a valid JSON file and could not "
                  "be loaded.\n{1}".format(userdb_file, format_exc()))
            return
    else:
        users = {}
    import getpass
    user_id = args.user_id
    user = users.get(user_id)
    if user is None:
        print("\nNo user with \"{}\" id exists. You should use 'create-user' "
              "command instead of 'update-user'.".format(user_id))
        return
    fullname = input("Full name [{}]: ".format(user["fullname"]))
    fullname = fullname.strip()
    if len(fullname) > 0:
        user["fullname"] = fullname
    password = getpass.getpass("Password (leave blank to keep old password): ")
    if len(password) > 0:
        password_conf = getpass.getpass("Password (confirm): ")
        if password_conf != password:
            print("\nPassword doesn't match with its confirmation.")
            return
        user["password"] = auth.hash_password(password)
    print("Currently, user has {}been granted admin priviledges."
          "".format("" if user["admin"] else "not "))
    spec_val = "Y/n" if user["admin"] else "y/N"
    admin_txt = input("Grant admin priviledges [{}]: ".format(spec_val))\
                .strip().lower()
    is_admin = not(admin_txt.startswith("n")) if user["admin"] \
               else admin_txt.startswith("y")
    user["admin"] = is_admin
    print("Currently, user is {}."
          "".format("enabled" if user["enabled"] else "disabled"))
    spec_val = "Y/n" if user["enabled"] else "y/N"
    enab_txt = input("Enable user [{}]: ".format(spec_val))\
                .strip().lower()
    is_enabled = not(enab_txt.startswith("n")) if user["admin"] \
                 else enab_txt.startswith("y")
    user["enabled"] = is_enabled
    user_uri = cfg["user_uri_prefix"] + user_id
    print("User URI is: {}".format(user_uri))
    with open(userdb_file, 'w', encoding='utf-8') as users_db:
        json.dump(users, users_db, sort_keys=True)
    print("User {} has been updated.".format(user_id))


def list_users(args):
    try:
        cfg = get_app_config()
    except Exception as exc:
        print("\nCan't load configuration of application. Check "
              "you have run 'configure' command.")
        return
    userdb_file = login_manager.users_database
    if osp.exists(userdb_file):
        try:
            with open(userdb_file, encoding='utf-8') as users_db:
                users = json.load(users_db)
        except Exception as exc:
            from traceback import format_exc
            print("\nThe users file ({0}) is not a valid JSON file and could not "
                  "be loaded.\n{1}".format(userdb_file, format_exc()))
            return
    else:
        users = {}
    out_list = []
    for user_id, user in sorted(users.items()):
        out_list.append({"user id": user_id,
                         "user URI": cfg["user_uri_prefix"] + user_id,
                         "user name": user["fullname"],
                         "enabled": "yes" if user["enabled"] else "no",
                         "admin": "yes" if user["admin"] else "no"
        })
    import csv
    fields = ["user id", "user URI", "user name", "enabled", "admin"]
    if args.output:
        with open(args.output, "w", encoding="utf-8") as out:
            wrt = csv.DictWriter(out, fieldnames=fields)
            wrt.writeheader()
            for line in out_list:
                wrt.writerow(line)
    else:
        import sys
        wrt = csv.DictWriter(sys.stdout, fieldnames=fields)
        wrt.writeheader()
        for line in out_list:
            wrt.writerow(line)


def app_config(args):
    msg = "** ELI Annotation Tool - Configuration **"
    print("{0}\n{1}\n{0}".format("*"*len(msg), msg))
    cfg = {}
    # Deploys standard localization files if none are present
    loc_files = list(glob.glob(osp.join(DATA_INDEX.l10n_dir,'*.json')))
    if len(loc_files) == 0:
        print("\n* Deploying standard localization files...")
        localizations.deploy_standard_localizations(DATA_INDEX.l10n_dir)
        xslt_transform.build_xml_glossary(DATA_INDEX.l10n_dir)
    # Languages
    print("\n* Languages")
    languages = localizations.list_installed_localizations(DATA_INDEX.l10n_dir)
    assert len(languages) > 0, "No languages found in localizations directory"
    print("\nAvailable languages are: {0}".format(" ".join(languages)))
    # Chooses interface language
    lang = None
    while lang not in languages:
        lang = input("\nChoose the language of the user interface (one code)"
                     "\n? ")
        lang = lang.strip()
    cfg["lang"] = lang
    # Chooses vocabulary HTML languages
    langs = []
    while len(langs) == 0 \
          or not reduce(__and__, [lng in languages for lng in langs]):
        langs = input("\nChoose the languages for the vocabulary rendering in "
                      "HTML (one or several codes separated by spaces)\n? ")
        langs = langs.split()
    cfg["vocab_langs"] = langs
    # Chooses users' URI prefix
    print("\n* User URIs")
    prefix = input("\nChoose the URI prefix for the users (will be added "
                   "before the user ID to build an URI; this URI indicates who "
                   "created a notice)\n? ")
    cfg["user_uri_prefix"] = prefix
    # Chooses HTML rendering
    print("\n * HTML rendering")
    print("\nThe HTML rendering of the vocabularies and the notices can contain"
          ": ")
    print("[1] Only metadata inside the HTML header for describing the objets "
          "in RDFa and schema.org standards")
    print("[2] metadata inside the HTML header AND actual content in the HTML "
          "body for displaying the objects in human-readable text")
    print("\nIf you don't know what to choose, choose 2.")
    choice = None
    while choice not in ("1", "2"):
        choice = input("\nEnter your choice (1 or 2)\n? ").strip()
    cfg["html_rendering"] = xslt_transform.ONLY_METADATA if choice == "1" \
                            else xslt_transform.WHOLE_PAGE
    # Writes configuration
    with open(APP_CFG_FILE, 'w', encoding='utf-8') as fp:
        json.dump(cfg, fp)
    # Deploys standard localized resource files if none are present
    for res_name in (localizations.ABOUT, localizations.EXCEL_VOCAB_DOC):
        loc_files = list(glob.glob(
            osp.join(DATA_INDEX.l10n_dir, res_name+'.*.html')))
        if len(loc_files) == 0:
            print("\n* Deploying standard {0} files...".format(res_name))
            localizations.deploy_standard_localized_resources(
                DATA_INDEX.l10n_dir, res_name)
    # Deploys standard vocabularies if none are present
    DATA_INDEX.vocab_index.regenerate()
    if len(DATA_INDEX.vocab_index) == 0:
        print("\n* Deploying standard vocabularies...")
        vocabs.deploy_standard_vocabs(DATA_INDEX.vocab_index,
                                      DATA_INDEX.l10n_dir,
                                      cfg["vocab_langs"], cfg["lang"])


def add_localization(args):
    # Tries to load JSON data
    try:
        with open(args.filename, encoding="utf-8") as inp:
            local = json.load(inp)
    except Exception as exc:
        from traceback import format_exc
        print("Can't read input JSON file:\n{}".format(format_exc()))
        return
    valid, errors = localizations.check_localization(local)
    if not valid:
        print("The JSON file is not a valid localization file because of:\n{}"
              "".format("\n".join(errors)))
        return
    def_code = local.get("langCode", "").strip().lower()
    print("Enter the language (two-letters code) this localization file will "
          "be added for")
    ok = False
    while not ok:
        lang_code = input("[{}]? ".format(def_code)).strip().lower()
        if lang_code == "":
            lang_code = def_code
        ok = (len(lang_code) == 2 and lang_code[0] in string.ascii_letters
              and lang_code[1] in string.ascii_letters)
    localizations.store_localization(DATA_INDEX.l10n_dir, lang_code, local)
    xslt_transform.build_xml_glossary(DATA_INDEX.l10n_dir)


def get_localization(args):
    print("Enter the language (two-letters code) of the localization file you "
          "want to get")
    ok = False
    while not ok:
        lang_code = input("? ").strip().lower()
        ok = (len(lang_code) == 2 and lang_code[0] in string.ascii_letters
              and lang_code[1] in string.ascii_letters)
    data = localizations.get_localization(DATA_INDEX.l10n_dir, lang_code)
    if data is None:
        print("No localization JSON file for {} language, returning default "
              "file (with English data)".format(lang_code))
        data = localizations.get_default_localization()
        data["langCode"] = lang_code
    if args.output:
        with open(args.output, "w", encoding="utf-8") as out:
            json.dump(data, out, ensure_ascii=False, indent=True)
    else:
        import sys
        json.dump(data, sys.stdout, ensure_ascii=False, indent=True)


def add_localized_resource(args):
    # Reads and checks input file
    try:
        with open(args.filename, mode="rb") as inp:
            data = inp.readlines()
    except Exception as exc:
        from traceback import format_exc
        print("Can't read input file:\n{}".format(format_exc()))
        return
    print("Choose the resource described in this file")
    print("[1] About text of ELI Annotation Tool")
    print("[2] Documentation of Excel vocabulary files")
    res_choice = None
    while res_choice not in ("1", "2"):
        res_choice = input("\nEnter your choice (1 or 2)\n? ").strip()
    print("\nEnter the language (two-letters code) this resource file will "
          "be added for")
    ok = False
    while not ok:
        lang_code = input("? ").strip().lower()
        ok = (len(lang_code) == 2 and lang_code[0] in string.ascii_letters
              and lang_code[1] in string.ascii_letters)
    res_names = {"1": localizations.ABOUT,
                 "2": localizations.EXCEL_VOCAB_DOC}
    localizations.store_localized_resource(
        DATA_INDEX.l10n_dir, res_names[res_choice], lang_code, b"".join(data))


def get_localized_resource(args):
    print("Choose the resource you want to get")
    print("[1] About text of ELI Annotation Tool")
    print("[2] Documentation of Excel vocabulary files")
    res_choice = None
    while res_choice not in ("1", "2"):
        res_choice = input("\nEnter your choice (1 or 2)\n? ").strip()
    print("\nEnter the language (two-letters code) of this resource you "
          "want to get")
    ok = False
    while not ok:
        lang_code = input("? ").strip().lower()
        ok = (len(lang_code) == 2 and lang_code[0] in string.ascii_letters
              and lang_code[1] in string.ascii_letters)
    res_names = {"1": localizations.ABOUT,
                 "2": localizations.EXCEL_VOCAB_DOC}
    data = localizations.get_localized_resource(
        DATA_INDEX.l10n_dir, res_names[res_choice], lang_code)
    if data is None:
        print("This resource doesn't exist in {} language, returning resource "
              "in English".format(lang_code))
        data = localizations.get_localized_resource(
            DATA_INDEX.l10n_dir, res_names[res_choice], "en")
    if args.output:
        with open(args.output, "wb") as out:
            out.write(data)
    else:
        import sys, os
        with os.fdopen(sys.stdout.fileno(), "wb") as out:
            out.write(data)



if __name__ == '__main__':
    import argparse
    import sys

    desc = """Controls the ELI annotation tool.

Various commands are available to configure, manage users, manage localizations
and start the application. You can use the -h option to have a list of the
available commands. You can also type a command followad by the -h option to
have details on this command.
"""
    parser = argparse.ArgumentParser(description=desc)
    subparsers = parser.add_subparsers()

    # Configure
    configure_parser = subparsers.add_parser(
        'configure', help='configure application')
    configure_parser.set_defaults(func=app_config)

    # Create user
    add_user_parser = subparsers.add_parser(
        'create-user', help='create user')
    add_user_parser.set_defaults(func=create_user)

    # Edit user
    edit_user_parser = subparsers.add_parser(
        'edit-user', help='edit user')
    edit_user_parser.add_argument(
        'user_id', type=str, help='the id of the user to be edited')
    edit_user_parser.set_defaults(func=edit_user)

    # List users
    get_local_parser = subparsers.add_parser(
        'list-users', help='lists the existing users in a CSV file')
    get_local_parser.add_argument(
        '--output', metavar="filename", type=str,
        help='the file where to store the users')
    get_local_parser.set_defaults(func=list_users)

    # Add localization
    add_local_parser = subparsers.add_parser(
        'add-localization', help='add a localization JSON file')
    add_local_parser.add_argument(
        'filename', type=str, help='the localization file to be added')
    add_local_parser.set_defaults(func=add_localization)

    # Get localization
    get_local_parser = subparsers.add_parser(
        'get-localization', help='get a localization JSON file')
    get_local_parser.add_argument(
        '--output', metavar="filename", type=str,
        help='the file where to store the localization')
    get_local_parser.set_defaults(func=get_localization)

    # Add localized resource
    add_res_parser = subparsers.add_parser(
        'add-resource', help=('add a localized resource (About text or Excel '
                              'vocabulary documentation)'))
    add_res_parser.add_argument(
        'filename', type=str, help=('the localized resource file to be added '
                                    '(HTML file)'))
    add_res_parser.set_defaults(func=add_localized_resource)

    # Get localized resource
    get_res_parser = subparsers.add_parser(
        'get-resource', help=('get a localized resource (About text or Excel '
                              'vocabulary documentation)'))
    get_res_parser.add_argument(
        '--output', metavar="filename", type=str,
        help='the file where to store the localized resource')
    get_res_parser.set_defaults(func=get_localized_resource)

    # Serve
    serve_parser = subparsers.add_parser('serve', help='start Flask server')
    serve_parser.add_argument('--port', metavar='port', type=int, default=5000,
                              help='port the server will listen to')
    serve_parser.add_argument('--debug', action='store_true',
                              help='set debug mode')
    serve_parser.add_argument('--regenerate', action='store_true',
        help=('regenerate indexes of vocabularies and notices before starting '
              'the server'))
    serve_parser.set_defaults(func=serve)

    # Parses args and calls corresponding function
    args = parser.parse_args()
    if hasattr(args, 'func'):
        sys.exit(args.func(args))
    else:
        sys.exit(parser.print_usage())
