#!D:\projects\quicktutorial\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'secret==0.6.0','console_scripts','secret'
__requires__ = 'secret==0.6.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('secret==0.6.0', 'console_scripts', 'secret')()
    )
