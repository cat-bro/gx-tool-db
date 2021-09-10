#!/usr/bin/env python

import ast
import os
import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

SOURCE_DIR = "gx_tool_db"

_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open(f'{SOURCE_DIR}/__init__.py', 'rb') as f:
    init_contents = f.read().decode('utf-8')

    def get_var(var_name):
        pattern = re.compile(fr'{var_name}\s+=\s+(.*)')
        match = pattern.search(init_contents).group(1)
        return str(ast.literal_eval(match))

    version = get_var("__version__")
    PROJECT_NAME = get_var("PROJECT_NAME")
    PROJECT_URL = get_var("PROJECT_URL")
    PROJECT_AUTHOR = get_var("PROJECT_AUTHOR")
    PROJECT_EMAIL = get_var("PROJECT_EMAIL")

TEST_DIR = 'tests'
PROJECT_DESCRIPTION = 'Management utility for YAML database of Galaxy tools'
PACKAGES = [
    'gx_tool_db',
]
ENTRY_POINTS = '''
     [console_scripts]
     gx-tool-db=gx_tool_db.main:main
'''
PACKAGE_DATA = {
    # Be sure to update MANIFEST.in for source dist.
    'gx_tool_db': [
        "credentials.json",
    ],
}
PACKAGE_DIR = {
    SOURCE_DIR: SOURCE_DIR,
}

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

if os.path.exists("requirements.txt"):
    requirements = open("requirements.txt").read().split("\n")
else:
    # In tox, it will cover them anyway.
    requirements = []


test_requirements = [
    # TODO: put package test requirements here
]


setup(
    name=PROJECT_NAME,
    version=version,
    description=PROJECT_DESCRIPTION,
    long_description=readme + '\n\n' + history,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    url=PROJECT_URL,
    packages=PACKAGES,
    entry_points=ENTRY_POINTS,
    package_data=PACKAGE_DATA,
    package_dir=PACKAGE_DIR,
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='galaxy',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Topic :: Software Development',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Testing',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    test_suite=TEST_DIR,
    tests_require=test_requirements
)
