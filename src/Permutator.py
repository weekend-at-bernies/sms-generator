#!/usr/bin/env python

import sys
import time
import os
import getopt
import string

def getInputData(inputfile):
    if (os.path.exists(inputfile) == False):
        return ""

    f = open(inputfile, 'r')
    line = f.readline().strip(' \t\n\r')
    f.close()

    if len(line) % 2 != 0:
        return ""
    
    if all(c in string.hexdigits for c in line) == False:
        return ""

    return line


# 'hexstr' : an even length string in form eg. "A45FF007". CALLER MUST SANITIZE
# 'bindex' :  byte index. CALLER MUST SANITIZE
# 'blen' : byte length. No sanitization required. If too large, will be auto cut off to max value
# 'minval' : min val (inclusive). values smaller will be ignored. CALLER MUST SANITIZE. < 0 special case: see below
# 'maxval' : max val (inclusive). values greater will be ignored. CALLER MUST SANITIZE. < 0 special case: see below
# < 0 special case : if < 0, then IGNORE min/max val
# Example: permutate(0xA45FF007, 1, 2, 1, 3, False) will return:
# A4000107
# A4000207
# A4000307
def permutate(hexstr, bindex, blen, minval=-1, maxval=-1, debug=False):
    cindex = bindex * 2
    lcstr = len(hexstr)
    lbstr = lcstr / 2
    havemin = True
    havemax = True
    variants = []

    if minval < 0:
	havemin = False
    if maxval < 0:
	havemax = False
  
    if ((bindex + blen) > lbstr):
        modblen = lbstr - bindex
    else:
        modblen = blen

    part1 = ""
    part2 = ""
    part3 = ""

    part1 = hexstr[:cindex]
    part2 = hexstr[cindex:cindex+(modblen*2)]
    if ((bindex + blen) < lbstr):
        part3 = hexstr[cindex+(modblen*2):]

    randpart2 = ""
    i1 = 0
    imax = 2 ** (len(part2) * 4)
    while i1 < imax:
        randpart2 = "%X"%(i1)
	lcrandpart2 = len(randpart2)
        if lcrandpart2 < (modblen*2):
            i2 = 0
            while (i2 < ((modblen*2) - lcrandpart2)):
                randpart2 = "0" + randpart2
                i2 += 1       
	i1 += 1
	if havemin and (i1 - 1) < minval:
	    continue
        if havemax and (i1 - 1) > maxval:
            continue	
	if debug == True:
            variants.append(part1 + " [ " + randpart2 + " ] " + part3)	    
        else:
            variants.append(part1 + randpart2 + part3)
    return variants


def usage():
    print "./Permutator.py -i <input file> -b <byte index> [-l <length>] [-y <min val>] [-x <max val>] [-d <debug>] [-h THIS help]"

def main(argv):

    inputfile = ""
    byteindex = -1
    bytelength = 1
    debug = False
    minval = -1
    maxval = -1

    try:
        opts, args = getopt.getopt(argv,"hdl:i:b:x:y:")
    except getopt.GetoptError:
        print "Error: invalid argument"
        usage()
        sys.exit()   

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt == '-i':
            inputfile = arg
	elif opt == '-d':
	    debug = True
        elif opt == '-l':
            try:
                bytelength = int(arg)
            except:
                print "Error: invalid length value"
                usage()
                sys.exit(-1)
        elif opt == '-b':
            try:
                byteindex = int(arg)
	    except:
                print "Error: invalid byte index value"
                usage()
                sys.exit(-1)    
	elif opt == '-x':
	    try:
                maxval = int(arg)
	    except:
                print "Error: invalid max value"
                usage()
                sys.exit(-1) 
	elif opt == '-y':
	    try:
                minval = int(arg)
	    except:
                print "Error: invalid min value"
                usage()
                sys.exit(-1) 

    if (inputfile == ""):
        print "Error: no input file provided"
        usage()
        sys.exit(-1)

    if (byteindex < 0):
        print "Error: invalid or no byte index provided"
        usage()
        sys.exit(-1)

    if (bytelength < 1):
        print "Error: invalid length value"
        usage()
        sys.exit(-1)

    targetStr = getInputData(inputfile)
    if len(targetStr) == 0:
        print "Error: input file contains invalid data"
        usage()
        sys.exit(-1)

    if (byteindex >= (len(targetStr) / 2)):
        print "Error: byte index %d too large"%(byteindex)
        usage()
        sys.exit(-1)

    variants = permutate(targetStr, byteindex, bytelength, minval, maxval, debug)
    for variant in variants:
	print variant

    	
if __name__ == "__main__":
    main(sys.argv[1:])
    sys.exit(0)



