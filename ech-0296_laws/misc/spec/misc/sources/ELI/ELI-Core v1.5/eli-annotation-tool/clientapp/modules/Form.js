// -*- coding: utf-8 -*-
// Project sponsor is https://ec.europa.eu/isa2/
// License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

/* global fetch */

//@flow
import React from 'react';
import { Link } from 'react-router';
import { api_fetch } from './API';
import FE from './FormElements';
import NC from './NotifComponent';

const ManageForms = (props) => (
        <div className="container">
        <h1>{props.localize("forms")}</h1>

        <div className="formLinks row">

        <Link to="/formconfig/act" className="col-md-offset-3 col-md-2">
        <button className="btn btn-primary">{props.localize("configureFormFor")} <span className="typeOfForm">{props.localize("act")}</span></button>
        </Link>

        <Link to="/formconfig/journal" className="col-md-2">
        <button className="btn btn-primary">{props.localize("configureFormFor")} <span className="typeOfForm">{props.localize("journal")}</span></button>
        </Link>

        <Link to="/formconfig/consolidation" className="col-md-2">
        <button className="btn btn-primary">{props.localize("configureFormFor")} <span className="typeOfForm">{props.localize("consolidation")}</span></button>
        </Link>

        </div>
        </div>
);

const bool = (x) => x ? true : false;

const validate_config = (schema, values, path, uri_vars, vocabs, loc_function) => {
    const value = FE.traverse_values(values, path);
    const schema_node = FE.traverse_schema(schema, path);
    if (value === undefined || schema_node === undefined) {
        return ;
    }
    if (schema_node.vocab === undefined) {
        value.config_invalid = false;
        value.config_msg = "";
    } else {
        if (schema_node.vocab === null && (schema_node.enabled || uri_vars.has(FE.path2Id0(path)))) {
            value.config_invalid = true;
            value.config_msg = loc_function("missingFieldVocabulary");
        } else if (uri_vars && vocabs && uri_vars.has(FE.path2Id0(path))) {
            const missings = FE.missingVocabNotations(vocabs[schema_node.vocab]);
            if (missings.length > 0) {
                value.config_invalid = true;
                value.config_msg = loc_function("missingNotationsInVocabulary");
            } else {
                value.config_invalid = false;
                value.config_msg = "";
            }
        } else {
            value.config_invalid = false;
            value.config_msg = "";
        }
    }
};

const validate_configs = (schema, values, state, loc_function) => {
    if (state) {
        FE.enumerate_values_paths(values)
            .forEach(path => validate_config(schema, values, path, state.uri_vars, state.vocabs, loc_function));
    }
};

const check_vocabs_in_schema = (schema, available_vocabs) => {
    FE.enumerate_schema_paths(schema).forEach(
        path => {
            if (path.length > 0 && (path[0] !== "elix:languages_list" && path[0] !== "elix:formats_list")) {
                const schema_node = FE.traverse_schema(schema, path);
                if (schema_node.vocab !== undefined && schema_node.vocab !== null) {
                    if (! available_vocabs.includes(schema_node.vocab)) {
                        schema_node.vocab = null;
                    }
                }
            }
        });
}

const getInvalidConfigs = (values) => {
    const vals = FE.enumerate_values_paths(values);
    return vals.filter(path => bool(FE.traverse_values(values, path).config_invalid === true));
};

const resource_type = {'act': 'Act',
                       'journal': 'OfficialJournal',
                       'consolidation': 'Consolidation'};

const export_schema = (schema, form_name, top_level=true) => {
    const exported_schema = {}
    Object.entries(schema).forEach(entry => {
        if (entry[0] === "properties") {
            exported_schema.properties = export_schema(entry[1], form_name, false);
        } else if (top_level && (entry[0] === "id" || entry[0] === "$schema")) {
            const items = entry[1].split(":");
            items[items.length-2] = resource_type[form_name];
            const now = new Date();
            items[items.length-1] = now.toISOString();
            exported_schema[entry[0]] = items.join(":");
        } else {
            exported_schema[entry[0]] = entry[1];
        }
    });
    return exported_schema;
};

const export_values = (values, form_name, top_level=true) => {
    const exported_values = {}
    Object.entries(values).forEach(entry => {
        if (entry[0].startsWith("lang_") || entry[0].startsWith("format_")) {
            exported_values[entry[0]] = export_values(entry[1], form_name, false);
        } else {
            exported_values[entry[0]] = {value: entry[1].value,
                                         config_invalid: entry[1].config_invalid,
                                         valid: entry[1].valid};
        }
    });
    if (top_level) {
        exported_values['elix:resource_type'] = {value: "elix:"+resource_type[form_name]};
    }
    return exported_values;
};


class Form extends NC.NotifComponent {
    constructor(props) {
        super(props);
	Object.assign(this.state, {
            ui_description: null,
            schema: null,
            miniatures : null,
            values: {},
            available_vocabs: null,
            vocabs: {},
            lang_vocab_name: null,
            format_vocab_name: null,
            uri_vars: new Set(),
            edit_mode: props.route.path.includes('formconfig') // XXX UGLY
        });
	this.loadDataFromServer = this.loadDataFromServer.bind(this);
	this.dispatch = this.dispatch.bind(this);
        this.loadVocab = this.loadVocab.bind(this);
    }
    loadDataFromServer() {
        const downloads = [];
        downloads.push(api_fetch('/vocabs', 'GET')
	               .then(response => response.json()));
        downloads.push(api_fetch('/form/'+this.props.params.formName, 'GET')
	               .then(response => response.json()));
        downloads.push(this.props.params.noticeURI
                       ? (api_fetch('/notice/'+this.props.params.noticeURI+'.json', 'GET')
                          .then(response => response.json()))
                       : (api_fetch('/form/'+this.props.params.formName+'-values', 'GET')
                          .then(response => (response.ok ? response.json() : {})))
                      );
        downloads.push(fetch('/static/forms/ui-definition.json')
                       .then(response => response.json()));
        downloads.push(fetch('/static/miniatures.json')
                       .then(response => response.json()));

        Promise.all(downloads).then(results => {
            const [vocab, form, values, ui, minis] = results;
            const state = {available_vocabs: vocab.data,
                           schema: form,
                           ui_description: ui,
                           miniatures: minis,
                           edit_mode: this.state.edit_mode
                          };
            const langs_node = FE.traverse_schema(form, ["elix:languages_list"]);
            if (langs_node !== undefined) {
                state.lang_vocab_name = langs_node.vocab;
            }
            const formats_node = FE.traverse_schema(form, ["elix:formats_list"]);
            if (formats_node !== undefined) {
                state.format_vocab_name = formats_node.vocab;
            }
            check_vocabs_in_schema(form, vocab.data);
            state.values = FE.init_values(form, values);
            state.uri_vars = FE.compute_uri_vars(state.values);
            FE.validate_values(form, state.values, state, this.props.localize);
            validate_configs(form, state.values, state, this.props.localize);
            this.setState(state);
            vocab.data.map(name => this.loadVocab(name));
        });
    }
    loadVocab(name) {
	api_fetch('/vocabs/'+encodeURIComponent(name)+'.jsonld', 'GET') // XXX set content-type
	    .then(response => response.json())
            .then(json => {
                this.setState(prevState => {
                    const vocabs = Object.assign({}, prevState.vocabs);
                    vocabs[name] = json;
                    return {vocabs};
                });
            validate_configs(this.state.schema, this.state.values, this.state, this.props.localize);
            });
    }
    componentDidMount() {
	this.loadDataFromServer();
    }
    dispatch(action) {
        //console.log('dispatch',action);
        switch(action.type) {
        case 'TOGGLE_ENABLE':
            this.setState(prevState => {
                const node = FE.traverse_schema(prevState.schema, action.path);
                node.enabled = !node.enabled;
                node.mandatory = (!node.enabled ? false : node.mandatory);
                if (node.vocab !== undefined) {
                    validate_config(prevState.schema, prevState.values, action.path, prevState.uri_vars, prevState.vocabs, this.props.localize);
                    FE.reset_value(prevState.schema, prevState.values, action.path, prevState, this.props.localize);
                }
                return {schema: prevState.schema};
            });
            break;
        case 'TOGGLE_MANDATORY':
            this.setState(prevState => {
                const node = FE.traverse_schema(prevState.schema, action.path);
                node.mandatory = !node.mandatory;
                return {schema: prevState.schema};
            });
            break;
        case 'SET_VOCAB':
            this.setState(prevState => {
                const node = FE.traverse_schema(prevState.schema, action.path);
                node.vocab = (action.value === undefined ? null : action.value);
                validate_config(prevState.schema, prevState.values, action.path, prevState.uri_vars, prevState.vocabs, this.props.localize);
                FE.reset_value(prevState.schema, prevState.values, action.path, prevState, this.props.localize);
                return {schema: prevState.schema};
            });
            break;
        case 'SET_VALUE':
            this.setState(prevState => {
                if(action.path[0] === 'elix:languages_list'
                   || action.path[0] === 'elix:formats_list') {
                    // remove from schema
                    const keys = Object.keys(prevState.schema.properties);
                    keys.map(k => k.startsWith('lang_') && delete prevState.schema.properties[k]);
                    // get sets
                    let languages = (action.path[0] === 'elix:languages_list'
                                     ? action.value
                                     : FE.traverse_values(prevState.values, ['elix:languages_list']).value);
                    let formats = (action.path[0] === 'elix:formats_list'
                                   ? action.value
                                   : FE.traverse_values(prevState.values, ['elix:formats_list']).value);
                    // recreate schema nodes
                    const deepcopy = (x) => JSON.parse(JSON.stringify(x));
                    languages.map(uri => {
                        const lkey = 'lang_'+uri.split('/').splice(-1);
                        const lang = deepcopy(prevState.schema.factories.lang_);
                        formats.map(uri => {
                            const fkey = 'format_'+uri.split('/').splice(-1);
                            const fmt = deepcopy(prevState.schema.factories.format_);
                            fmt.title = uri;
                            lang.properties[fkey] = fmt;
                        });
                        lang.title = uri;
                        prevState.schema.properties[lkey] = lang;
                    });
                    prevState.values = FE.init_values(prevState.schema, prevState.values);
                    FE.validate_values(prevState.schema, prevState.values, prevState, this.props.localize);
                    validate_configs(prevState.schema, prevState.values, prevState, this.props.localize);
                }
                const validation = FE.validate_value(prevState.schema, action.path, action.value, prevState, this.props.localize);
                const value = FE.traverse_values(prevState.values, action.path);
                value.value = action.value;
                value.valid = validation.valid;
                value.msg = validation.msg;
                const state = {values: prevState.values,
                               schema: prevState.schema};
                if(FE.URISCHEME_KEYS.includes(action.path[0])) {
                    state.uri_vars = FE.compute_uri_vars(prevState.values);
                    FE.URISCHEME_KEYS.forEach(key => {
                        const value = FE.traverse_values(state.values, [key]);
                        const validation = FE.validate_value(prevState.schema, [key], value.value, prevState, this.props.localize);
                        value.valid = validation.valid;
                        value.msg = validation.msg;
                    });
                    state.uri_vars.forEach(uri_var => {
                        const path = uri_var.split("--");
                        const schema_node = FE.traverse_schema(state.schema, path);
                        if (schema_node && !schema_node.enabled) {
                            schema_node.enabled = true;
                        }
                        validate_config(state.schema, state.values, path, state.uri_vars, prevState.vocabs, this.props.localize);
                    })
                }
                return state;
            });
            break;
        case 'SET_URL_VALIDITY':
            this.setState(prevState => {
                const value = FE.traverse_values(prevState.values, action.path);
                // Defines validity dictionary if it doesn't exist
                if (value.url_valids === undefined) {
                    value.url_valids = {}
                }
                // Deletes keys corresponding to values that don't exist anymore
                Object.keys(value.url_valids).slice().forEach(val => {
                    if (! value.value.includes(val)) {
                        delete value.url_valids[val];
                    }
                });
                // Adds new URL validity of value (if it still exists)
                if (value.value.includes(action.value)) {
                    value.url_valids[action.value] = {
                        valid: action.valid,
                        msg: action.msg
                    };
                }
                return {values: prevState.values};
            });
            break;
        default:
            console.warn("Unknown action", action);
        }
    }
    submitForm(event) {
        event.preventDefault();
        let prom = null;
        if(this.state.edit_mode) {
            fetch("/form/" + this.props.params.formName,
                  {method: "PUT",
                   headers: {'Content-Type': 'application/json'},
                   credentials: 'include',
                   body: JSON.stringify({form: export_schema(this.state.schema, this.props.params.formName),
                                         default_values: export_values(this.state.values, this.props.params.formName)})
                  })
                .then(response => {
                    if(response.ok) {
                        response.json().then(json => {
                            if (json.log_msg === null || json.log_msg === undefined) {
                                this.closeForm();

                            } else {
                                this.buildNotif("warning", json.log_msg);
                            }
                        });
                    } else {
                        response.json().then(
                            json => this.buildNotif("error",  json.log_msg)
                        );
                    }
                })
	        .catch(error => this.buildNotif("error", [{"title": "clientError",
                                                           "details": error.toString()}])
                      );
            this.buildNotif("info", [{"title": "processing",
                                      "details": ""}]);
        } else {
            let query = {headers: {'Content-Type': 'application/json'},
                         credentials: 'include',
                         body: JSON.stringify(export_values(this.state.values, this.props.params.formName))
                        };
            let url = '/notice';
            if(this.props.params.noticeURI) {
                query.method = 'PUT';
                url = url + '/' +this.props.params.noticeURI+'.json';
            } else {
                query.method = 'POST';
            }
            fetch(url, query)
                .then(response => {
                    if(response.ok) {
                        response.json().then(json => {
                            if (json.log_msg === null || json.log_msg === undefined) {
                                this.closeForm();

                            } else {
                                this.buildNotif("warning", json.log_msg);
                            }
                        });
                    } else {
                        response.json().then(
                            json => this.buildNotif("error",  json.log_msg)
                        );
                    }
                })
	        .catch(error => this.buildNotif("error", [{"title": "clientError",
                                                           "details": error.toString()}])
                      );
            this.buildNotif("info", [{"title": "processing",
                                      "details": ""}]);
        }
    }
    closeForm() {
        (this.state.edit_mode
         ? this.context.router.push('/formconfig')
         : this.context.router.push('/notice'));
    }
    render() {
        const loc = this.props.localize;
        if (this.state.vocabs === null
            || this.state.schema === null
            || this.state.ui_description === null
            || this.state.miniatures === null) {
            return (<p>{loc("loading")}</p>);
        } else {
            const invalidValueIds = FE.getInvalidValues(this.state.values);
            const invalidConfigIds = getInvalidConfigs(this.state.values);
            const invalidURLIds = FE.getInvalidURLs(this.state.values);
            const form_invalid = bool(invalidValueIds.length + invalidConfigIds.length > 0);
            const submit_button_class = ['btn','btn-primary'];
            if(form_invalid) submit_button_class.push('disabled');
            const close_button = (<button type='button'
                                  className={'btn'}
                                  onClick={(e) => this.closeForm()}
                                  >{loc("close")}</button>);
            const submit_button_label = (this.state.edit_mode ? loc("saveForm") : loc("saveNotice"));
            const submit_button = (form_invalid
                                   ?
                                   (<button type='submit'
                                    className={submit_button_class.join(' ')}
                                    disabled={true}
                                    >{submit_button_label}</button>)
                                   :
                                   (<button type='submit'
                                    className={submit_button_class.join(' ')}
                                    onClick={(e) => this.submitForm(e)}
                                    >{submit_button_label}</button>));
            const title = (this.state.edit_mode ? loc("configureFormFor") : loc("createNoticeFor"))
                +" "+loc(this.props.params.formName);
            // Computes invalid messages
            const getTitle = (path) => {
                return FE.full_title(path, this.state, this.props.lang, loc);
            };
            let invalidFieldMsg = null;
            if(form_invalid) {
                const invalidValueItems = invalidValueIds.sort().map(path => (
                        <li key={'invalidmsg'+FE.path2Id(path)} className="clickable" onClick={(e) => FE.jumpAndShow(FE.path2Id(path))}><strong>
                        {getTitle(path)}</strong></li>));
                const invalidConfigItems = invalidConfigIds.sort().map(path => (
                        <li key={'invalidcfg'+FE.path2Id(path)} className="clickable" onClick={(e) => FE.jumpAndShow(FE.path2Id(path))}><strong>
                        {getTitle(path)}</strong></li>));
                invalidFieldMsg = (<div id='invalidMsg' className="error-messages">
                              {((invalidConfigItems.length > 0) ? (<p>{loc("invalidConfigFields")}</p>): "")}
                              {((invalidConfigItems.length > 0) ? (<ul>{invalidConfigItems}</ul>) : "")}
                              {((invalidValueItems.length > 0) ? (<p>{loc("invalidValueFields")}</p>): "")}
                              {((invalidValueItems.length > 0) ? (<ul>{invalidValueItems}</ul>) : "")}
                              </div>);
            }
            let invalidUrlMsg = null;
            if (invalidURLIds.length > 0) {
                const invalidURLItems = invalidURLIds.sort().map(path => (
                        <li key={'invalidurl'+FE.path2Id(path)} className="clickable" onClick={(e) => FE.jumpAndShow(FE.path2Id(path))}><strong>
                        {getTitle(path)}</strong></li>));
                invalidUrlMsg = (<div id='urlMsg' className="warning-messages">
                          <p>{loc("invalidURLFields")}</p>
                          <ul>{invalidURLItems}</ul>
                          </div>);
            }
            const urischemesection = (this.state.edit_mode
                                      ? React.createElement(FE.EditableURISchemeSection,
                                                            {state: this.state,
                                                             dispatch: this.dispatch,
                                                             localize: loc,
                                                             lang: this.props.lang})
                                      : React.createElement(FE.URISchemeSection,
                                                            {state: this.state,
                                                             dispatch: this.dispatch,
                                                             localize: loc,
                                                             lang: this.props.lang}));
            const langformatsection = (this.state.edit_mode
                                       ? React.createElement(FE.EditableLangFormatSection,
                                                             {state: this.state,
                                                              dispatch: this.dispatch,
                                                              localize: loc,
                                                              lang: this.props.lang})
                                       : null);
            return (<div className="container">
                    <h1>{title}</h1>
                    <form className='form'>
                    {urischemesection}
                    {langformatsection}
                    {FE.renderChildren(this.state.ui_description.definitions.main.content,
                                       {state: this.state,
                                        dispatch: this.dispatch,
                                        localize: loc,
                                        lang: this.props.lang
                                       },
                                       [])}
                    {invalidFieldMsg}
                    {invalidUrlMsg}
                    <div className='row'>
                    <div className='col-sm-3'>
                    {submit_button}
                    </div>
                    <div className='col-sm-3'>
                    {close_button}
                    </div>
                    </div>
                    </form>
                    {this.renderNotif(this.props.localize)}
                    </div>
            ); // XXX do nothing if button disabled
        }
    }
};
Form.contextTypes = {
    router: React.PropTypes.object.isRequired
};

export { ManageForms, Form };
