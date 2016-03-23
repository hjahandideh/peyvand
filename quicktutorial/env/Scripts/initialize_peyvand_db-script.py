#!c:\projects\quicktutorial\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'peyvand','console_scripts','initialize_peyvand_db'
__requires__ = 'peyvand'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('peyvand', 'console_scripts', 'initialize_peyvand_db')()
    )
