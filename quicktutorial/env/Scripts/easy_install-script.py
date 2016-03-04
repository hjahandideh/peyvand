#!c:\projects\quicktutorial\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools','console_scripts','easy_install'
__requires__ = 'setuptools'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('setuptools', 'console_scripts', 'easy_install')()
    )
