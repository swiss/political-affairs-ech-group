# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

ENGLISH = 'http://publications.europa.eu/resource/authority/language/ENG'
FRENCH = 'http://publications.europa.eu/resource/authority/language/FRA'
PRINT = 'http://publications.europa.eu/resource/authority/product-form/PRINT'
PDF = 'https://www.iana.org/assignments/media-types/application/pdf'
VALUES_DATA = {
    ('elix:resource_type',): ['elix:Act'],
    ('elix:languages_list',): [ENGLISH,FRENCH],
    ('elix:formats_list',): [PDF, PRINT],

    ('elix:abstractLegalResourceUriScheme',): ['http://example/{eli:date_document|year}/{eli:type_document}'],
    ('elix:legalResourceUriScheme',): ['http://example/{eli:date_document|year}/{eli:type_document}/ACT'],
    ('elix:legalExpressionUriScheme',): ['http://example/{eli:date_document|year}/{eli:type_document}/ACT/{eli:language}'],
    ('elix:formatUriScheme',): ['http://example/{eli:date_document|year}/{eli:type_document}/ACT/{eli:language}/{eli:format}'],

    ('eli:consolidates',): [],
    ('eli:date_document',): ['2017-09-04'],
    ('eli:id_local',): ['ID1'],
    ('eli:is_about',): ["http://data.sparna.fr/vocabularies/days#saturday", "http://data.sparna.fr/vocabularies/days#friday"],
    ('eli:number',) : ["412",],
    ('eli:transposes',): [],
    ('eli:type_document',): ["http://test.logilab.org/document#ABC"],
    (ENGLISH, 'eli:language'): [ENGLISH],
    (ENGLISH, 'eli:id_local'): ['ID1-ENG'],
    (ENGLISH, 'eli:title'): ['English title'],
    (ENGLISH, PRINT, 'eli:format'): [PRINT],
    (ENGLISH, PRINT, 'eli:published_in'): ['The English journal'],
    (ENGLISH, PDF, 'eli:format'): [PDF],
    (ENGLISH, PDF, 'eli:id_local'): ['ID1-ENG-PDF'],
    (ENGLISH, PDF, 'eli:is_exemplified_by'): ['http://document/english/pdf'],
    (FRENCH, 'eli:language'): [FRENCH],
    (FRENCH, 'eli:id_local'): ['ID1-FRA'],
    (FRENCH, 'eli:title'): ['Titre français'],
    (FRENCH, PRINT, 'eli:format'): [PRINT],
    (FRENCH, PRINT, 'eli:id_local'): ['ID1-FRA-PRINT'],
    (FRENCH, PRINT, 'eli:published_in'): ['Le journal français'],
    (FRENCH, PDF, 'eli:format'): [PDF],
    (FRENCH, PDF, 'eli:is_exemplified_by'): ['http://document/french/PDF'],
}
