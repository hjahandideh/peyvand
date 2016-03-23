#!c:\projects\quicktutorial\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'shootout','console_scripts','initialize_shootout_db'
__requires__ = 'shootout'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('shootout', 'console_scripts', 'initialize_shootout_db')()
    )
