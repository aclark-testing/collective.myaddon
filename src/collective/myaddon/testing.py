# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig

import collective.myaddon


class CollectiveMyaddonLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.file(
            'configure.zcml',
            collective.myaddon,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.myaddon:default')


COLLECTIVE_MYADDON_FIXTURE = CollectiveMyaddonLayer()


COLLECTIVE_MYADDON_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_MYADDON_FIXTURE,),
    name='CollectiveMyaddonLayer:IntegrationTesting'
)


COLLECTIVE_MYADDON_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_MYADDON_FIXTURE,),
    name='CollectiveMyaddonLayer:FunctionalTesting'
)


COLLECTIVE_MYADDON_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_MYADDON_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveMyaddonLayer:AcceptanceTesting'
)
