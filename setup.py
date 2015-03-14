#!/usr/bin/env python
"""
    Jean-Lou Dupont's Command Line Tools
    
    Created on 2015-03-09
    @author: jldupont
"""
__author__  ="Jean-Lou Dupont"
__version__ ="0.2"

DESC="""
Overview
--------

Collection of command line tools

* jldcmd-jwrite: read JSON objects from stdin and write to target path
* jldcmd-wsniff: sniff beacon, probe request & response from a 802.11 interface, outputs JSON to stdout
"""


from distutils.core import setup
from setuptools import find_packages


setup(name=         'jldcmds',
      version=      __version__,
      description=  'Collection of command line tools',
      author=       __author__,
      author_email= 'jl@jldupont.com',
      url=          'https://github.com/jldupont/jldcmds',
      package_dir=  {'': "src",},
      packages=     find_packages("src"),
      scripts=      ['src/scripts/jldcmd-jwrite'
                     ,'src/scripts/jldcmd-wsniff'
                     ],
      zip_safe=False
      ,long_description=DESC
      ,install_requires=[ "argparse" 
                         ,'scapy'
                         ]
      )

#############################################

f=open("latest", "w")
f.write(str(__version__)+"\n")
f.close()

