# Setup file for comictagger python source  (no wheels yet)
#
# An entry point script called "comictagger" will be created
#
# Currently commented out, an experiment at desktop integration.
# It seems that post installation tweaks are broken by wheel files.
# Kept here for further research

from __future__ import print_function
from setuptools import setup
from setuptools import dist
from setuptools import Command
import setuptools.command.build_py 
import setuptools.command.install
import subprocess
import os
import sys
import shutil
import platform
import tempfile
import comictaggerlib.ctversion

python_requires='>=3',


with open('requirements.txt') as f:
    required = f.read().splitlines()

platform_data_files = []


class BuildPyCommand(setuptools.command.build_py.build_py):
  """Custom build command."""

  def run(self):
    setuptools.command.build_py.build_py.run(self)
            
class customInstall(setuptools.command.install.install):
  """Custom install command."""

  def run(self):
    
    # Do the standard install
    setuptools.command.install.install.run(self)
    
    # Custom post install 
    #postInstall(self.install_scripts)
    
#----------------------------------------------------    
setup(name="comictagger",
      install_requires=required,
      cmdclass={
        'build_py': BuildPyCommand,
        'install': customInstall,
        },
      version=comictaggerlib.ctversion.version,
      description="A cross-platform GUI/CLI app for writing metadata to comic archives",
      author="ComicTagger team",
      author_email="comictagger@gmail.com",
      url="https://github.com/davide-romanini/comictagger",
      download_url="https://pypi.python.org/packages/source/c/comictagger/comictagger-{0}.zip".format(comictaggerlib.ctversion.version),
      packages=["comictaggerlib", "comicapi"],
      package_data={
          'comictaggerlib': ['*.so'],
      },
      entry_points=dict(console_scripts=['comictagger=comictaggerlib.main:ctmain']),
      data_files=platform_data_files,
      classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Environment :: Win32 (MS Windows)",
            "Environment :: MacOS X",
            "Intended Audience :: End Users/Desktop",
            "License :: OSI Approved :: Apache Software License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Topic :: Utilities",
            "Topic :: Other/Nonlisted Topic",
            "Topic :: Multimedia :: Graphics"
      ],
      keywords=['comictagger', 'comics', 'comic', 'metadata', 'tagging', 'tagger'],
      license="Apache License 2.0",

      long_description="""
ComicTagger is a multi-platform app for writing metadata to digital comics, written in Python and PyQt.

Features:

* Runs on Mac OSX, Microsoft Windows, and Linux systems
* Communicates with an online database (Comic Vine) for acquiring metadata
* Uses image processing to automatically match a given archive with the correct issue data
* Batch processing in the GUI for tagging hundreds or more comics at a time
* Reads and writes multiple tagging schemes ( ComicBookLover and ComicRack).
* Reads and writes RAR and Zip archives (external tools needed for writing RAR)
* Command line interface (CLI) on all platforms (including Windows), which supports batch operations, and which can be used in native scripts for complex operations.
"""
      )
