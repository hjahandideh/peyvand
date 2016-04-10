#!d:\projects\quicktutorial\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'mako','console_scripts','mako-render'
__requires__ = 'mako'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('mako', 'console_scripts', 'mako-render')()
    )
