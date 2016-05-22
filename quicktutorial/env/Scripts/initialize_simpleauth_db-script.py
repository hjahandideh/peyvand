#!d:\projects\quicktutorial\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'simpleauth','console_scripts','initialize_simpleauth_db'
__requires__ = 'simpleauth'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('simpleauth', 'console_scripts', 'initialize_simpleauth_db')()
    )
