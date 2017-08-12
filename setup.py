# -*- coding: utf-8 -*-
from __future__ import with_statement
import os
from setuptools import setup

# A simple internal workaround to pypiwin32 setup dependancy 
version = '221'

setup(
    name='pypiwin32',
    version=version,
    packages=[],
    install_requires=['pywin32>=%s' % version]
)
