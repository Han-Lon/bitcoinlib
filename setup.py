# -*- coding: utf-8 -*-
#
#    bitcoinlib - Compact Python Bitcoin Library
#    PyPi Setup Tool
#    © 2016 December - 1200 Web Development <http://1200wd.com/>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    readmetxt = f.read()

setup(
      name='bitcoinlib',
      version='0.3.0.10',
      description='Bitcoin and Other cryptocurrency Library',
      long_description=readmetxt,
      classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Intended Audience :: Developers',
            'Intended Audience :: Financial and Insurance Industry',
            'Intended Audience :: Information Technology',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Security :: Cryptography',
            'Topic :: Office/Business :: Financial :: Accounting',
      ],
      url='http://github.com/1200wd/bitcoinlib',
      author='1200wd',
      author_email='info@1200wd.com',
      license='GNU3',
      packages=['bitcoinlib'],
      test_suite= 'tests',
      install_requires=[
            'requests',
            'ecdsa',
            'pbkdf2',
            'pycrypto',
            'scrypt',
            'sqlalchemy',
      ],
      include_package_data=True,
      keywords='bitcoin library cryptocurrency tools wallet crypto keys',
      zip_safe=False
)