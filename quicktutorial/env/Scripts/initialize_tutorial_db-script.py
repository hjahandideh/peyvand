#!c:\projects\quicktutorial\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'tutorial','console_scripts','initialize_tutorial_db'
__requires__ = 'tutorial'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('tutorial', 'console_scripts', 'initialize_tutorial_db')()
    )
