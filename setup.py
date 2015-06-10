#!/usr/bin/env python

#


"""A setuptools based setup module based on

https://raw.githubusercontent.com/pypa/sampleproject/master/setup.py

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

long_description = """
This is a test module

"""


pkg_list = find_packages(exclude=['contrib', 'docs', 'test*'])
exec(open('{0[0]}/version.py'.format(pkg_list)).read())

def get_version():
    # In case there's a customization to how we want to represent the version
    # string.  I like apending the git hash when developing.
    # -pcn
    global __version__
    return __version__


setup(
    name='prettypublictest',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=get_version(),

    description='Test build - a flask app',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/pcn/prettypublictest',

    # Author details
    author='Peter C. Norton',
    author_email='spacey@spacey.org',

    # Choose your license
    license='Apache 2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Operations',
        'Topic :: Infrastructure Automation :: Libraries',

        # Pick your license as you wish (should match "license" above)
        # 'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        #'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.2',
        #'Programming Language :: Python :: 3.3',
        #'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='test',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=pkg_list,

    scripts=[
        'bin/runserver.py',
    ],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # install_requires=['peppercorn'],
    install_requires = [l.strip().decode('utf-8') for l in open('requirements.txt').readlines()],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': [l.strip() for l in open('requirements-test.txt').readlines()]
    # },
)
