#!/usr/bin/env python

import os
import sys
import optparse
import string
import random

import GenerateMulti
import IniHandler

sendertypes = ('SMSSUBMIT', 'OPENBTSINJ', 'SMSPPDL')
classtypes = ('REGTEXT', 'FLASHTEXT')


def main(argv):
    setcount = 0
    partcount = 0
    randomize1 = False
    randomize2 = False
    randomize3 = False
    verbose = False
    sendertype = sendertypes[0]
    classtype = classtypes[0]

    parser = optparse.OptionParser()
    parser.add_option("--n1", help="number of sets (required; minimum 1)", dest="setcount", metavar="<int>")
    parser.add_option("--n2", help="number of parts per set (required otherwise ignored if -r1 specified; must be between 2 and 255, inclusive)", dest="partcount", metavar="<int>")
    parser.add_option("--r1", help="randomize number of parts per set (optional, otherwise tramples -n2 if set)", dest="randomize1", action="store_true")
    parser.add_option("--r2", help="randomize order of parts inside each set (optional)", dest="randomize2", action="store_true")
    parser.add_option("--r3", help="randomize order of sets (optional)", dest="randomize3", action="store_true")
    parser.add_option("-s", help="sender type (optional; first in list is default)", dest="sendertype", metavar=str(sendertypes))
    parser.add_option("-c", help="class type (optional; first in list is default)", dest="classtype", metavar=str(classtypes))
    parser.add_option("-i", help="random seed", dest="seed", metavar="<int>")
    parser.add_option("-v", help="verbose", dest="verbose", action="store_true")
    (opts, args) = parser.parse_args()

    if opts.sendertype is not None:
        if opts.sendertype in sendertypes:
            sendertype = opts.sendertype
        else:
            print "\nError: invalid sender type given: %s"%(opts.sendertype)
            parser.print_help()
            sys.exit(-1) 

    if opts.classtype is not None:
        if opts.classtype in classtypes:
            classtype = opts.classtype
        else:
            print "\nError: invalid class type given: %s"%(opts.classtype)
            parser.print_help()
            sys.exit(-1) 

 
    if opts.randomize1 is not None:
        randomize1 = opts.randomize1

    if opts.randomize2 is not None:
        randomize2 = opts.randomize2

    if opts.randomize3 is not None:
        randomize3 = opts.randomize3

    if opts.verbose is not None:
        verbose = opts.verbose

    if opts.seed is not None:
        try:
            random.seed(int(opts.seed))
        except:
            print "\nError: invalid seed value given: %s"%(opts.seed)
            parser.print_help()
            sys.exit(-1) 

    try:
        setcount = int(opts.setcount)
    except:
        print "\nError: invalid number of sets given: %s"%(opts.setcount)
        parser.print_help()
        sys.exit(-1) 

    if not randomize1:
        try:
            partcount = int(opts.partcount)
        except:
            print "\nError: invalid number of multiparts given: %s"%(arg)
            parser.print_help()
            sys.exit(-1) 



    if (opts.setcount < 1):
        print "\nError: %d is invalid: number of sets must be >= 1"%(opts.setcount)
        usage()
        sys.exit(-1)

    if not randomize1:
        if (partcount < 2) or (partcount > 255):
            print "\nError: %d is invalid: number of multiparts must be between 2 and 255 (inclusive)"%(partcount)
            usage()
            sys.exit(-1)

    generateMultiTextSets(setcount, partcount, randomize1, randomize2, randomize3, sendertype, classtype, verbose)



def generateMultiTextSets(setcount, partcount, randomize1, randomize2, randomize3, sendertype, classtype, verbose):

    senderdir = ""
    classdir = ""
    currpartcount = 0
    
    if sendertype == sendertypes[0]:
        senderdir = "sms_submit"
    elif sendertype == sendertypes[1]:
        senderdir = "openbts_injection"
    elif sendertype == sendertypes[2]:
        senderdir = "card_reader"
   
    if classtype == classtypes[0]:
        classdir = "multi_reg_text"
    elif classtype == classtypes[1]:
        classdir = "multi_flash_text"

    ud_path = "sms/%s/%s/multitest/ud.ini"%(senderdir,classdir)
    sms_path = "sms/%s/%s/multitest/sms.ini"%(senderdir,classdir)

    if not os.path.isfile(ud_path):
        print "\nFatal error: file does not exist: ./%s"%(ud_path)
        sys.exit(-1) 
    
    if not os.path.isfile(sms_path):
        print "\nFatal error: file does not exist: ./%s"%(sms_path)
        sys.exit(-1) 

    for i in range(0, setcount):
        
        if randomize1:
            currpartcount = random.randint(2, 255)
        else:
            currpartcount = partcount

        # Update the test ud.ini file with randomized text (WARNING: ud.ini file is overwritten!).
        inihandler = IniHandler.IniHandler(ud_path)
        #inihandler.update("DecodedUD", generateRandomStr(153))       <--- pure random characters 
        # we do this so we know where the part ends:
        inihandler.update("DecodedUD", (generateRandomStr(151) + " X"))
        if not inihandler.dump(ud_path, True):
	    print "\nFatal error: could not process: ./%s"%(ud_path)
            sys.exit(-1) 

        if verbose:
            print ""
            print "--------------------------------------------------------------------------"
            print "SET %d of %d"%((i + 1), setcount)
        GenerateMulti.generateMulti(currpartcount, sendertype, classtype, 0, randomize2, verbose)
       

def generateRandomStr(length):
    return ''.join(random.SystemRandom().choice(string.letters + string.digits) for _ in range(length))
   # return ''.join(random.SystemRandom().choice(string.letters + string.digits) for _ in range(length))


    	
if __name__ == "__main__":
    main(sys.argv[1:])
    sys.exit(0)



