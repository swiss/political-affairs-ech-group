# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import os
import os.path as osp

from . import vocabs, notices, form_configs, xslt_transform

class DataIndex:

    def __init__(self, basedir):
        self.basedir = basedir
        if not osp.exists(osp.join(basedir,'vocabs')):
            os.makedirs(osp.join(basedir,'vocabs'))
        if not osp.exists(osp.join(basedir,'notices')):
            os.makedirs(osp.join(basedir,'notices'))
        if not osp.exists(osp.join(basedir,'forms')):
            os.makedirs(osp.join(basedir,'forms'))
        if not osp.exists(osp.join(basedir,'localizations')):
            os.makedirs(osp.join(basedir,'localizations'))
        self.vocab_index = vocabs.VocabularyIndex(os.path.join(self.basedir,'vocabs'))
        self.notice_index = notices.NoticeIndex(os.path.join(self.basedir,'notices'))
        self.form_index = form_configs.FormConfigIndex(os.path.join(self.basedir,'forms'))
        self.l10n_dir = osp.join(self.basedir,'localizations')
        xslt_transform.build_xml_glossary(self.l10n_dir)

