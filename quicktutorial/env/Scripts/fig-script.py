#!C:\projects\quicktutorial\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'fig==1.0.1','console_scripts','fig'
__requires__ = 'fig==1.0.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('fig==1.0.1', 'console_scripts', 'fig')()
    )
