#!C:\projects\quicktutorial\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pygments','console_scripts','pygmentize'
__requires__ = 'pygments'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pygments', 'console_scripts', 'pygmentize')()
    )
