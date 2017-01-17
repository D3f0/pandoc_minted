#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'pandocfilters'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pandoc_minted',
    version='0.1.0',
    description="Pandoc filter to provide minted support (github.com/nick-ulle/pandoc-minted)",
    long_description=readme + '\n\n' + history,
    author="Nahuel Defossé",
    author_email='nahuel.defosse@gmail.com',
    url='https://github.com/D3f0/pandoc_minted',
    packages=[
        'pandoc_minted',
    ],
    package_dir={'pandoc_minted':
                 'pandoc_minted'},
    entry_points={
        'console_scripts': [
            'pandoc-minted=pandoc_minted.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pandoc_minted',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
