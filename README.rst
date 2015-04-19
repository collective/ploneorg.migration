====================
ploneorg.migration
====================

This package is the responsible for the migration from the old plone.org to the
new (2015) plone.org. This is because we want to get rid of the old ZODB and
begin from scratch with a brand new one. The migration is made using a
Transmogrifier pipeline transforming this origin:

Plone 4.3.x AT-based content types

to this destination:

Plone 4.3.4 plone.app.contenttypes-based types

over the wire, using JSON exports. This pipeline can be used to migrate any site
that has this requirements.

This package uses the wisdom and knowledge of several Transmogrifier packages
available in the community:

 * collective.transmogrifier
 * plone.app.transmogrifier
 * quintagroup.transmogrifier
 * transmogrify.dexterity

and adding some custom modifications to fix some procedures to solve the own use
case.

The JSON export is made using a customized version that can be found in the
package ploneorg.jsonify and reusing the wisdow in:

 * collective.jsonmigrator
 * collective.jsonify
