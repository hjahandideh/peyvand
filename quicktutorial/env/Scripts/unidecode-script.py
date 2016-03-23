#!c:\projects\quicktutorial\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'unidecode','console_scripts','unidecode'
__requires__ = 'unidecode'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('unidecode', 'console_scripts', 'unidecode')()
    )
