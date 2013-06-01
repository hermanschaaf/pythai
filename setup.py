from distutils.core import setup
from distutils.core import Command, Extension
import os
import sys
# from setuptools import setup, find_packages
from subprocess import call

class Pep8Command(Command):
    description = "Run pep8 script"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            import pep8
            pep8
        except ImportError:
            print ('Missing "pep8" library. You can install it using pip: '
                   'pip install pep8')
            sys.exit(1)

        cwd = os.getcwd()
        retcode = call(("pep8 %s/pythai/ --exclude=vendor --ignore=E501" % (cwd)).split(' '))
        sys.exit(retcode)

class TestCommand(Command):
    description = "Run tests"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        errno = subprocess.call(['nosetests'])
        raise SystemExit(errno)

setup(
    name="pythai",
    version="0.1.3",
    packages=['pythai'],

    ext_modules=[ 
        Extension("libthai", 
                  ["pythai/libthai.c"],
                  libraries=['thai'])],

    # Required repositories
    # install_requires=[
    #     'argparse==1.2.1',
    #     'nose==1.3.0',
    #     'wsgiref==0.1.2'
    # ],
    package_data = {
        'pythai': ['LICENSE.txt', 'README.md']
    },

    # metadata for upload to PyPI
    author = "Herman Schaaf",
    author_email = "herman.schaaf@gengo.com",
    description = "Python functions for working with the Thai language",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    cmdclass={
        'pep8': Pep8Command,
        'test': TestCommand,
    },
    license = "GNU",
    keywords = "thai language linguistics segmentation",
    url = "https://github.com/hermanschaaf/pythai",

    # could also include long_description, download_url, classifiers, etc.
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic'
    ]

)
