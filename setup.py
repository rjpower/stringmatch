#!/usr/bin/python

from setuptools import setup

setup(
    name='stringmatch',
    version='0.01',
    install_requires=[],
    packages=[ 'stringmatch' ],
    zip_safe=False,
    test_suite='py.test',
    entry_points='',
    cffi_modules=["stringmatch/match_builder.py:ffibuilder"],
)

