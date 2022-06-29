# Written By: Nick Evans
# Purpose: Lightweight script to append timestamp to the beginning of .xisf image files to enable pixinsight blink tool to load images in the correct order.
# Usage: Either 
# 1) place this script in the directory with your .xisf files you wish to rename, and run it or 
# 2) run this script from commandline with argument to the path to where the files are. Example: $ python3 timestamp_files.py /c/images/

import time
import os
from pathlib import Path
import sys

## Get Path to process
if(sys.argv[1] != ""):
    # get path via command line argument
    path = Path(sys.argv[1])
else:
    # get path from where the script is ran from
    path = Path(os.getcwd())

### Insert path validation code / error catching here...

# Update user
print('------------------------------------')
print('Input path = ', path)
print('Detected %s files. Processing... ' %len(os.listdir(path)))
print('------------------------------------')

# Process Files
for x in os.listdir(path):
    if x.endswith(".xisf"): #could update with different file extension - perhaps via another argument
        f_path = os.path.join(path, x)

        # Obtaining the modified time (in seconds) of the file/folder
        t = os.path.getmtime(f_path)
                
        # Converting the time to an epoch string
        t_str = time.ctime(t)
        
        # Converting the string to a time object
        t_obj = time.strptime(t_str)
        
        # Transforming the time object to a timestamp to ISO 8601 format
        form_t = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
        
        # Modified Letter Colon " " (U+A789)
        form_t = form_t.replace(":", "꞉")
        
        # Renaming the filename to its timestamp
        os.rename(f_path, os.path.split(f_path)[0] + '/' + form_t +'_'+ x)
        print(os.path.split(f_path)[0] + '/' + form_t +'_'+ x) #+ os.path.splitext(f_path)[1]) # for the extension
print('------------------------------------')
print('Processing Complete.')


