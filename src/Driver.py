#!/usr/bin/env python

import sys
import time
import os
import getopt
import SMS
import OverallSMS
import SMSParser
import RPDUParser
import UDParser
import WSPParser
import WBXMLParser
import SIMCmdParser
import MMSParser
import EnvelopeParser
import Utils
import IniHandler


def usage():
    print "./Driver.py -i <input file> [-v verbose] [-V extra verbose] [-h THIS help]"

def doParse(parser, inputfile):
    if os.path.exists(inputfile):
        result = parser.parse(IniHandler.getIniData(inputfile))
        if not result:
            print "Error: parsing file %s: %s"%(inputfile, parser.myError)
            sys.exit()  
    else:
        print "Error: file could not be found for parsing: %s"%(inputfile)
        sys.exit()

def driver(inputfile):
    myOverallSMS = OverallSMS.OverallSMS()

    doParse(SMSParser.SMSParser(myOverallSMS), inputfile)

    if (len(myOverallSMS.myEnvelopeFile) > 0):
        doParse(EnvelopeParser.EnvelopeParser(myOverallSMS), myOverallSMS.myEnvelopeFile)

    if (len(myOverallSMS.myRPDUFile) > 0):
        doParse(RPDUParser.RPDUParser(myOverallSMS), myOverallSMS.myRPDUFile)

    if (len(myOverallSMS.myUDFile) > 0):
        doParse(UDParser.UDParser(myOverallSMS), myOverallSMS.myUDFile)
    
    if (len(myOverallSMS.myWSPFile) > 0):
        doParse(WSPParser.WSPParser(myOverallSMS), myOverallSMS.myWSPFile)

    if (len(myOverallSMS.myWBXMLFile) > 0):
        doParse(WBXMLParser.WBXMLParser(myOverallSMS), myOverallSMS.myWBXMLFile)

    if (len(myOverallSMS.mySIMCmdFile) > 0):
        doParse(SIMCmdParser.SIMCmdParser(myOverallSMS), myOverallSMS.mySIMCmdFile)

    if (len(myOverallSMS.myMMSFile) > 0):
        doParse(MMSParser.MMSParser(myOverallSMS), myOverallSMS.myMMSFile)

    return myOverallSMS

def main(argv):
    myOverallSMS = ""
    err = "Error: "

    verbosity = 0
    inputfile = ""

    try:
        opts, args = getopt.getopt(argv,"hVvi:")
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
        elif opt == '-v':
            verbosity = 1 
        elif opt == '-V':
            verbosity = 2   

    if (inputfile == ""):
        print "Error: no input file provided"
        usage()
        sys.exit()

    if not os.path.exists(inputfile):
        print "Error: could not find input file %s"%(inputfile)
        usage()
        sys.exit()

    myOverallSMS = driver(inputfile)

    print myOverallSMS.dump(verbosity)
    
if __name__ == "__main__":
    main(sys.argv[1:])
    sys.exit(0)



