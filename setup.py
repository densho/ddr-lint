#!/usr/bin/env python

from distutils.core import setup

setup(
    description = 'ddr-lint',
    author = 'Geoffrey Jost',
    url = 'https://github.com/densho/ddr-lint/',
    download_url = 'https://github.com/densho/ddr-lint.git',
    author_email = 'geoffrey.jost@densho.org',
    version = '0.1',
    packages = ['ddrlint'],
    package_dir = {'ddrlint': 'ddrlint'},
    package_data = {},
    scripts = ['bin/ddrlint',],
    name = 'ddrlint'
)
