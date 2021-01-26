#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyrnr',
    packages=['pyrnr'],

    version='0.0.1',

    license='MIT',

    install_requires=['opencv-python'],

    author='wataridori2010',
    author_email='wataridori2010@gmail.com',

    url='https://github.com/wataridori2010/pyrnr',

    description='This library performs pyramidal (i.e. multi-scales) image noise reduction.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='pyrnr, multi-scale, nr, denoise',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)