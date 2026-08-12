// -*- coding: utf-8 -*-
// Project sponsor is https://ec.europa.eu/isa2/
// License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import React from 'react';
import moment from 'moment';
import { Link } from 'react-router';
import { api_fetch } from './API';
import NC from './NotifComponent';

const TYPE_MAP = {
    'elix:Act': 'act',
    'elix:OfficialJournal': 'journal',
    'elix:Consolidation': 'consolidation'
};

const format_datetime = (dtime_str) => {
    if (dtime_str === "" || dtime_str === null || dtime_str === undefined) {
        return "";
    }
    const dtime = moment(dtime_str);
    return dtime.format("YYYY-MM-DD HH:mm:ss");
};

class Notice extends React.Component {
    constructor(props, context) {
	super(props);
	this.state = {
            data: null
        };
	this.loadDataFromServer = this.loadDataFromServer.bind(this);
        this.onDelete = this.onDelete.bind(this);
    }
    loadDataFromServer() {
        api_fetch('/notice', 'GET')
	    .then(response => response.json())
            .then(jsdata => this.setState({data: jsdata.data}));
    }
    onDelete(e, name) {
        e.preventDefault();
        api_fetch('/notice/'+encodeURIComponent(name), 'DELETE')
            .then(() => {this.loadDataFromServer();});
    }
    componentDidMount() {
	this.loadDataFromServer();
    }

    render() {
        const loc = this.props.localize;
        const rows = ((this.state.data === null)
                      ? (<p>{loc("loading")}</p>)
                      : ((this.state.data.length === 0) ?
                         (<p>{loc("noNotice")}</p>) :
                         (<table className="table table-condensed">
                          <tbody>
                          {this.state.data
                           .map(item => <tr key={item.uri}><td>{item.uri}</td>
                                <td>{loc(item.type, "eliOntologyExtension")}</td>
                                <td>{format_datetime(item.datetime)}</td>
                                <td><a href={'/notice/'+encodeURIComponent(item.uri+'_html')}>{loc("previewHtml")}</a></td>
                                <td><a href={'/notice/'+encodeURIComponent(item.uri+'.rdf')}>{loc("downloadRdf")}</a></td>
                                <td><a href={'/notice/'+encodeURIComponent(item.uri+'.zip')}>{loc("downloadZip")}</a></td>
                                <td><Link to={'/form/'+TYPE_MAP[item.type]+'/'+encodeURIComponent(item.uri)}>{loc("edit")}</Link></td>
                                <td><button onClick={(e) => this.onDelete(e, item.uri)} title={loc("deleteNotice")}>
                                <span className="glyphicon glyphicon-trash"></span></button></td>
                                </tr>)
                          }
                          </tbody>
                          </table>)
                        ));
        return (<div className="container">
                <h1>{loc("notices")}</h1>

                <div className="formLinks row">

                <Link to="/form/act" className="col-md-offset-2 col-md-2">
                <button className="btn btn-primary">{loc("createNoticeFor")}<span className="typeOfForm">{loc("act")}</span></button>
                </Link>

                <Link to="/form/journal" className="col-md-2">
                <button className="btn btn-primary">{loc("createNoticeFor")}<span className="typeOfForm">{loc("journal")}</span></button>
                </Link>

                <Link to="/form/consolidation" className="col-md-2">
                <button className="btn btn-primary">{loc("createNoticeFor")}<span className="typeOfForm">{loc("consolidation")}</span></button>
                </Link>

                <Link to="/notice/import" className="col-md-2">
                <button className="btn btn-primary">{loc("importNoticeFrom")}<span className="typeOfForm">{loc("rdfa")}</span></button>
                </Link>
                </div>

                <h2>{loc("workInProgress")}</h2>
                {rows}

                </div>
               );
    }
}

class NoticeRdfImport extends NC.NotifComponent {
    constructor(props, context) {
	super(props);
        Object.assign(this.state, {
            notification: null,
            formValid: false,
            formData: {'file': null, 'url': null, 'resource_type': "act"}
        });
        this.onSelectType = this.onSelectType.bind(this);
        this.onChooseFile = this.onChooseFile.bind(this);
        this.onSetUrl = this.onSetUrl.bind(this);
        this.onSubmit = this.onSubmit.bind(this);
    }

    onSelectType(e) {
      const {file, url} = this.state.formData,
            formData = Object.assign(this.state.formData,
                                     {resource_type: e.target.value}),
            formValid = (file || url)? true: false;
      this.setState({formData: formData, formValid: formValid});
    }

    onSetUrl(e) {
      document.getElementById('file').value = null; // XXX do better
      const formData = Object.assign(this.state.formData,
                                     {url: e.target.value,
                                      file: null}),
            formValid = this.state.formData.resource_type? true: false;
      this.setState({formData: formData, formValid: formValid});
    }

    onChooseFile(e) {
        document.getElementById('url').value = null; // XXX do better
        this.clearNotif();
        const formData = Object.assign(this.state.formData,
                                       {file: e.target.files[0], url:null}),
              formValid = this.state.formData.resource_type? true: false;
        this.setState({formData: formData, formValid: formValid});
    }

    onSubmit(e) {
        e.preventDefault();
        if( !this.state.formValid) return;
        const {file, url, resource_type} = this.state.formData;
        let formData = new FormData();
        formData.append('file', file);
        formData.append('url', url);
        formData.append('resource_type', resource_type);
        api_fetch('/notice/import', 'POST', {body: formData})
            .then(response => {
                if(response.ok) {
                    response.json().then(json => {
                        if (json.log_msg === null || json.log_msg === undefined) {
                            // Redirecting to the edit form of the new resource
                            const editUri = ("/form/"
                                             + this.state.formData.resource_type
                                             + "/"
                                             + encodeURIComponent(json.uri));
                            this.context.router.push(editUri);
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
	    .catch(error => this.buildNotif("error",[{"title": "clientError",
                                                      "details": error.toString()}])
                  );
        this.buildNotif("info", [{"title": "processing",
                                  "details": ""}]);
    }

    helpIcon(field) {
        return (<a data-toggle='collapse' href={'#'+field+'-help'}
                title='help'>
                <span className='text-info glyphicon glyphicon-info-sign small'></span></a>);
    }

    helpText(field, text) {
        return (<div id={field+'-help'}
             className='help-block collapse' aria-expanded='false'>
             {text}
             </div>);
    }

    render() {
        const loc = this.props.localize;

        const formbutton = (<button type="submit"
                            className="btn btn-primary submit-vocabulary"
                            disabled={!this.state.formValid}>{loc("importNotice")}</button>);


        const formContent = (<form id="uploadForm" ref="uploadForm"
                                   className="form add-vocabulary"
                                   onSubmit={this.onSubmit}
                                   encType="multipart/form-data">
                               <section>
                               <div className="form-group">
                               <label className='control-label'
                               htmlFor="inputfile">{loc("importFromFile")}
                               {this.helpIcon('file')}</label>
                               {this.helpText('file',
                                              loc("importFromFileHelp"))}
                               <input id="file" name="inputfile" type="file"
                                      className="form-control-file" ref="file"
                                      accept=".rdf, .xml, .html"
                                      onChange={e => this.onChooseFile(e)} />
                               </div>
                               <div className="form-group">
                               <label className='control-label'
                               htmlFor="url">{loc("importFromUrl")}
                               {this.helpIcon('url')}</label>
                               {this.helpText('url', loc("importFromUrlHelp"))}
                               <input id="url" name="url" className="form-control"
                                      onChange={e => this.onSetUrl(e)}
                                      value={this.state.formData.url?this.state.formData.url:''} />
                               </div>
                               <div className="form-group">
                               <label className='control-label' htmlFor="resource_type">
                               <span className='glyphicon glyphicon-asterisk small mandatory'></span> 
                               {loc("resourceType")}</label>
                               <select className='form-control' name="resource_type"
                                       onChange={e => this.onSelectType(e)}
                                       value={this.state.formData.resource_type}>
                               <option value="act">{loc("act")}</option>
                               <option value="journal">{loc("journal")}</option>
                               <option value="consolidation">{loc("consolidation")}</option>
                               </select>
                               </div>
                               {formbutton}
                               </section>
                             </form>);

        return (<div className="container">
                <h1>{loc("importNoticeFrom")+" "+loc("rdfa")}</h1>
                {formContent}
                {this.renderNotif(loc)}
                </div>);
    }
}

NoticeRdfImport.contextTypes = {
    router: React.PropTypes.object.isRequired
};

export { Notice, NoticeRdfImport };
