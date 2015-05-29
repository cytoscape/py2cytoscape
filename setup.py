#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup script for py2cytoscape

To install, run:

python setup.py install
"""

from setuptools import setup, find_packages

setup(
    name='py2cytoscape',
    version='0.4.0',
    description='Tools to use Cytoscape and Cytoscape.js from Python',
    author='Keiichiro Ono',
    author_email='kono@ucsd.edu',
    url='http://www.cytoscape.org/',
    license='MIT License',
    keywords=['data visualization', 'visualization', 'cytoscape',
              'bioinformatics'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    test_suite='tests',
    packages=find_packages(),
    package_data={'py2cytoscape': ['cytoscapejs/*.js', 'cytoscapejs/*.html', 'cytoscapejs/*.json']}
)
