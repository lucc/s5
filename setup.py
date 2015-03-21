#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='s5',
    description='Secure Self hosted Synchronization and Sharing Service (S5)',
    author='wonko@hanstool.org',
    version='0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['s5server = s5.server', 's5 = s5.client']
    },
    install_requires=['pycrypto'],
)
