# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import os
import unittest
import hospital

@hospital.healthcheck
class FilesystemHCheck(unittest.TestCase):
    def test_ping(self):
        """/var/lib/eli-annotation must be writable."""
        assert os.access("/var/lib/eli-annotation", os.W_OK)
