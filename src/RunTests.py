#!/usr/bin/env python

import filecmp
import subprocess
import sys

def main(argv):
    i = 1
    numtests = int(argv)
    while i <= numtests:
	f = open("currtest%d.out"%i, "w")
	subprocess.call(["python", "Driver.py", "-i", "sms/test/test%d/sms.ini"%i], stdout=f)
	if (filecmp.cmp("currtest%d.out"%i, "sms/test/test%d/test%d.out"%(i, i)) == False):
	    print("Test %d failure..."%(i))
        else:
            print("Test %d success..."%(i))	
        subprocess.call(["rm", "currtest%d.out"%i])
	i = i + 1
	f.close()
	

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        main(sys.argv[1])
    else:
	print("Usage: ./RunTests.py <num of tests>")
    sys.exit(0)

