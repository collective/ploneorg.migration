# -*- coding: utf-8 -*-
"""Installer for the ploneorg.migration package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')


setup(
    name='ploneorg.migration',
    version='0.1',
    description="Transmogrifier pipeline used for plone.org migration (from AT to DX via JSON)",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3.4",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Python Plone',
    author='Victor Fernandez de Alba',
    author_email='sneridagh@gmail.com',
    url='http://pypi.python.org/pypi/ploneorg.migration',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['ploneorg'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'setuptools',
        'transmogrify.dexterity',
        'quintagroup.transmogrifier',
        'collective.jsonmigrator',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
