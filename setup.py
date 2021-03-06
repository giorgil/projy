#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Projy setup.py script """

# system
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import os
# projy
from projy import __version__

# cross-platform incantations
osname = os.uname()[0]
install_requires = ['blessings']
if osname == 'Windows':
    install_requires = []


setup(
    name='Projy',
    version=__version__,
    description='Projy is a template-based skeleton generator.',
    author='Stéphane Péchard',
    author_email='stephanepechard@gmail.com',
    packages=['projy','projy.templates', 'projy.collectors'],
    url='http://stephanepechard.github.com/projy',
    long_description=open('README.txt').read(),
    entry_points = {
        'console_scripts': [
            'projy = projy.cmdline:execute',
        ],
    },
    install_requires=install_requires,
    tests_require=['nose'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Filesystems',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: System Shells',
        'Topic :: Utilities',
      ],
)

