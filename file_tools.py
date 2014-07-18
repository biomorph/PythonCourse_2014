__author__ = 'ravi'
import sys
import os
import mimetypes
import gzip

def open_file_by_mimetype(file_name):
    if os.path.exists(file_name):
        if mimetypes.guess_type(file_name)[1] == 'gzip':
            return gzip.open(file_name,'r')
        else:
            return open(file_name,'r')
    else:
        sys.exit("File does not exist")
