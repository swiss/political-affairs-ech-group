// -*- coding: utf-8 -*-
// Project sponsor is https://ec.europa.eu/isa2/
// License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

/* global require */

//@flow

import chai from 'chai'; /* global describe it */
import chaiEnzyme from 'chai-enzyme';
chai.use(chaiEnzyme());

import React from 'react';
var enzyme = require('enzyme'); // XXX import enzyme from 'enzyme' does not work

import FE from '../modules/FormElements';

const dummy_localize = (key, domain="uiMessages", component="label") => key;

describe('Helpers', () => {
    describe('traverse_schema', () => {
        it('should end correctly on leaves', () => {
            const schema = {properties: {somekey: 1}};
            chai.expect(FE.traverse_schema(schema, ['somekey'])).to.equal(1);
        });
        it('should traverse correctly', () => {
            const schema = {properties: {somepath: {properties: {somekey:2}}}};
            chai.expect(FE.traverse_schema(schema, ['somepath','somekey'])).to.equal(2);
            chai.expect(FE.traverse_schema(schema, [])).to.deep.equal(schema);
        });
    });
    describe('enumerate_schema_paths', () => {
        it('should work correctly', () => {
            const schema = {properties: {somepath: {properties: {somekey:{}, otherkey:{}}}}};
            chai.expect(FE.enumerate_schema_paths(schema))
                .to.deep.equal([['somepath','somekey'], ['somepath','otherkey']]);
        });
    });
    describe('traverse_values', () => {
        it('should end correctly on leaves', () => {
            const values = {somekey: {value: [1]}};
            chai.expect(FE.traverse_values(values, ['somekey']).value.length).to.equal(1);
            chai.expect(FE.traverse_values(values, ['somekey']).value[0]).to.equal(1);
        });
        it('should traverse correctly', () => {
            const values = {somepath: {somekey:2}};
            chai.expect(FE.traverse_values(values, ['somepath','somekey'])).to.equal(2);
        });
    });
    describe('enumerate_values_paths', () => {
        it('should work correctly', () => {
            const values = {somekey: {value: [1]}, somepath: {somekey2: {value: [2]}}};
            chai.expect(FE.enumerate_values_paths(values))
                .to.deep.equal([['somekey'], ['somepath','somekey2']]);
        });
    });
    describe('validate_value', () => {
        it('should validate correctly', () => {
            const loc = x => x;
            const schema_node = {validators: ['notempty']};
            const state = {uri_vars: new Set([]), edit_mode: false};
            let validation = FE.validate_value(schema_node, [], [1], state, loc);
            chai.expect(validation.valid).to.be.true;
        });
        it('should check uri_vars are not empty correctly', () => {
            const loc = x => x;
            const schema = {properties: {somekey: {}}};
            const state = {uri_vars: new Set(['somekey']), edit_mode: true};
            let validation = FE.validate_value(schema, ['somekey'], [], state, loc);
            chai.expect(validation.valid).to.be.true;
            state.edit_mode = false;
            validation = FE.validate_value(schema, ['somekey'], [], state, loc);
            chai.expect(validation.valid).to.be.false;
            validation = FE.validate_value(schema, ['somekey'], ['', null], state, loc);
            chai.expect(validation.valid).to.be.false;
            validation = FE.validate_value(schema, ['somekey'], [1], state, loc);
            chai.expect(validation.valid).to.be.true;
            validation = FE.validate_value(schema, ['somekey'], ["", 1, "stuff"], state, loc);
            chai.expect(validation.valid).to.be.true;
        });
    });
    describe('init_values', () => {
        it('should init values correctly', () => {
            const schema = {properties: {somepath: {properties: {somekey:2}}}};
            const v = FE.init_values(schema, {});
            chai.expect(v).to.deep.equal({somepath: {somekey: {value: []}}});
        });
    });
    describe('props4child', () => {
        it('should copy the properties', () => {
            const r = FE.props4child(3,{a:1,b:2},[]);
            chai.expect(r).to.deep.equal({a:1,b:2,uiDef:3,path:[],key:'key_undefined'});
        });
    });
    describe('extract_uri_vars', () => {
        it('should correctly extract vars', () => {
            chai.expect(FE.extract_uri_vars('http://some.gov.eu/{eli:type_document|filter1}-{eli:number|filter2}/{eli:version}'))
                .to.deep.equal([{name: 'eli:type_document', filter: 'filter1'},
                                {name: 'eli:number', filter: 'filter2'},
                                {name: 'eli:version', filter: null}]);
        });
    });
    describe('get_uri_eligible_keys', () => {
        it('should list all schema keys', () => {
            const schema = {properties:
                            {'eli:type_document': {type: 'string'},
                             'subpath': {properties:
                                         {'eli:date_document': {type: 'string'}}}
                            }
                           };
            chai.expect(FE.get_uri_eligible_keys(schema))
                .to.deep.equal(['eli:type_document','eli:date_document', 'eli:language', 'eli:format']);
        });
        it('should list keys in eligible_uri_properties of schema', () => {
            const schema = {eligible_uri_properties: ["eli:type_document", "eli:number"],
                            properties:
                            {'eli:type_document': {type: 'string'},
                             'eli:number' : {type: 'string'},
                             'subpath': {properties:
                                         {'eli:date_document': {type: 'string'}}}
                            }
                           };
            chai.expect(FE.get_uri_eligible_keys(schema))
                .to.deep.equal(['eli:type_document','eli:number']);
        });
    });
    describe('eliUriSchemeValidator', () => {
        it('should correctly validate vars', () => {
            const uriScheme = 'http://some.gov.eu/{eli:type_document}-{eli:unknown}/{eli:juridiction}';
            const state = {schema: {id: 'sectionOne',
                                    eligible_uri_properties: ["eli:type_document", "eli:number"],
                                    properties: {
                                        'eli:type_document': {type: 'string'},
                                        'eli:number' : {type: 'string'},
                                        'eli:date_document': {type: 'string'}
                                    }
                                   }
                          };
            const invalidIds = FE.eliUriSchemeValidator(uriScheme, state);
            chai.expect(invalidIds).to.deep.equal(['eli:unknown','eli:juridiction']);
        });
    });
    describe('eliUriSchemeDistinct', () => {
        it('should be false if two uri patterns are equal', () => {
            const state = {
                values: {
                    "elix:abstractLegalResourceUriScheme": {
                        msg: null, valid: true, value: ["a"]
                    },
                    "elix:legalResourceUriScheme": {
                        msg: null, valid: true, value: ["a/b"]
                    },
                    "elix:legalExpressionUriScheme": {
                        msg: null, valid: true, value: ["a/b/c"]
                    },
                    "elix:formatUriScheme": {
                        msg: null, valid: true, value: ["a/b/c/d"]
                    }
                }
            };
            const all_different = FE.eliUriSchemeDistinct("a", state);
            chai.expect(all_different).to.be.true;
            state.values["elix:legalResourceUriScheme"].value = "a";
            const not_all_different = FE.eliUriSchemeDistinct("a", state);
            chai.expect(not_all_different).to.be.false;
        });
    });

    describe('compute_urischeme', () => {
        it('should compute correctly', () => {
            chai.expect(FE.compute_urischeme('http://some.gov.eu/', {}))
                .to.equal('http://some.gov.eu/');
            chai.expect(FE.compute_urischeme('http://some.gov.eu/{somekey}',
                                             {somekey: {value: ['act']}}))
                .to.equal('http://some.gov.eu/act');
            chai.expect(FE.compute_urischeme('http://some.gov.eu/{somekey}/{otherkey}',
                                             {somekey: {value: ['act']}, otherkey: {value: [1]}}))
                .to.equal('http://some.gov.eu/act/1');
        });
        it('should compute date filters correctly', () => {
            chai.expect(FE.compute_urischeme('http://some.gov.eu/{somekey|year}{somekey|month}{somekey|day}',
                                             {somekey: {value: ['2017-05-29']}}))
                .to.equal('http://some.gov.eu/20170529');
        });
        it('should compute vocab values correctly', () => {
            const vocabs = {"http://test.com/vocab1": [
                {"@id": "http://test.com/vocab1#one",
                 "@type": ["http://www.w3.org/2004/02/skos/core#Concept"],
                 "http://www.w3.org/2004/02/skos/core#notation" : [
                     {"@value": 'ONE'}]
                },
                {"@id": "http://test.com/another-uri#two",
                 "@type": ["http://www.w3.org/2004/02/skos/core#Concept"],
                 "http://www.w3.org/2004/02/skos/core#notation" : [
                     {"@value": 'TWO'}]
                }],
                            "http://test.com/vocab2": [
                {"@id": "http://test.com/vocab2#one",
                 "@type": ["http://www.w3.org/2004/02/skos/core#Concept"],
                 "http://www.w3.org/2004/02/skos/core#notation" : [
                     {"@value": 'ONE.2'}]
                },
                {"@id": "http://test.com/vocab2#two",
                 "@type": ["http://www.w3.org/2004/02/skos/core#Concept"],
                 "http://www.w3.org/2004/02/skos/core#notation" : [
                     {"@value": 'TWO.2'}]
                }]
                           };
            chai.expect(FE.compute_urischeme('http://some.gov.eu/{somekey}/{otherkey}',
                                             {somekey: {value: ["http://test.com/another-uri#two"]},
                                              otherkey: {value: ["http://test.com/vocab2#one"]}},
                                             vocabs))
                .to.equal('http://some.gov.eu/TWO/ONE.2');
        });
    });
    describe('getInvalidValues', () => {
        it('should not bomb on empty values or keys without a valid flag', () => {
            chai.expect(FE.getInvalidValues({})).to.deep.equal([]);
            chai.expect(FE.getInvalidValues({"eli:type_document": {value: ["XX"]}})).to.deep.equal([]);
        });
        it('should return keys with a valid flag set to false', () => {
            const values = {"eli:type_document": {valid: true, value:["XX"]},
                            "eli:transposes": {valid: false, value: ["YY"]},
                            "lang_ENG": {"eli:title": {valid: false, value: [""]}
                                        }
                           };
            chai.expect(FE.getInvalidValues(values)).to.deep.equal(
                [["eli:transposes"], ["lang_ENG", "eli:title"]]);
        });
    });
    describe('getInvalidURLs', () => {
        it('should not bomb on empty values or values without a url_valid flag', () => {
            chai.expect(FE.getInvalidURLs({})).to.deep.equal([]);
            chai.expect(FE.getInvalidURLs({"eli:transposes": {value: ["XX"]}})).to.deep.equal([]);
        });
        it('should return keys with a url_valid flag set to false', () => {
            const values = {"eli:type_document": {valid: true, value: ["XX"]},
                            "eli:transposes": {url_valids: {"EE": {"valid": true}, "YY": {"valid": false}}, valid: true, value: ["EE", "YY"]},
                            "lang_ENG": {"eli:title": {valid: false, value: [""]},
                                         "eli:repeals": {url_valids: {"ZZ": {"valid": false}}, valid: true, value: ["ZZ"]}
                                        }
                           };
            chai.expect(FE.getInvalidURLs(values)).to.deep.equal(
                [["eli:transposes"], ["lang_ENG", "eli:repeals"]]);
        });
    });
});

const localizations = {uiMessages: {}, formFields: {}, somedomain: {node1: {label: 'Some Domain'}}};
const EmptySpanComponent = (props) => <span className="noop" />;

describe('Form*', () => {
    const mkprops = () => ({state: {values: {'node1': {value: [], valid: true} },
                                    localizations: localizations,
                                    schema: {properties:
                                             {'node1':
                                              {title: 'NodeOne',
                                               type: 'string',
                                               enabled: true,
                                               mandatory: true
                                              }}},
                                    available_vocabs: null,
                                    uri_vars: new Set(),
                                    vocabs: {}
                                   },
                            localize: dummy_localize,
                            path: [],
                            thispath: ['node1'],
                            uiDef: {id: 'node1',
                                    input_type: 'text',
                                    ui_object: 'field',
                                    l10n_domain: 'somedomain',
                                   }
                           });
    describe('FormFieldText', () => {
        it('should render', () => {
            const props = mkprops();
            props.features = FE.compute_decorator_features(props);
            const wrapper = enzyme.mount(React.createElement(FE.FormFieldText, props));
            chai.expect(wrapper).to.have.descendants('input');
        });
    });
    describe('FormFieldDate', () => {
        it('should render', () => {
            const props = mkprops();
            props.uiDef.type = 'dateField';
            props.features = FE.compute_decorator_features(props);
            const wrapper = enzyme.mount(React.createElement(FE.FormFieldDate, props));
            chai.expect(wrapper).to.have.descendants('input');
        });
        it('should be disabled when config mode', () => {
            const props = mkprops();

            // date field disabled when edit
            props.uiDef.type = 'dateField';
            props.state.edit_mode = true;
            props.features = FE.compute_decorator_features(props);
            let ft = FE.compute_decorator_features(props);
            chai.expect(ft.input_enabled).to.equal(false);

            props.state.edit_mode = false;
            props.features = FE.compute_decorator_features(props);
            ft = FE.compute_decorator_features(props);
            chai.expect(ft.input_enabled).to.equal(true);
            // XXX test FormFieldDate ?

        });
    });
    describe('FormFieldSelect', () => {
        it('should render', () => {
            const props = mkprops();
            props.features = FE.compute_decorator_features(props);
            const wrapper = enzyme.mount(React.createElement(FE.FormFieldSelect, props));
            //chai.expect(wrapper).to.have.descendants('div');
        });
        it('should compute options from vocab', () => {
            const vocab = [{"@id": "http://test.com/vocab#one",
                            "@type": ["http://www.w3.org/2004/02/skos/core#Concept"],
                            "http://www.w3.org/2004/02/skos/core#notation" : [
                                {"@value": 'ONE'}],
                            "http://www.w3.org/2004/02/skos/core#prefLabel" : [
                                {"@language": "fr",
                                 "@value": 'un'},
                                {"@language": "en",
                                 "@value": 'one'}]
                           },
                           {"@id": "http://test.com/vocab#two",
                            "@type": ["http://www.w3.org/2004/02/skos/core#Concept"],
                            "http://www.w3.org/2004/02/skos/core#notation" : [
                                {"@value": 'TWO'}],
                            "http://www.w3.org/2004/02/skos/core#prefLabel" : [
                                {"@language": "fr",
                                 "@value": 'deux'},
                                {"@language": "en",
                                 "@value": 'two'}]
                           }];
            // vocab in french
            let options = FE.optionsFromVocab(vocab, 'fr');
            let expected = [{'value': "http://test.com/vocab#two",
                             'notation': "TWO",
                             'label': "deux - TWO"},
                            {'value': "http://test.com/vocab#one",
                             'notation': "ONE",
                             'label': "un - ONE"}];
            chai.expect(options).to.deep.equal(expected);
            // vocab in english
            options = FE.optionsFromVocab(vocab, 'en');
            expected = [{'value': "http://test.com/vocab#one",
                         'notation': "ONE",
                         'label': "one - ONE"},
                        {'value': "http://test.com/vocab#two",
                         'notation': "TWO",
                         'label': "two - TWO"}];
            chai.expect(options).to.deep.equal(expected);
        });
        it('should compute disabled state', () => {
            const props = mkprops();
            props.features = FE.compute_decorator_features(props);
            // select field disabled when not edit and no vocab
            const wrapper = enzyme.mount(React.createElement(FE.FormFieldSelect, props));
            chai.expect(wrapper).to.have.className('is-disabled');
        });
    });

    // *************************************************************************

    describe('Decorator features', () => {
        it('should display unless disabled and input mode', () => {
            const props = mkprops();

            props.state.edit_mode = true;
            props.state.schema.properties.node1.enabled = true;
            let ft = FE.compute_decorator_features(props);
            chai.expect(ft.is_displayed).to.equal(true);

            props.state.edit_mode = true;
            props.state.schema.properties.node1.enabled = false;
            ft = FE.compute_decorator_features(props);
            chai.expect(ft.is_displayed).to.equal(true);

            props.state.edit_mode = false;
            props.state.schema.properties.node1.enabled = true;
            ft = FE.compute_decorator_features(props);
            chai.expect(ft.is_displayed).to.equal(true);

            props.state.edit_mode = false;
            props.state.schema.properties.node1.enabled = false;
            ft = FE.compute_decorator_features(props);
            chai.expect(ft.is_displayed).to.equal(false);
        });
        it('should collapse the input when disabled and config mode', () => {
            const props = mkprops();

            props.state.edit_mode = true;
            props.state.schema.properties.node1.enabled = true;
            let ft = FE.compute_decorator_features(props);
            chai.expect(ft.is_collapsed).to.equal(false);

            props.state.edit_mode = true;
            props.state.schema.properties.node1.enabled = false;
            ft = FE.compute_decorator_features(props);
            chai.expect(ft.is_collapsed).to.equal(true);

            props.state.edit_mode = false;
            props.state.schema.properties.node1.enabled = true;
            ft = FE.compute_decorator_features(props);
            chai.expect(ft.is_collapsed).to.equal(false);

            props.state.edit_mode = false;
            props.state.schema.properties.node1.enabled = false;
            ft = FE.compute_decorator_features(props);
            chai.expect(ft.is_collapsed).to.equal(false);
        });
        it('should be mandatory if used in uri scheme or marked as such', () => {
            const props = mkprops();

            props.state.schema.properties.node1.mandatory = true;
            let ft = FE.compute_decorator_features(props);
            chai.expect(ft.is_urivar).to.equal(false);
            chai.expect(ft.is_mandatory).to.equal(true);

            props.state.schema.properties.node1.mandatory = false;
            ft = FE.compute_decorator_features(props);
            chai.expect(ft.is_urivar).to.equal(false);
            chai.expect(ft.is_mandatory).to.equal(false);

            props.state.uri_vars.add('node1');
            ft = FE.compute_decorator_features(props);
            chai.expect(ft.is_urivar).to.equal(true);
            chai.expect(ft.is_mandatory).to.equal(true);
        });
        it('should enable the mandatory button in config mode unless in uri vars', () => {
            const props = mkprops();

            props.state.edit_mode = false;
            let ft = FE.compute_decorator_features(props);
            chai.expect(ft.mandatory_enabled).to.equal(false);

            props.state.edit_mode = true;
            ft = FE.compute_decorator_features(props);
            chai.expect(ft.mandatory_enabled).to.equal(true);

            props.state.uri_vars.add('node1');
            ft = FE.compute_decorator_features(props);
            chai.expect(ft.mandatory_enabled).to.equal(false);
        });
        it('should enable the vocab selection when config mode and vocabs avalaible', () => {
            const props = mkprops();

            props.uiDef.type = 'unknown';
            props.state.edit_mode = true;
            let ft = FE.compute_decorator_features(props);
            chai.expect(ft.vocab_enabled).to.equal(false);

            props.state.edit_mode = false;
            ft = FE.compute_decorator_features(props);
            chai.expect(ft.vocab_enabled).to.equal(false);

            props.uiDef.type = 'selectField';
            props.state.edit_mode = true;
            ft = FE.compute_decorator_features(props);
            chai.expect(ft.vocab_enabled).to.equal(true);

            props.state.edit_mode = false;
            ft = FE.compute_decorator_features(props);
            chai.expect(ft.vocab_enabled).to.equal(false);

            props.state.edit_mode = true;
            props.state.schema.properties.node1.enabled = false;
            ft = FE.compute_decorator_features(props);
            chai.expect(ft.vocab_enabled).to.equal(false);
        });
    });

    /*
    // *************************************************************************

    describe('EmptySpanComponent', () => {
        it('should render', () => {
            const span = enzyme.shallow(React.createElement(EmptySpanComponent, {}));
            chai.expect(span).to.have.descendants('span');
        });
    });


    // *************************************************************************

    describe('FormFieldDecorator', () => {
        const decoratedspan = FE.FormFieldDecorator(EmptySpanComponent);

        it('should render', () => {
            const props = mkprops();
            const wrapper = enzyme.mount(React.createElement(decoratedspan, props));
            chai.expect(wrapper).to.contain(<span className="noop"/>);
        });
        it('should display mandatory icon', () => {
            const props = mkprops();
            props.is_mandatory = true;
            const wrapper = enzyme.mount(React.createElement(decoratedspan, props));
            chai.expect(wrapper).containMatchingElement(<span className="glyphicon glyphicon-asterisk mandatory small"/>);
        });
        it('should collapse', () => {
            const props = mkprops();
            props.is_collapsed = true;
            const wrapper = enzyme.mount(React.createElement(decoratedspan, props));
            chai.expect(wrapper).not.containMatchingElement(<span className="noop"/>);
        });
        it('should have class has-error only when value is invalid', () => {
            const props = mkprops();
            const wrapper = enzyme.mount(React.createElement(decoratedspan, props));
            chai.expect(wrapper).not.have.className('has-error');
            props.state.values.node1.valid = false;
            const wrapper2 = enzyme.mount(React.createElement(decoratedspan, props));
            chai.expect(wrapper2).have.className('has-error');
        });
        it('should pass the field value in props', () => {
            const props = mkprops();
            props.state.values.node1.value = 1;
            props.bidule = true;
            const wrapper = enzyme.mount(React.createElement(decoratedspan, props));
            chai.expect(wrapper.component.props).to.deep.equal({value: 1, valid: true});
            //chai.expect(wrapper.find('span')).to.have.props({value: 1});
        });
        it.skip('should have a disabled input if edit and date or not edit and computed', () => {
            const decoratedspan = FE.FormFieldDecorator(EmptySpanComponent);
            const props = mkprops();
            props.edit = true; // and dateField
            const wrapper = enzyme.mount(React.createElement(decoratedspan, props));
            chai.expect(wrapper.find('span')).to.have.props('is_disabled', true);
        });
    });
*/

});

