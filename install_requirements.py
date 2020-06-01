import subprocess
import sys
import os
import importlib
import contextlib

def install(package):
    '''installs the package using pip'''
    subprocess.call([sys.executable,'-m','pip','install',package])


required = ['pygame','tkinter']

if len(required)>0:
    print('[Input] You are about to install',len(required),'Packages, would you like to procees (y/n)?')
    ans = input()

    if ans.lower() == 'y':
        for package in required:
            try:
                print('[Log] Looking for',package)
                with contextlib.redirect_stdout(None):
                    __import__(package)

                print('[Log]',package,'already installed ... ')
            except ImportError:
                print('[Log]',package,'not installed.')
                try:
                    print('[Log] Installing',package)
                    install(package)
                    with contextlib.redirect_stdout(None):
                        __import__(package)
                except Exception as e:
                    print('[ERROR] Could not install',package,'-',e)
                    
