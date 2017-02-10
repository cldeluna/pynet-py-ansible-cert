import sys
import os
i = 0
for folderName, subfolders, filenames in os.walk('c:\\'):
    print "The current folder is: " + folderName
    for subfolder in subfolders:
        print 'SUBFOLDER OF ' + folderName + ': ' + subfolder
        for filename in filenames:
            print 'FILE INSIDE ' + folderName + ': ' + filename
            print ' '
            i += 1
            if i == 20: sys.exit(15)