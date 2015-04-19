from plone import api
from Products.Five.browser import BrowserView
from collective.transmogrifier.transmogrifier import Transmogrifier


class PloneorgMigrationMain(BrowserView):

    def __call__(self):
        portal = api.portal.get()
        transmogrifier = Transmogrifier(portal)
        transmogrifier('plone.org.main')
