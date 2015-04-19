# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig

import ploneorg.migration


class PloneorgMigrationLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.file(
            'configure.zcml',
            ploneorg.migration,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ploneorg.migration:default')


PLONEORG_MIGRATION_FIXTURE = PloneorgMigrationLayer()


PLONEORG_MIGRATION_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONEORG_MIGRATION_FIXTURE,),
    name='PloneorgMigrationLayer:IntegrationTesting'
)


PLONEORG_MIGRATION_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONEORG_MIGRATION_FIXTURE,),
    name='PloneorgMigrationLayer:FunctionalTesting'
)


PLONEORG_MIGRATION_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONEORG_MIGRATION_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PloneorgMigrationLayer:AcceptanceTesting'
)
