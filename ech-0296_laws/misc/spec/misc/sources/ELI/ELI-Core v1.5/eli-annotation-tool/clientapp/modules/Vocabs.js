// -*- coding: utf-8 -*-
// Project sponsor is https://ec.europa.eu/isa2/
// License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

/* global FormData */

import React from 'react';
import ReactDOM from 'react-dom';

import NC from './NotifComponent';
import { api_fetch } from './API';


class Vocabs extends React.Component {
    constructor(props) {
	super(props);
	this.state = {
            data: null
        };
	this.loadDataFromServer = this.loadDataFromServer.bind(this);
        this.onDelete = this.onDelete.bind(this);
    }
    loadDataFromServer() {
        api_fetch('/vocabs', 'GET')
	    .then(response => response.json())
            .then(jsdata => this.setState({data: jsdata.data}));
    }
    onDelete(e) {
        e.preventDefault();
        //this.clearMessage(); // clear add message when delete item from list
        api_fetch('/vocabs/'+encodeURIComponent(e.target.dataset.name), 'DELETE')
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
                         (<p>{loc("noVocabulary")}</p>) :
                         (<table className="table table-condensed">
                          <tbody>
                          {this.state.data.map(
                               name => <tr key={name}><td>{name}</td>
                                   <td><a href={'/vocabs/'+encodeURIComponent(name)+'_html'}>{loc("previewHtml")}</a></td>
                                   <td><a href={'/vocabs/'+encodeURIComponent(name)+'.rdf'}>{loc("downloadRdf")}</a></td>
                                   <td><a href={'/vocabs/'+encodeURIComponent(name)+'.csv'}>{loc("downloadCsv")}</a></td>
                                               <td><a href={'/vocabs/'+encodeURIComponent(name)+'.zip'}>{loc("downloadZip")}</a></td>
                                  {((this.props.user.admin) ?
                                    (<td><button title={loc("deleteVocabulary")}
                                     data-name={name} onClick={this.onDelete}>
                                     <span className="glyphicon glyphicon-trash" data-name={name}></span>
                                     </button></td>) :
                                    null)}
                              </tr>)
                          }
                          </tbody>
                          </table>)
                        ));
        const addvocab = (this.props.user.admin
                          ? (<AddVocabulary {...this.props} reloadList={this.loadDataFromServer}/>)
                          : null);
        return (<div className="container">
                <h1>{loc("vocabularies")}</h1>
                <section>
                <h2>{loc("availableVocabularies")}</h2>
                {rows}
                </section>
                {addvocab}
                </div>
               );
    }
}

class AddVocabulary extends NC.NotifComponent {
    constructor(props) {
	super(props);
        Object.assign(this.state, {
            hasfile: false
        });
        this.onChooseFile = this.onChooseFile.bind(this);
        this.onSubmit = this.onSubmit.bind(this);
    }
    onChooseFile(e) {
        this.clearNotif();
        this.setState({hasfile: (e.target.files.length > 0)});
    }
    onSubmit(e) {
        e.preventDefault();
        if(!this.state.hasfile) return;

        const formData = new FormData();
        formData.append('file',document.getElementById('file').files[0]); // XXX do better

        api_fetch('/vocabs', 'POST', {body: formData})
            .then(response => {
                if(response.ok) {
                    response.json().then(json => {
                        if (json.log_msg === null || json.log_msg === undefined) {
                            this.buildNotif("success", [{"title": "success",
                                                         "details": ""}]);
                        } else {
                            this.buildNotif("warning", json.log_msg);
                        }
                    	this.props.reloadList();
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

    render() {
        const loc = this.props.localize;

        const formbutton = (<button type="submit"
                            className="btn btn-primary submit-vocabulary"
                            disabled={!this.state.hasfile}>{loc("importVocabulary")}</button>);

        return (<section>
                <h2>{loc("addVocabulary")}</h2>
                <div className="alert alert-info"><span className="text-info glyphicon glyphicon-info-sign small"></span> {loc("addVocabularyHelp")} <a href={"/resource/excel_vocab_doc/"+this.props.lang} className="alert-link"><span className="text-info glyphicon glyphicon-book"></span></a></div>
                <form id="uploadForm" ref="uploadForm" className="form-inline add-vocabulary" onSubmit={this.onSubmit} encType="multipart/form-data">

                <div className="form-group">
                <input id="file" name="inputfile" type="file"
                className="form-control-file"
                ref="file"
                accept=".xls,.xlsx,.xml,.ttl,.csv,.html,.rdf"
                onChange={e => this.onChooseFile(e)} />
                </div>
                {formbutton}
                </form>
                {this.renderNotif(loc)}
                </section>);
    }
}

export { Vocabs };
