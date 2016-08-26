#!/usr/bin/env python

from setuptools import setup

setup(name='moves',
      version='0.1.1',
      description='Moves Client API',
      author='Derek Arnold, Matt Greenwood',
      author_email='matt@thegreenwoods.org',
      url='https://github.com/mig2/moves',
      download_url='http://github.com/mig2/moves/archive/v0.1.1.tar.gz',
      packages=['moves3'],
      install_requires=open('requirements.txt').read(),
      long_description=open('README.md').read(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.5',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      license='MIT'
      )
