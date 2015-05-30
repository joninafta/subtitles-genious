# -*- coding: utf-8 -*-
"""
Created on Wed May 27 23:12:02 2015

@author: Jonathan
"""

#!/usr/bin/env python
 
import os
import sys
import time

def convert_to_utf8(path):
    # gather the encodings you think that the file may be
    # encoded inside a tuple
    #encodings =  ('cp1255', 'iso8859_8', 'cp424', 'cp856', 'cp862')
    encodings =  ('iso8859_8', 'cp424', 'cp856', 'cp862')
        
    filenames = next(os.walk(path))[2]
           
    for filename in filenames:
        
        if filename.find('he.srt') == -1:
            continue
        # try to open the file and exit if some IOError occurs
        f = open(path+filename, 'r').read()
        
        # now start iterating in our encodings tuple and try to
        # decode the file
        for enc in encodings:
            try:
                # try to decode the file with the first encoding
                # from the tuple.
                # if it succeeds then it will reach break, so we
                # will be out of the loop (something we want on
                # success).
                # the data variable will hold our decoded text                
                data = f.decode(enc)
                print filename + ' is encoded with ' + enc
                break
            except Exception:
                # if the first encoding fail, then with the continue
                # keyword will start again with the second encoding
                # from the tuple an so on.... until it succeeds.
                # if for some reason it reaches the last encoding of
                # our tuple without success, then exit the program.
                if enc == encodings[-1]:
                    sys.exit(1)
                continue
     
        # now get the absolute path of our filename and append .bak
        # to the end of it (for our backup file)
        newfilename=filename.replace('.he','')        
        # and at last convert it to utf-8
        f = open(path+newfilename, 'w')
        try:
            f.write(data.encode('utf-8'))
            os.remove(path+filename)
        except Exception, e:
            print e
        finally:
            f.close()

print ('enter requested directory:')
dirInput=raw_input()
convert_to_utf8(dirInput+"\\")
print 'finished ...'
time.sleep(5)