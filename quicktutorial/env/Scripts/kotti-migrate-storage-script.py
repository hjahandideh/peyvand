#!c:\projects\quicktutorial\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Kotti','console_scripts','kotti-migrate-storage'
__requires__ = 'Kotti'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('Kotti', 'console_scripts', 'kotti-migrate-storage')()
    )
