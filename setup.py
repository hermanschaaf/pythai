#-*- coding: UTF-8 -*-
from setuptools import setup,find_packages,Command, Extension
import os

setup(
    name="pythai",
    version="0.1.3",
    packages=['pythai'],

    ext_modules=[ 
        Extension("libthai", 
                  ["pythai/libthai.c"],
                  libraries=['thai'])],

    # Required repositories
    install_requires=[
        'nose',
        'six',
        'future>=0.16.0'
    ],
    package_data = {
        'pythai': ['LICENSE.txt', 'README.md']
    },

    # metadata for upload to PyPI
    author = "Herman Schaaf",
    author_email = "herman.schaaf@gengo.com",
    description = "Python functions for working with the Thai language",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    license = "GNU",
    keywords = "thai language linguistics segmentation",
    url = "https://github.com/hermanschaaf/pythai",
    test_suite='pythai.tests',

    # could also include long_description, download_url, classifiers, etc.
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic'
    ]

)
