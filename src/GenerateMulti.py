#!/usr/bin/env python

import sys
import os
import getopt
import random
import Driver
import Permutator
import IniHandler

sendertypes = ('SMSSUBMIT', 'OPENBTSINJ', 'SMSPPDL')
classtypes = ('REGTEXT', 'FLASHTEXT', 'CLASS2')

# print "2 supported types for OpenBTS injection: regular text multipart SMS & class 2 multipart SMS" 
# print "1 supported type for card reader: ENVELOPE APDU command with SMS-PP download of a multipart SMSes"


def usage():
    print ""
    print "Descripton:"
    print "This is a utility for generating all the parts in a multipart SMS."
    print ""
    print "Usage:"
    print "./GenerateMulti.py -n <int> [-s <str>] [-c <str>] [-x <int>] [-r] [-i <int>] [-v] [-h]"
    print ""
    print "Notes:"
    print "-n : number of parts (required, must be between 2 and 255, inclusive)" 
    print "-s : supported sender types (optional): " + str(sendertypes) + " where default='" + sendertypes[0] + "'"
    print "-c : supported class types (optional): " + str(classtypes) + " where default='" + classtypes[0] + "'"
    print "-x : number of parts to randomly exclude (optional, must be between 0 and 'n', inclusive)"
    print "-r : randomize part order (optional)"
    print "-i : random seed (optional)"
    print "-v : verbose (optional)"    
    print "-h : THIS help (optional)"


def main(argv):
    numberparts = 0
    verbose = False
    randomize = False
    excludecount = 0
    sendertype = sendertypes[0]
    classtype = classtypes[0]

    try:
        opts, args = getopt.getopt(argv,"hrvn:s:c:x:i:")
    except getopt.GetoptError:
        print "\nError: invalid argument given"
        usage()
        sys.exit()   

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
	elif opt == '-v':
	    verbose = True
        elif opt == '-r':
	    randomize = True
        elif opt == '-s':
            if arg in sendertypes:
                sendertype = arg
            else:
                print "\nError: invalid sender type given: %s"%(arg)
                usage()
                sys.exit(-1)
        elif opt == '-c':
            if arg in classtypes:
                classtype = arg
            else:
                print "\nError: invalid class type given: %s"%(arg)
                usage()
                sys.exit(-1)
        elif opt == '-i':
            try:
                random.seed(int(arg))
            except:
                print "\nError: invalid seed value given: %s"%(arg)
                usage()
                sys.exit(-1) 
        elif opt == '-x':
            try:
                excludecount = int(arg)
            except:
                print "\nError: invalid number of random parts to exclude given: %s"%(arg)
                usage()
                sys.exit(-1) 
        elif opt == '-n':
            try:
                numberparts = int(arg)
            except:
                print "\nError: invalid number of parts given: %s"%(arg)
                usage()
                sys.exit(-1) 

    if (numberparts < 2) or (numberparts > 255):
        print "\nError: %d is invalid: number of parts must be between 2 and 255 (inclusive)"%(numberparts)
        usage()
        sys.exit(-1)

    if (excludecount < 0) or (excludecount > numberparts):
        print "\nError: invalid number of random parts to exclude given: %d"%(excludecount)
        usage()
        sys.exit(-1) 

    generateMulti(numberparts, sendertype, classtype, excludecount, randomize, verbose)



def generateMulti(numberparts, sendertype, classtype, excludecount, randomize, verbose):

    byteoffset = -1
    senderdir = ""
    classdir = ""
    
    if sendertype == sendertypes[0]:
        senderdir = "sms_submit"
    elif sendertype == sendertypes[1]:
        senderdir = "openbts_injection"
        byteoffset = 31
    elif sendertype == sendertypes[2]:
        senderdir = "card_reader"
   
    if classtype == classtypes[0]:
        classdir = "multi_reg_text"
    elif classtype == classtypes[1]:
        classdir = "multi_flash_text"
    elif classtype == classtypes[2]:
        classdir = "class2"

    # Generate a hex string representation of numberparts variable.
    # Eg. if numberparts == 250, then nopartshexstr = 'FA'.
    # Eg. if numberparts == 7, then nopartshexstr = '07'.
    nopartshexstr = "%X" % numberparts
    if len(nopartshexstr) == 1:
	nopartshexstr = "0" + nopartshexstr

    ud_path = "sms/%s/%s/multitest/ud.ini"%(senderdir,classdir)
    sms_path = "sms/%s/%s/multitest/sms.ini"%(senderdir,classdir)

    if not os.path.isfile(ud_path):
        print "\nFatal error: file does not exist: ./%s"%(ud_path)
        sys.exit(-1) 
    
    if not os.path.isfile(sms_path):
        print "\nFatal error: file does not exist: ./%s"%(sms_path)
        sys.exit(-1) 

    # Update the test ud.ini file with the nopartshexstr (WARNING: ud.ini file is overwritten!).
    inihandler = IniHandler.IniHandler(ud_path)
    inihandler.update("DecodedIED", "00" + nopartshexstr + "FF")
    if not inihandler.dump(ud_path, True):
	print "\nFatal error: could not process: ./%s"%(ud_path)
        sys.exit(-1) 

    base_sms = Driver.driver(sms_path).dump(0)
    temp_list = Permutator.permutate(base_sms, byteoffset, 1, 1, numberparts, verbose)
  
    i = 1
    multipart_smses = []
    for temp in temp_list:
        multipart_smses.append([i, temp])
        i += 1

    if randomize:
        random.shuffle(multipart_smses)

    excludecountorg = excludecount
    while (excludecount > 0):
        curr_len = len(multipart_smses)
        multipart_smses.pop(random.randint(0, (curr_len - 1)))
        excludecount -= 1
    excludecount = excludecountorg

    if verbose:
        print ""
        print "SENDER TYPE: %s"%(sendertype)
        print "CLASS TYPE: %s"%(classtype)
        print "NUMBER OF PARTS: %d"%(numberparts)
        print "EXCLUDED PART COUNT: %d"%(excludecount)
        print "RANDOMIZE PART ORDER: %s"%(randomize)
    i = 1
    for multipart_sms in multipart_smses:
        if verbose:
            print ""
            print "PART %d of %d"%(multipart_sms[0], numberparts)
            i += 1
        print multipart_sms[1]


if __name__ == "__main__":
    main(sys.argv[1:])
    sys.exit(0)




    	



