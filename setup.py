#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('./docs/readme.rst') as readme_file:
    readme = readme_file.read()

with open('./docs/history.rst') as history_file:
    history = history_file.read()

with open('./docs/installation.rst') as installation_file:
    installation = installation_file.read()

with open('./docs/usage.rst') as usage_file:
    usage = usage_file.read()

requirements = [
    'lxml',
    'elist',
    'edict'
]

setup_requirements = [
    'lxml',
    'elist',
    'edict'
]


setup(
    name='nvhtml',
    version='0.0.20',
    description="A Python library manipulate html",
    long_description=readme + '\n\n' + installation + '\n\n' + usage + '\n\n' + history,
    author="dli",
    author_email='286264978@qq.com',
    url='https://github.com/ihgazni2/nvhtml',
    entry_points = {
         'console_scripts': [
                                'nvhtml_beauty=nvhtml.bin:main',
                                'nvhtml_tag=nvhtml.TAGS.bin_nvhtml_tag:main',
                                'nvhtml_tgpth=nvhtml.TAGS.bin_nvhtml_tgpth:main'
                            ]
    },
    packages=find_packages(),
    package_data={
                  'documentation': ['docs/*'],
                 },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    keywords='html,tag,level,search',
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    setup_requires=setup_requirements,
    py_modules=['nvhtml'],
)
