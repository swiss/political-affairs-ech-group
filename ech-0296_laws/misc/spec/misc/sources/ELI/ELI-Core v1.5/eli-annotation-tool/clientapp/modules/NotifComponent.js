// -*- coding: utf-8 -*-
// Project sponsor is https://ec.europa.eu/isa2/
// License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

/* global FormData */

import React from 'react';
import ReactDOM from 'react-dom';

class NotifComponent extends React.Component {
    constructor(props) {
	super(props);
	this.state = {
            notification: null
        };
        this.buildNotif = this.buildNotif.bind(this);
        this.clearNotif = this.clearNotif.bind(this);
        this.clearNotifMessage = this.clearNotifMessage.bind(this);
        this.renderNotif = this.renderNotif.bind(this);
    }
    buildNotif(notif_type, messages) {
        messages.forEach(
            (msg, idx) => msg.key= "notif-msg-" + idx
        );
        this.setState({
            notification: {"type": notif_type,
                           "messages": messages}
            });
    }
    clearNotif() {
        this.setState({
            notification: null
        });
    }
    clearNotifMessage(msg_key) {
        if (this.state.notification !== null) {
            const old_notif = this.state.notification;
            const idx = old_notif.messages.findIndex(x => x.key == msg_key);
            old_notif.messages.splice(idx,1);
            this.setState({
                notification: {"type": old_notif.type,
                               "messages": old_notif.messages}
            });
        }
    }
    renderNotif(localize_function) {
        if (this.state.notification === null) {
            return "";
        }
        const notifClass = {error: 'alert-danger', warning: 'alert-warning',
                            success: 'alert-success', info: 'alert-info'};
        return this.state.notification.messages.map(
            msg => (<div className={"alert alert-dismissible "
                                    + notifClass[this.state.notification.type]}
                    key={msg.key}>
                      <button type="button" className="close"
                      onClick={e => this.clearNotifMessage(msg.key)}>
                      <span aria-hidden="true">&times;</span>
                      </button>
                      <div>
                        <p><b>{localize_function(msg.title)+" "}
                        {(msg.title_suffix !== undefined && msg.title_suffix !== null && msg.title_suffix !== "") ? (<mark>{msg.title_suffix}</mark>) : ""}</b></p>
                        {msg.details.split("\n").map((line,idx) => <p key={msg.key+"."+idx}>{line}</p>)}
                      </div>
                    </div>)
        );
    }
}

export default { NotifComponent };
