#!/usr/bin/env python

from setuptools import setup

with open('README.rst') as readme:
    long_description = readme.read()

version = check_output(['git', 'describe']).decode('utf-8').strip().replace('v','')

setup(
    name='mgen',
    version=version,
    description='Matrix generation functions',
    author='NOhs',
    packages=['mgen'],
    long_description=long_description,
    install_requires=['numpy'],
    license='BSD',
    url='https://github.com/NOhs/mgen',
    keywords=['matrix', 'rotations', 'Euler angles'])