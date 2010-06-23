# -*- coding: utf-8 -*-
'''
Created on 9 févr. 2010

@author: tle
'''
import platform

if platform.system() == 'Linux':
    print 'This system isn\'t supported'
    
elif platform.system() == 'Darwin':
    """
    This is a setup.py script generated by py2applet
    
    Usage:
        python setup.py py2app
    """
    
    from setuptools import setup
    
    APP = ['__init__.py']
    DATA_FILES = ['../db']
    OPTIONS = {'argv_emulation': True, 'includes': ['sip','PyQt4'], 'packages': ['gui','base']}
    
    setup(
        name='PySSH Manager',
        app=APP,
        data_files=DATA_FILES,
        options={'py2app': OPTIONS},
        setup_requires=['py2app'],
    )
    
elif platform.system() == 'Windows':
    from py2exe.build_exe import py2exe
    from distutils.core import setup
    
    setup(
        name='PySSH Manager',
        windows=[{'script' : '../src/__init__.py', 'icon_resources' : [(1, '../compilers/Diagram.ico')]}],
        options={'py2exe' : {'includes' : ['sip'], 'optimize': 2, 'bundle_files': 1, 'compressed': True}},
        zipfile = None,
    )