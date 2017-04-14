#-*- coding:utf-8 -*-
#mysetup.py  
from distutils.core import setup
import py2exe
options={'py2exe':{'compressed':1,
"optimize":2,
"bundle_files":3
}}
setup(
windows=['fivechesstest.py'],
options=options,
zipfile=None
      )
