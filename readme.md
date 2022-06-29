# timestamp_files utility

## Purpose 
Lightweight script to append timestamp to the beginning of .xisf image files to enable pixinsight blink tool to load images in the correct order.

## Usage
Two options to run it:
1) Place this script in the directory with your .xisf files, and run it or 
2) Run this script from commandline with argument to the path to where the files are. 

Example: 
```
$ python3 timestamp_files.py /c/images/
```

## Requirements
python3

## Developer Notes
- Doesn't detect if files had been timestamped before.
- Unknown what happens if trying to append to a filename with > 255 characters
- Could be used for .jpg files, or any file extension