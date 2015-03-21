#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
    params = dict(
        packages=find_packages(),
        entry_points={
            'console_scripts': ['s5server = s5.server.__main__:main',
                                's5 = s5.client.cli:main']
        },
        install_requires=['pycrypto'],
    )
except ImportError:
    import sys
    print('Warning: Installing s5 with distutils instead of setuptools.\n'
          'Please ensure that you have pycrypto installed and add scripts\n'
          'to your shell\'s PATH that execute s5.client and s5.server.',
          file=sys.stderr)
    from distutils.core import setup
    params = dict(
        packages=['s5', 's5.plugins', 's5.server', 's5.shared', 's5.client',
                  's5.plugins.crypto', 's5.plugins.compression',
                  's5.plugins.items']
    )

setup(
    name='s5',
    description='Secure Self hosted Synchronization and Sharing Service (S5)',
    author='wonko@hanstool.org',
    version='0.0',
    **params
)
