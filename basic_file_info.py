#!/usr/bin/env python3

import sys
import os
import stat
import time

if len(sys.argv) < 2:
    print("Please use 1 aruguement(filez location)")
elif len(sys.argv) == 2: 

    name = sys.argv[1]

    print("filez Name : <{}>".format(os.path.basename(name)))
    print("filez Size : {} bytes".format(os.path.getsize(name)))
    print("Inode : {}".format(os.lstat(name)[stat.ST_INO]))
    print("Last Mod : {}".format(time.ctime(os.path.getmtime(name))))
else: 
    print("Please use proper number of arguments - 1")
