# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.myaddon.testing import COLLECTIVE_MYADDON_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that collective.myaddon is properly installed."""

    layer = COLLECTIVE_MYADDON_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.myaddon is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.myaddon'))

    def test_uninstall(self):
        """Test if collective.myaddon is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.myaddon'])
        self.assertFalse(self.installer.isProductInstalled('collective.myaddon'))

    def test_browserlayer(self):
        """Test that ICollectiveMyaddonLayer is registered."""
        from collective.myaddon.interfaces import ICollectiveMyaddonLayer
        from plone.browserlayer import utils
        self.assertIn(ICollectiveMyaddonLayer, utils.registered_layers())
