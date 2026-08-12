// -*- coding: utf-8 -*-
// Project sponsor is https://ec.europa.eu/isa2/
// License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

//@flow

import React from 'react';
import { api_fetch } from './API';
//import * as jsonld from 'jsonld';
import jQuery from 'jquery';
import moment from 'moment';

import Select from 'react-select';
import VirtualizedSelect from 'react-virtualized-select';
import DebounceInput from 'react-debounce-input';
import Datetime from 'react-datetime';

let idCounter = 0;
const getUniqueId = function getUniqueId() {
    idCounter++;
    return "eliv_uid-" + idCounter;
};

const URISCHEME_KEYS = ["elix:abstractLegalResourceUriScheme",
                        "elix:legalResourceUriScheme",
                        "elix:legalExpressionUriScheme",
                        "elix:formatUriScheme"];

const compute_uri_vars = (values) => {
    const uri_vars = new Set();
    URISCHEME_KEYS.forEach(key =>
                           extract_uri_vars(traverse_values(values, [key]).value)
                           .forEach(v => uri_vars.add(v.name)));
    return uri_vars;
};

const jumpAndShow = (elementId) => {
    const target = document.getElementById('field/'+elementId);
    const jQtarget = jQuery(target);
    jQtarget.parents(".tab-pane").each((idx,pane) => {
        jQuery(pane)
            .parents(":has(ul.nav)")
            .find("ul.nav a[href='#"+pane.id+"']")
            .tab("show");
    });
    jQtarget.parents(".collapse").collapse("show");
    window.setTimeout(() => target.scrollIntoView(), 300);
};

const getInvalidValues = (values) => {
    const vals = enumerate_values_paths(values);
    return vals.filter(path => bool(traverse_values(values, path).valid === false));
};

const get_url_validity = (value) => {
    if (value.url_valids === undefined) {
        return true;
    }
    return Object.values(value.url_valids).map(va => va.valid !== false).reduce((a,b) => a && b, true);
};

const getInvalidURLs = (values) => {
    const vals = enumerate_values_paths(values);
    return vals.filter(path => ! get_url_validity(traverse_values(values, path) || {}));
};

const extract_uri_vars = (value) => {
    const r = /\{([:|@\w]*)\}/gi;
    const vars = [];
    let item = null;
    while (true) {
        item = r.exec(value);
        if(item === null) break;
        const group = item[1].toLowerCase();
        const v = {};
        if(group.includes('|')) {
            [v.name, v.filter] = group.split('|');
        } else {
            [v.name, v.filter] = [group, null];
        }
        vars.push(v);
    };
    return vars;
};

const get_uri_eligible_keys = (schema) => {
    if (schema.eligible_uri_properties !== undefined) {
        return schema.eligible_uri_properties;
    }
    const keys = [];
    for(let path of enumerate_schema_paths(schema)) {
        keys.push(path[path.length-1]);
    }
    keys.push('eli:language','eli:format');
    return keys;
};

const eliUriSchemeValidator = (val, state) => {
    const uri_vars = extract_uri_vars(val);
    const eligible_keys = get_uri_eligible_keys(state.schema);
    const invalid_vars = uri_vars
              .map(v => v.name)
              .filter(v => eligible_keys.indexOf(v) === -1);
    return invalid_vars;
};

const eliUriSchemeDistinct = (val, state) => {
    const identical_values = URISCHEME_KEYS
          .map(key => traverse_values(state.values, [key]).value)
          .filter(value => (value[0] === val));
    return bool(identical_values.length <= 1);
};

const VALIDATORS = {
    eliUriScheme: (x, state, loc_function) => {
        const r = {valid: true, msg: ''};
        if (x === null || x === undefined) {
            r.valid = false;
            r.msg = loc_function("mandatoryURISchemes");
            return r;
        }
        const v = x[0];
        if (v === '' || v === undefined) {
            r.valid = false;
            r.msg = loc_function("mandatoryURISchemes");
            return r;
        }
        const invalid_vars = eliUriSchemeValidator(v, state);
        if(invalid_vars.length !== 0) {
            r.valid = false;
            r.msg = loc_function("invalidURIVariables") + invalid_vars.join(', ');
        } else if(!eliUriSchemeDistinct(v, state)) {
            r.valid = false;
            r.msg = loc_function("distinctURISchemes");
        }
        return r;
    },
    eliDate: (x, state, loc_function) => {
        const r = {valid: true, msg: ''};
        if (x !== null && x !== undefined) {
            const v = x[0];
            if (v && !moment(v, 'YYYY-MM-DD', true).isValid()) {
                r.valid = false;
                r.msg = loc_function("invalidDateFormat");
            }
        }
        return r;
    },
    notempty: (x, state, loc_function) => {
        const r = {valid: true, msg: ''};
        if (x === null || x === undefined) {
            r.valid = false;
            r.msg = loc_function("mandatoryValue");
        } else {
            r.valid = bool(x.length > 0 && x.map(v => v !== null && v !== "").reduce((a,b) => (a || b), false));
            r.msg = (r.valid ? '' : loc_function("mandatoryValue"));
        }
        return r;
    }
};


const full_title = (path, state, lang, loc_function) => {
    if (path.length === 1) {
        // ELI field
        const field_name = ((path[0].startsWith("elix:")) ?
                             loc_function(path[0], "eliOntologyExtension") :
                             loc_function(path[0], "eliOntology"));
        return field_name;
    }
    if (path.length === 2) {
        // lang + ELI field
        const lang_node = traverse_schema(state.schema, path.slice(0,1), true);
        const lang_uri = ((lang_node || {}).title || path[0]);
        const lang_vocab = state.vocabs[state.lang_vocab_name];
        const langLabels = labelsFromVocab((lang_vocab || []), lang);
        const lang_name = ((langLabels[lang_uri] !== undefined) ? langLabels[lang_uri] : lang_uri);
        const field_name = ((path[1].startsWith("elix:")) ?
                             loc_function(path[1], "eliOntologyExtension") :
                             loc_function(path[1], "eliOntology"));
        return lang_name + " / " + field_name;
    }
    if (path.length === 3) {
        // lang + format + ELI field
        const lang_node = traverse_schema(state.schema, path.slice(0,1));
        const lang_uri = ((lang_node || {}).title || path[0]);
        const lang_vocab = state.vocabs[state.lang_vocab_name];
        const langLabels = labelsFromVocab((lang_vocab || []), lang);
        const lang_name = ((langLabels[lang_uri] !== undefined) ? langLabels[lang_uri] : lang_uri);
        const format_node = traverse_schema(state.schema, path.slice(0,2));
        const format_uri = ((format_node || {}).title || path[1]);
        const format_vocab = state.vocabs[state.format_vocab_name];
        const formatLabels = labelsFromVocab((format_vocab || []), lang);
        const format_name = ((formatLabels[format_uri] !== undefined) ? formatLabels[format_uri] : format_uri);
        const field_name = ((path[2].startsWith("elix:")) ?
                             loc_function(path[2], "eliOntologyExtension") :
                             loc_function(path[2], "eliOntology"));
        return lang_name + " / " + format_name + " / " + field_name;
    }
    return path.join(" / ");
};


const bool = (x) => x ? true : false;

const enumerate_schema_paths = (schema, path=[]) => {
    const paths = [];
    if (schema.properties === undefined) {
        paths.push(path);
    } else {
        for(let key of Object.keys(schema.properties)) {
            paths.push(...enumerate_schema_paths(schema.properties[key], [...path, key]));
        }
    }
    return paths;
};

const traverse_schema = (schema, path) => {
    if(path.length === 0)
        return schema;
    else if(path.length === 1)
        return schema.properties[path[0]];
    else
        return traverse_schema(schema.properties[path[0]], path.slice(1));
};

const validate_value = (schema, path, value, state, loc_function) => {
    const schema_node = traverse_schema(schema, path);
    if (schema_node === undefined) {
        return ;
    }
    const keys = (schema_node.validators === undefined
                  ? [] : schema_node.validators);
    if (state.edit_mode !== true) {
        if (schema_node.vocab === null && (schema_node.enabled || state.uri_vars.has(path2Id0(path)))) {
            return {valid: false, msg: loc_function("missingFieldVocabulary")};
        }
        if (schema_node.mandatory
            || (state && state.uri_vars.has(path2Id0(path)))) {
            if (keys.indexOf("notempty") == -1) {
                keys.push('notempty');
            }
        }
    } else {
        if (path.length > 0 &&
            (path[0] === "elix:languages_list" || path[0] === "elix:formats_list")) {
            if (schema_node.vocab === null ||
                state.available_vocabs === undefined ||
                ! state.available_vocabs.includes(schema_node.vocab)) {
                return {valid: false, msg: loc_function("missingFieldVocabulary")};
            }
            if (keys.indexOf("notempty") == -1) {
                keys.push('notempty');
            }
        }
    }
    for(let key of keys) {
        const validator = VALIDATORS[key];
        if(validator === undefined) {
            return {valid: false, msg: loc_function("unknownValidator") + key};
        }
        const r = validator(value, state, loc_function);
        if(!r.valid) {
            return r;
        }
    }
    return {valid: true, msg: null};
};

const validate_values = (schema, values, state, loc_function) => {
    enumerate_values_paths(values)
        .forEach(path => {
            const val = traverse_values(values, path);
            const validation = validate_value(schema, path, val.value, state, loc_function);
            val.valid = validation.valid;
            val.msg = validation.msg;
        });
};

const reset_value = (schema, values, path, state, loc_function) => {
    const value = traverse_values(values, path);
    if (value) {
        value.value = [];
        const validation = validate_value(schema, path, value.value, state, loc_function);
        value.valid = validation.valid;
        value.msg = validation.msg;
    }
};

const enumerate_values_paths = (values, path=[]) => {
    const items = [];
    for(let key of Object.keys(values)) {
        const itempath = [...path, key];
        if (values[key] !== undefined) {
            if(values[key].value !== undefined) {
                items.push(itempath);
            } else {
                items.push(...enumerate_values_paths(values[key], itempath));
            }
       }
    }
    return items;
};

const traverse_values = (values, path) => {
    if(path.length === 1) {
        return values[path[0]];
    } else {
        return traverse_values(values[path[0]], path.slice(1));
    }
};

const init_values = (schema_node, oldvalues) => {
    if (schema_node.properties === undefined) {
        const val = (oldvalues ? oldvalues.value : []);
        return {value: val};
    } else {
        let values = {};
        for(let key of Object.keys(schema_node.properties)) {
            values[key] = init_values(schema_node.properties[key],
                                      oldvalues ? oldvalues[key] : undefined);
            if(key.startsWith('lang_')) {
                values[key]['eli:language'].value = [schema_node.properties[key].title];
            }
            if(key.startsWith('format_')) {
                values[key]['eli:format'].value = [schema_node.properties[key].title];
            }
        }
        return values;
    }
};

const props4child = (child, props, path) => {
    const r = Object.assign({}, props);
    r.uiDef = child;
    r.key = 'key_'+child.id;
    if(path !== undefined) r.path = path;
    return r;
};

const mkthispath = (path, id) => {
    const p = path.slice();
    p.push(id);
    return p;
};

const path2Id = (path) => path.join('--').replace(':','_');
const path2Id0 = (path) => path.join('--');

const copy_object = (x) => Object.assign({},x);

const renderChildren = (children, props, path) =>
          children
          .map(child => React.createElement(implementers[child.type],
                                            props4child(child, props, path)))
      .filter(element => is_displayed(element.props));


const is_displayed = (props) => {
    if (props.state.edit_mode) return true;
    // Subsections or tabs implementing child for each format or lang
    if (props.uiDef.type == "subSections" || props.uiDef.type == "tabs" ) {
        const child_props = collectChildren(props);
        child_props.forEach(child => child.state = props.state);
        return child_props.map(child => is_displayed(child)).reduce(((a,b) => a || b), false);
    }
    // Section, tab or subsection containing direct children
    if (props.uiDef.type == "section" || props.uiDef.type == "zone" || props.uiDef.type == "subSection" || props.uiDef.type == "tab" ) {
        const child_props = []
        props.uiDef.content.forEach(uiChild => {
            const childProp = copy_object(props);
            childProp.path = props.path.slice(0);
            childProp.uiDef = uiChild;
            child_props.push(childProp);
        });
        return child_props.map(child => is_displayed(child)).reduce(((a,b) => a || b), false);
    }

    const thispath = mkthispath(props.path, props.uiDef.id);
    const schema_node = traverse_schema(props.state.schema, thispath);

    return bool(schema_node && schema_node.enabled);
};

const compute_decorator_features = (props) => {
    const features = {};
    features.thispath = mkthispath(props.path, props.uiDef.id);
    features.thisId = path2Id(features.thispath);

    features.parent_schema_node = traverse_schema(props.state.schema, props.path);
    features.schema_node = traverse_schema(props.state.schema, features.thispath);

    features.is_urivar = props.state.uri_vars.has(path2Id0(features.thispath));
    features.is_enabled = bool(features.schema_node && features.schema_node.enabled);
    features.is_displayed = bool(props.state.edit_mode || features.is_enabled);
    features.is_collapsed = bool(props.state.edit_mode && !features.is_enabled);
    features.is_mandatory = bool(features.schema_node.mandatory || features.is_urivar);

    features.value = traverse_values(props.state.values, features.thispath);
    features.value_valid = bool(features.value && features.value.valid);
    features.value_error_msg = (features.value && features.value.msg);
    features.value_is_uri = ((features.schema_node.items
                              && features.schema_node.items.format === 'uri')
                             || (features.schema_node.format === "uri"));

    if (props.uiDef.l10n_term !== undefined) {
        features.label = props.localize(props.uiDef.l10n_term, props.uiDef.l10n_domain);
        features.help = props.localize(props.uiDef.l10n_term, props.uiDef.l10n_domain, "help");
    } else {
        features.label = props.localize(props.uiDef.id, props.uiDef.l10n_domain);
        features.help = props.localize(props.uiDef.id, props.uiDef.l10n_domain, "help");
    }

    if (props.state.schema.eligible_uri_properties !== undefined &&
        URISCHEME_KEYS.includes(props.uiDef.id)) {
        features.eligibleFieldsList = props.state.schema.eligible_uri_properties;
    }

    if (props.uiDef.l10n_domain === "eliOntology") {
        features.eliField = ((props.uiDef.l10n_term !== undefined) ? props.uiDef.l10n_term : props.uiDef.id);
    }

    features.badges = props.badges || [];
    features.title_parts = features.badges.map(badge => badge.title);
    features.title_parts.push(features.label);

    features.mandatory_enabled = bool(props.state.edit_mode && features.is_enabled && !features.is_urivar);

    features.vocab_enabled = (props.state.edit_mode
                              && !features.is_collapsed
                              && (props.uiDef.type === 'selectField'));
    features.vocab_options = ((features.vocab_enabled && (props.state.available_vocabs !== null))
                              ? props.state.available_vocabs.map(item => ({value: item, label: item}))
                              : []);
    features.activation_enabled = bool(props.state.edit_mode && !features.is_urivar);
    features.activation_status = features.is_mandatory || features.is_enabled;

    features.config_valid = bool(features.value && ! bool(features.value.config_invalid));
    features.config_error_msg = (features.value && features.value.config_msg);

    features.input_enabled = true;
    if(props.state.edit_mode && (props.uiDef.type === 'dateField')) features.input_enabled = false;
    if(features.vocab_enabled && props.state.available_vocabs === null) features.input_enabled = false;

    features.multiple = bool(features.schema_node.type === "array");

    return features;
};

const FormFieldDecorator = (WrappedComponent) => {
    class _DecoratedField extends React.Component {
        constructor(props) {
            super(props);
        }
        render() {
            const loc = this.props.localize;
            const F = compute_decorator_features(this.props);

            // ***** do not display => done
            if(!F.is_displayed) return null;

            const wrappedprops = copy_object(this.props);
            wrappedprops.features = copy_object(F);

            const field = (F.is_collapsed
                           ? ''
                           : (<div className='meta-input-group'>
                              {React.createElement(WrappedComponent, wrappedprops)}
                              {(!F.value_valid
                                ? (<p className={(this.props.state.edit_mode ? "text-danger" : "")}>{F.value_error_msg}</p>)
                                : "")}
                              </div>)
                          );
            const badges = F.badges.map(badge => (
                    <span key={badge.label} className='label' title={badge.title}>{badge.label}</span>));
            const helpIcon = ((F.help !== undefined || F.eliField !== undefined)
                             ? (<a data-toggle='collapse' href={'#'+F.thisId+'-help'}
                                   title={loc("showHelp")}>
                                <span className='text-info glyphicon glyphicon-info-sign small'></span></a>)
                              : "");
            const helpBlk = ((F.help !== undefined || F.eliField !== undefined)
                             ? (<div id={F.thisId+'-help'} className='help-block collapse'
                                     aria-expanded='false'>
                                {((F.help !== undefined) ? (<p>{F.help}</p>) : "")}
                                {((F.eligibleFieldsList !== undefined) ? (<p>{loc("eligibleUriFields")} {F.eligibleFieldsList.join(", ")}</p>) : "")}
                                {((F.eliField !== undefined) ? (<p>{loc("eliField")} {F.eliField}</p>) : "")}
                                </div>)
                             : "");
            const mandatory_symbol = (F.is_mandatory
                                      ? (<span className={'glyphicon glyphicon-asterisk small'+(F.is_mandatory ? ' mandatory' : '')}
                                               title={loc("mandatoryLabel")}></span>)
                                      : '');
            if (!this.props.state.edit_mode) {
                // Not in config mode, we're done!
                return (<div id={'field/'+F.thisId} className={'form-group'+(F.value_valid ? '' : ' has-error')}>
                          <label className='control-label'>{mandatory_symbol} {F.label} {badges} {helpIcon}</label>
                          {helpBlk}
                          {field}
                        </div>);
            }

            // In config mode:

            const activate_field = (event) => {
                event.preventDefault();
                this.props.dispatch({type: 'TOGGLE_ENABLE',
                                     path: F.thispath,
                                     value: !F.activation_status});
            };
            const activ_class = ("activation-button"
                                 + (F.activation_enabled ? " clickable" : " disabled")
                                 + (F.activation_status
                                    ? ( (F.config_valid && F.value_valid)
                                        ? " activated"
                                        : " activated-error")
                                    : " deactivated"));
            const activ_title = (!F.activation_enabled
                                 ? loc("alwaysActivated")
                                 : (F.activation_status
                                    ? loc("clickForDeactivated")
                                    : loc("clickForActivated"))
                                );
            const activation = (<span className={activ_class}
                                id={'activation/'+F.thisId}
                                title={activ_title}
                                onClick={F.activation_enabled ? activate_field : null} >{
                                    (F.activation_status
                                     ? (<span className="glyphicon glyphicon-ok" />)
                                     : (<span className="glyphicon glyphicon-remove" />))
                                }</span>);

            const mandatorize_field = (event) => {
                event.preventDefault();
                this.props.dispatch({type: 'TOGGLE_MANDATORY',
                                     path: F.thispath,
                                     value: !F.is_mandatory
                                    });
            };
            const mand_text = ((!F.mandatory_enabled || F.is_mandatory)
                               ? loc("mandatoryLabel")
                               : loc("optionalLabel")
                              );
            const mand_title = (!F.mandatory_enabled
                                ? loc("alwaysMandatory")
                                 : (F.is_mandatory
                                    ? loc("clickForOptional")
                                    : loc("clickForMandatory"))
                               );
            const mandatory = (<div className="configuration"><button id={"mandatory/"+F.thisId}
                               className={"btn btn-xs btn-default"+(F.is_mandatory ? " active" : "")}
                               title={mand_title} onClickCapture={mandatorize_field}
                               disabled={!F.mandatory_enabled}
                               ><span className={'glyphicon glyphicon-asterisk small'+(F.is_mandatory ? ' mandatory' : '')}></span></button
                               > {mand_text}</div>);

            const set_field_vocab = (newValue) => {
                this.props.dispatch({type: 'SET_VOCAB',
                                     path: F.thispath,
                                     value: newValue.value
                                    });
            };
            const vocab = (F.vocab_enabled
                           ? (<div className="configuration">
                              <span>{loc("configuredVocab")}</span>
                              <VirtualizedSelect name={'vocab/'+F.thisId} options={F.vocab_options}
                              placeholder={loc("selectVocabulary")}
                              onChange={set_field_vocab}
                              value={F.schema_node.vocab}
                              clearable={false} />
                              </div>)
                           : '');

            const configuration = (F.activation_status
                                   ? (<div className={'col-xs-6'+ (F.config_valid ? '' : ' has-error')}>
                                        {mandatory}
                                        {vocab}
                                        {(F.config_error_msg ? (<p className="text-danger">{F.config_error_msg}</p>) : "")}
                                      </div>)
                                   : "");

            const default_value = (F.activation_status
                                   ? (<div className={'col-xs-6'+ (F.value_valid ? '' : ' has-error')}>
                                        <div id={'default/'+F.thisId} className="default-value">
                                          <span>{loc("defaultValues")}</span>
                                          {field}
                                        </div>
                                      </div>)
                                   : '');

            return (<div id={'field/'+F.thisId} className='row form-group'>
                    <div className="col-xs-12">
                      <div className={F.activation_status ?  '' : ' deactivated'}>
                        <div className="activation">{activation} <label className='control-label'>{F.label} {badges} {helpIcon}</label></div>
                          {helpBlk}
                        </div>
                      </div>
                      {configuration}
                      {default_value}
                    </div>);
        }
    }
    _DecoratedField.displayName = 'Decorated'+(WrappedComponent.displayName || WrappedComponent.name);
    return _DecoratedField;
};

const FormSection = (props) => {
    const {uiDef, state} = props;
    const loc = props.localize;
    const rend_children = renderChildren(uiDef.content, props);
    if (props.children !== undefined) {
        props.children.forEach(child => rend_children.push(child));
    }
    if (rend_children.length === 0) return null;
    return (<section>
            <h2 id={uiDef.id} className='clickable' data-toggle='collapse'
            data-target={'#'+uiDef.id+'-content'} title={loc("collapseSection")}>
            <span>{loc(uiDef.id)}</span>
            <span className='pull-right collapse-arrow'>
            <span className='glyphicon glyphicon-chevron-down'></span>
            </span>
            </h2>
            <div id={uiDef.id+'-content'} className='collapse in' aria-expanded='true'>
            {rend_children}
            </div>
            </section>);
};

const FormZone = (props) => {
    const {uiDef, state} = props;
    const rend_children = renderChildren(uiDef.content, props);
    if (rend_children.length === 0) return null;
    return (<div className='zone'>
            {rend_children}
            </div>);
};

const collectChildren = (props) => {
    const schemaParent = traverse_schema(props.state.schema, props.path);
    const childrenSchemaKeys = Object.keys(schemaParent.properties)
          .filter(key => key.startsWith(props.uiDef.idPrefix));
    const childUiDef = props.state.ui_description.definitions[props.uiDef.uiElement];
    const listSchema = ((props.uiDef.idPrefix === "lang_")
                        ? props.state.schema.properties["elix:languages_list"]
                        : ((props.uiDef.idPrefix === "format_")
                           ? props.state.schema.properties["elix:formats_list"]
                           : undefined));
    const vocabUri = ((listSchema !== undefined) ? listSchema.vocab : undefined);
    const uriLabels = labelsFromVocab((props.state.vocabs[vocabUri] || []), props.lang);
    const uriNotations = notationsFromVocab((props.state.vocabs[vocabUri] || []));
    const children = [];
    childrenSchemaKeys.forEach((childSchemaKey,idx) => {
        const childData = {uiDef: childUiDef};
        childData.schema = schemaParent.properties[childSchemaKey];
        childData.uri = childData.schema.title;
        childData.path = mkthispath(props.path, childSchemaKey);
        childData.title = ((uriLabels[childData.uri] !== undefined)
                           ? uriLabels[childData.uri]
                           : childData.uri);
        childData.badges = (props.badges ? props.badges.slice() : []);
        const badgeID = ((uriNotations[childData.uri] !== undefined)
                         ? uriNotations[childData.uri].toUpperCase()
                         : getLast(getLast(childData.path).split('_')).toUpperCase());
        childData.badges.push({title: childData.title, label: badgeID});
        if (childData.uiDef.miniaturesLib !== undefined) {
            const miniLib = props.state.miniatures[childData.uiDef.miniaturesLib];
            childData.miniature = ((miniLib !== undefined) ? miniLib[childData.uri] : undefined);
        }
        children.push(childData);
    });
    return children;
};

const getLast = (seq) => seq[seq.length-1];

const FormSubSections = (props) => {
    const renderSection = (child) => {
        const section_id = path2Id(child.path);
        const prp = copy_object(props);
        prp.path = child.path;
        prp.uiDef = child.uiDef;
        prp.badges = child.badges;
        const mini = ((child.miniature !== undefined)
                      ? (<img className='miniature' src={child.miniature} />)
                      : '');
        const rend_grandchildren = renderChildren(child.uiDef.content, prp);
        if (rend_grandchildren.length === 0) return null;
        return (<div key={section_id}>
                <h2 id={section_id} className='clickable' data-toggle='collapse'
                data-target={'#'+section_id+'-content'}
                title={props.localize("collapseSection")}>
                {mini}
                <span>{child.title}</span>
                <span className='pull-right collapse-arrow'>
                <span className='glyphicon glyphicon-chevron-down'></span>
                </span>
                </h2>
                <div id={section_id+'-content'} className='collapse in sub-section-indent' aria-expanded='true'>
                {rend_grandchildren}
                </div>
                </div>);
    };
    const subsections = collectChildren(props)
          .map(child => renderSection(child));
    if (subsections.length === 0) return null;
    return <div>{subsections}</div>;
};

const FormTabs = (props) => {
    const menuitems = [];
    const children = [];
    collectChildren(props).forEach((child,idx) => {
        const tabId = path2Id(child.path);
        const klass = (idx === 0 ? 'active' : '');
        const mini = ((child.miniature !== undefined)
                      ? (<img className='miniature' src={child.miniature} />)
                      : '');
        const prp = copy_object(props);
        prp.path = child.path;
        prp.uiDef = child.uiDef;
        prp.badges = child.badges;
        const rend_grandchildren = renderChildren(child.uiDef.content, prp);
        if (rend_grandchildren.length > 0) {
            menuitems.push(<li key={'li-'+tabId+'content'} role='presentation'
                           className={klass}>
                           <a id={tabId} href={'#'+tabId+'-content'}
                           aria-controls={tabId+'-content'}
                           role='tab'
                           data-toggle='tab'>
                           {mini}
                           <span>{child.title}</span>
                           </a>
                           </li>);
            children.push(<div key={tabId+'content'} id={tabId+'-content'}
                          role='tabpanel'
                          className={'tab-pane '+klass}>
                          {rend_grandchildren}
                          </div>);
        }
    });
    if (children.length === 0) return null;
    return (<div>
            <ul className='nav nav-tabs' role='tablist'>{menuitems}</ul>
            <div className='tab-content'>{children}</div>
            </div>);
};

const FormFieldText = (props) => {
    const {uiDef, state, dispatch} = props;

    const check_url = (value) => {
        if (value === "") {
            props.dispatch(
                {type: 'SET_URL_VALIDITY',
                 path: props.features.thispath,
                 value: value,
                 valid: true,
                 msg: ""
                });
        } else {
            props.dispatch(
                {type: 'SET_URL_VALIDITY',
                 path: props.features.thispath,
                 value: value,
                 valid: false,
                 msg: props.localize("checkingURL")
                });
            api_fetch('/check_url?q='+encodeURIComponent(value), 'GET')
                .then(response => response.json())
                .then(json => props.dispatch(
                    {type: 'SET_URL_VALIDITY',
                     path: props.features.thispath,
                     value: value,
                     valid: bool(json.http_code < 400),
                     msg: (json.http_code < 400
                           ? props.localize("correctURL")
                           : ((json.http_code >= 500)
                              ? props.localize("urlCheckerError")
                              : props.localize("wrongURL")
                             )
                          )
                    }));
        }
    };

    const onblur = (props.features.value_is_uri
                    ? check_url
                    : (value) => null);
    const placeholder = (props.state.edit_mode ? props.localize("noDefaultValue") : "");
    const vals = ((props.features.value && props.features.value.value) ?
                  (props.features.value.value.slice() || []) :
                  []);
    if (vals.length === 0
        || (props.features.multiple && vals[vals.length-1] !== "")) {
        vals.push("");
    }
    const update_state = (value, idx) => {
        const new_vals = vals.slice();
        if (idx >= 0 && idx < new_vals.length) {
            new_vals[idx] = value;
        }
        props.dispatch({type: 'SET_VALUE',
                        path: props.features.thispath,
                        value: new_vals.filter(v => (v !== "" && v !== null))
                       });
    };
    const fields = vals.map((value, idx) => (
            <div className="single-field"
                 key={"field/"+props.features.thisId+"-"+idx}>
            <DebounceInput debounceTimeout={500}
            type='text' className='form-control'
            placeholder={placeholder}
            value={value}
            disabled={!props.features.input_enabled}
        onBlur={(e) => onblur(e.target.value)}
            onChange={(e) => update_state(e.target.value, idx)} />
            {((props.features.value.url_valids) ? (
                (props.features.value.url_valids[value] && props.features.value.url_valids[value].msg !== "") ?
                    (<p className='check-result-block'>{props.features.value.url_valids[value].msg}</p>) :
                null) :
              null)}
            </div>
    ));
    return (<div>{fields}</div>);
};
const DecoratedFormFieldText = FormFieldDecorator(FormFieldText);

const FormFieldDate = (props) => {
    const ini_val = ((props.features.value && props.features.value.value) ?
                     (props.features.value.value[0] || "") :
                     "");
    return (<Datetime
            value={ini_val}
            dateFormat='YYYY-MM-DD'
            timeFormat={false}
            closeOnSelect={true}
            onChange={(e) => props.dispatch({type: 'SET_VALUE',
                                             path: props.features.thispath,
                                             value:  ((typeof e === 'object') ? [e.format('YYYY-MM-DD')] : [e]),
                                            })}/>);
};
const DecoratedFormFieldDate = FormFieldDecorator(FormFieldDate);

/* SKOS Vocabs for selects *************************************************** */

const SKOS = 'http://www.w3.org/2004/02/skos/core#';
const SKOS_Concept = SKOS+'Concept';
const SKOS_notation = SKOS+'notation';
const SKOS_prefLabel = SKOS+'prefLabel';
const SKOS_inScheme = SKOS+'inScheme';

const prefLabelLang = (node, lang) => {
    try {
        for(let label of node[SKOS_prefLabel]) {
            if(lang === label['@language'])
                return label['@value'];
        }
        return node[SKOS_prefLabel][0]['@value'];
    } catch (e) {
        return node["@id"];
    }
};

const getNotation = (node) => {
    try {
        return node[SKOS_notation][0]['@value'];
    } catch (e) {
        return "";
    }
};

const getConcepts = (nodes) => nodes.filter(node => (node['@type'] !== undefined && node['@type'][0] === SKOS_Concept));

const strcompare = (a,b) => {if(a < b) return -1; else if (a > b) return 1; else return 0;};

const labelsFromVocab = (vocab, lang) => {
    const labels = {};
    if (vocab) {
        getConcepts(vocab).forEach((node, idx) => {
            labels[node["@id"]] = prefLabelLang(node, lang);
        });
    }
    return labels;
}

const notationsFromVocab = (vocab) => {
    const nots = {};
    if (vocab) {
        getConcepts(vocab).forEach((node, idx) => {
            nots[node["@id"]] = getNotation(node);
        });
    }
    return nots;
}

const missingVocabNotations = (vocab) => {
    const nots = notationsFromVocab(vocab);
    const missings = Object.entries(nots).filter(entry => entry[1] === "").map(entry => entry[0]);
    return missings;
}

const optionsFromVocab = (vocab, lang) =>
          getConcepts(vocab)
          .sort((a,b) => strcompare(prefLabelLang(a,lang), prefLabelLang(b,lang)))
          .map(node => ({value: node['@id'],
                         notation: getNotation(node),
                         label: (getNotation(node) !== "")
                           ? prefLabelLang(node,lang) + " - " + getNotation(node)
                           : prefLabelLang(node,lang)
                        }));

const FormFieldSelect = (props) => {
    const vocab = props.state.vocabs[props.features.schema_node.vocab];
    let options = [];
    let isLoading = true;
    let placeholder = '';
    let disabled = undefined;
    if (vocab === undefined) {
        placeholder = props.localize("noDefinedVocabulary");
        disabled = true;
    } else {
        isLoading = false;
        options = optionsFromVocab(vocab, props.lang);
        placeholder = (props.state.edit_mode
                       ? props.localize("noDefaultValue")
                       : '');
        disabled = false;
    }
    const onChange = (option) => {
        const sel_vals = ((option === undefined || option === null || (Array.isArray(option) && option.length === 0)) ?
                          [] :
                          ((props.features.multiple) ?
                           option.map(opt => opt.value) :
                           [option.value]));
        props.dispatch({type:'SET_VALUE',
                        path: props.features.thispath,
                        value: sel_vals});
    };
    const ini_vals = ((props.features.multiple === true) ?
                      ((props.features.value && props.features.value.value) ? props.features.value.value : []):
                      ((props.features.value && props.features.value.value) ? (props.features.value.value[0] || null) : null));
    return React.createElement(VirtualizedSelect,
                               {options: options,
                                onChange: onChange,
                                value: ini_vals,
                                placeholder: placeholder,
                                isLoading: false,
                                disabled: disabled,
                                multi: props.features.multiple,
                                simpleValue: false,
                                selectComponent: props.selectComponent || Select,
                                localize: props.localize,
                                lang: props.lang
                               });
};
const DecoratedFormFieldSelect = FormFieldDecorator(FormFieldSelect);

const implementers = {
    section: FormSection,
    zone: FormZone,
    subSections: FormSubSections,
    tabs: FormTabs,
    dateField: DecoratedFormFieldDate,
    textField: DecoratedFormFieldText,
    selectField: DecoratedFormFieldSelect
};


const EditableURISchemeSection = (props) => {
    const uiDef = { "type": "section",
                    "id": "uriScheme",
                    "content": [
                        {
                            "type": "textField",
                            "l10n_domain": "eliOntologyExtension",
                            "id": "elix:abstractLegalResourceUriScheme"
                        },
                        {
                            "type": "textField",
                            "l10n_domain": "eliOntologyExtension",
                            "id": "elix:legalResourceUriScheme"
                        },
                        {
                            "type": "textField",
                            "l10n_domain": "eliOntologyExtension",
                            "id": "elix:legalExpressionUriScheme"
                        },
                        {
                            "type": "textField",
                            "l10n_domain": "eliOntologyExtension",
                            "id": "elix:formatUriScheme"
                        }
                    ]};
    const state = Object.assign({}, props.state);
    state.edit_mode = undefined;
    return React.createElement(FormSection,
                               {state: state,
                                uiDef: uiDef,
                                path: [],
                                dispatch: props.dispatch,
                                localize: props.localize,
                                lang: props.lang
                               });
};

const FILTERS = {
    year: (x) => x.split('-')[0],
    month: (x) => x.split('-')[1],
    day: (x) => x.split('-')[2]
};

const compute_urischeme = (scheme, values, vocabs) => {
    let result = scheme;
    const uri_vars = extract_uri_vars(scheme);
    uri_vars.forEach(({name, filter}) => {
        const val = traverse_values(values, [name]);
        const key = name + (filter === null ? '' : '\\|'+filter);
        let v = "";
        if (val && val.value && val.value.length > 0) {
            v = (val.value[0] || "");
            if(filter !== null) {
                if(FILTERS[filter] !== undefined) {
                    v = FILTERS[filter](v);
                }
            } else if (vocabs !== undefined) {
                const matches = [];
                try {
                    Object.values(vocabs).reduce((a,b) => a.concat(b), []).filter(val => val["@id"] === v).forEach(val => matches.push(val));
                } catch(e) {
                    console.warn("Can't read the vocabularies while building URI", e);
                }
                if (matches.length > 0) {
                    const notat = getNotation(matches[0]);
                    if (notat === "") {
                        console.warn("Can't get notation of "+v+" vocabulary value for building URI");
                        v = "XXX "+loc("noNotationFor")+v+" XXX";
                    } else {
                        v = notat;
                    }
                }
            }
        }
        if (v !== "") {
            result = result.replace(RegExp('\{'+key+'\}','g'), v);
        }
    });
    return result;
};

const URISchemeSection = (props) => {
    /*const P = {
        uiDef: null,
        state: null,
        dispatch: null,
        edit: null,
        features: null,
        thispath: null
    };*/

    const thispath = ['elix:legalResourceUriScheme'];
    const thisId = path2Id(thispath);
    const value = traverse_values(props.state.values, thispath);
    const scheme = ((value) ? (value.value[0] || "") : "");
    const computed_value = compute_urischeme(scheme, props.state.values, props.state.vocabs);
    const field = (<div key={'key_'+thisId} id={'field/'+thisId} className='form-group'>
                   <label className='control-label'>{props.localize("legalResourceURI")}</label>
                  <input type='text' className='form-control'
                  disabled={true} value={computed_value || ''}/>
                  </div>);
    const P = {
        uiDef: { "type": "section",
                 "id": "uriSection",
                 "content": [] },
        state: props.state,
        localize: props.localize,
        lang: props.lang
    };
    return React.createElement(FormSection, P, [field]);
};

const EditableLangFormatSection = (props) => {
    const uiDef = { "type": "section",
                    "id": "langFormatChoice",
                    "content": [
                        {
                            "type": "selectField",
                            "l10n_domain": "eliOntologyExtension",
                            "id": "elix:languages_list"
                        },
                        {
                            "type": "selectField",
                            "l10n_domain": "eliOntologyExtension",
                            "id": "elix:formats_list"
                        }
                    ]};
    const state = Object.assign({}, props.state);
    state.edit_mode = undefined;
    return React.createElement(FormSection,
                               {state: state,
                                uiDef: uiDef,
                                path: [],
                                dispatch: props.dispatch,
                                localize: props.localize,
                                lang: props.lang
                               });
};

export default { compute_decorator_features,
                 compute_uri_vars, extract_uri_vars,
                 eliUriSchemeValidator, compute_urischeme, URISCHEME_KEYS,
                 eliUriSchemeDistinct,
                 renderChildren,
                 traverse_schema, enumerate_schema_paths,
                 traverse_values, enumerate_values_paths,
                 init_values, validate_value, VALIDATORS, validate_values,
                 reset_value, getInvalidValues, getInvalidURLs, path2Id, path2Id0,
                 jumpAndShow, missingVocabNotations,
                 /* export for testing purposes */
                 props4child, optionsFromVocab, get_uri_eligible_keys, full_title,
                 FormSection, FormSubSections,
                 FormFieldText, FormFieldDate, FormFieldSelect, FormFieldDecorator,
                 DecoratedFormFieldText,
                 URISchemeSection, EditableURISchemeSection,
                 EditableLangFormatSection
               };
