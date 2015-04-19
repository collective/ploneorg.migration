# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from ploneorg.migration.testing import PLONEORG_MIGRATION_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that ploneorg.migration is properly installed."""

    layer = PLONEORG_MIGRATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ploneorg.migration is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('ploneorg.migration'))

    def test_uninstall(self):
        """Test if ploneorg.migration is cleanly uninstalled."""
        self.installer.uninstallProducts(['ploneorg.migration'])
        self.assertFalse(self.installer.isProductInstalled('ploneorg.migration'))

    def test_browserlayer(self):
        """Test that IPloneorgMigrationLayer is registered."""
        from ploneorg.migration.interfaces import IPloneorgMigrationLayer
        from plone.browserlayer import utils
        self.assertIn(IPloneorgMigrationLayer, utils.registered_layers())
