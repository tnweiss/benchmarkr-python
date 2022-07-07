#!/usr/bin/env python

from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
      name='benchmarkr',
      version='0.0.1',
      description='Python benchmarking tool',
      author='Tyler Weiss',
      author_email='apps@tylerweiss.dev',
      url='https://github.com/tnweiss/benchmarkr-python',
      packages=['benchmarkr'],
      requires=[]
)
