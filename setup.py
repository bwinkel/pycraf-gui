#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser


# Get some values from the setup.cfg
conf = ConfigParser()
conf.read(['setup.cfg'])
metadata = dict(conf.items('metadata'))

PACKAGENAME = metadata.get('package_name', 'pycraf-gui')
DESCRIPTION = metadata.get('description', 'pycraf-gui')
LONG_DESCRIPTION = metadata.get('long_description', '')
AUTHOR = metadata.get('author', 'Benjamin Winkel')
AUTHOR_EMAIL = metadata.get('author_email', '')
LICENSE = metadata.get('license', 'GPLv3')
URL = metadata.get('url', 'https://github.com/bwinkel/pycraf-gui')
# PROJECT_URLS = metadata.get('project_urls', '')
CLASSIFIERS = metadata.get('classifiers', '').split('\n')
CLASSIFIERS = [c for c in CLASSIFIERS if len(c)]  # filter out empty strings
__minimum_python_version__ = metadata.get("minimum_python_version", "3.5")

if os.path.exists('README.rst'):
    with open('README.rst') as f:
        LONG_DESCRIPTION = f.read()

# NOTE: for github pages, put an empty .nojekyll into the root dir of
# the web directory (gh-pages branch root)

entry_points = {}

# # Define entry points for command-line scripts
# entry_points['console_scripts'] = []

# if conf.has_section('entry_points'):
#     entry_point_list = conf.items('entry_points')
#     for entry_point in entry_point_list:
#         entry_points['console_scripts'].append('{0} = {1}'.format(
#             entry_point[0], entry_point[1]))

# Define entry points for GUI scripts
entry_points['gui_scripts'] = []

if conf.has_section('entry_points_gui'):
    entry_point_list = conf.items('entry_points_gui')
    for entry_point in entry_point_list:
        entry_points['gui_scripts'].append('{0} = {1}'.format(
            entry_point[0], entry_point[1]))


setup(
    name=PACKAGENAME,
    use_scm_version=True,  # provides version
    # use  the following to read version in package files
    # from pkg_resources import get_distribution, DistributionNotFound
    # try:
    #     __version__ = get_distribution(__name__).version
    # except DistributionNotFound:
    #     # package is not installed
    #     pass
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license=LICENSE,
    install_requires=[
        'setuptools',
        'numpy',
        ],
    tests_require=['pytest', 'numpy', 'pycraf'],
    packages=find_packages(),
    # zip_safe=False,
    entry_points=entry_points,
    python_requires='>={}'.format(__minimum_python_version__),
    classifiers=CLASSIFIERS,
    )
