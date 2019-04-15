import sys
import binascii
import subprocess
import os

# Suppose s: "foo", i1: 3, i2: 5, target: "foo2".
# This would return false
# If target: "foo3" or "foo4", this would return true. 
def inRange(s1, i1, i2, target):
	s1_l = len(s1)
	try:
		s2 = target[:s1_l]
		if (s1 == s2):
			s3 = target[s1_l:]
			if int(s3) >= i1:
				if int(s3) <= i2:
					return (True, int(s3))		
	except Exception:
		pass
	return (False, -1)
	
def getDash(count):
	s = ""
	i = 0
	while (i < count):
		s += "-"
		i += 1
	return s

def addIndent(s, count):
	i = 0
	while (i < count):
		s = " " + s
		i += 1
	return s

def toSeptetCount(octetCount):
	return ((octetCount * 8) / 7)

def encodeNumber(data):                 
	leng = len(data) / 2 + (len(data) % 2)
	outno = ""
	outno_dec = ""
	c = 0
	for i in range(0, len(data)):
		if (i % 2 == 1):
			c = c | ((ord(data[i]) - 48) << 4)
			outno = outno + chr(c)
			c = 0
		else:
			c = c | (ord(data[i]) - 48)
			if i == len(data) - 1:
				c = c | 0xF0
				outno = outno + chr(c)	
	
	for i in range(0, leng):
	        outno_dec += "%0.2X" % ord(outno[i])
	return outno_dec

def encode7bit(data,headerlen=0):
    string = data
 
    """ Pack a string of 7-bit characters into an 8-bit using the funky 7bit
    septets transformation.

    Account for the header length (in octets): if the header doesn't finish
    on a septet boundary we need to pack it out (see unpack7bit for more
    info).

    Return the number of septets (even partial, so include the leading
    crap) and the packet string.

    See URL above for an example.
    """
    n = 0
    num_septets = len(string)

    # determine starting bit to output at
    if headerlen:
        # need to find the next multiple of 7 up from the current header
        # length
        cur = 8 * headerlen
        if cur % 7:
            n = 7 - (cur / 7) % 7
        num_septets = len(string) + 1
        #print 'header length', headerlen, 'starts at', cur, 'and mod is', n

    # pack all those pesky septets into one big number
    bignum = 0
    for c in string:
        septet = ord(c)
        bignum |= septet << n
        n += 7

    # now grab octets from that big number, starting from the bottom
    #print format(bignum, 'b')
    m = 0
    l = []
    while n > 0:
        mask = 0xFF << m
        l.append((bignum & mask) >> m)
        #print format(l[-1], '08b')
        m += 8
        n -= 8

 #   return num_septets, ''.join(map(chr, l))
 #   return ''.join(map(chr, l))
    out = ""
    for i in l:
	out += "%02X" % i
    return out



def xml2wbxml(inputfile, version):
    try:
        import pywbxml
        return xml2wbxml_using_pywbxml(inputfile, version)
    except ImportError:
        return xml2wbxml_using_wbxml(inputfile, version)



# Caller must ensure 'inputfile' exists!
# No version support. Every WBXML output is version 1.0!
def xml2wbxml_using_pywbxml(inputfile, version):      
    #try:
    #    import pywbxml
    #except ImportError:
    #    print "Error: cannot import pywbxml module (is it installed?)"
    #    sys.exit(-1)

    # For Ubuntu 10.04 LTS:
    # $ sudo apt-get install libwbxml2-0 python-wbxml
    import pywbxml

    file = open(inputfile, 'r')
    lines = file.readlines()
    file.close()
    myxml = ""
    for line in lines:
        myxml += line
    mywbxml = pywbxml.xml2wbxml(myxml)		
    return binascii.b2a_hex(mywbxml).upper()

# Caller must ensure 'inputfile' exists!
def xml2wbxml_using_wbxml(inputfile, version):   
    #try:
    #    import wbxml
	#except ImportError:
      #  print "Error: cannot import pywbxml module (is it installed?)"
    #    print "Error: cannot import wbxml module (is it installed?)"
    #    sys.exit(-1)
		#nulldev = open(os.devnull, 'w')		
		# Redirect 'xml2wbxml' output to /dev/null otherwise it will produce output!
		#subprocess.call(["xml2wbxml", "-v", "%s"%version, "-o", "mywbxml.tmp", inputfile], stdout=nulldev, stderr=nulldev)				
		#f = open("mywbxml.tmp", 'rb')
    		#blob = f.read()
		#f.close()
		#subprocess.call(["rm", "mywbxml.tmp"])
		#return binascii.b2a_hex(blob).upper()


    # For Ubuntu > 10.04 LTS
    # REFER : https://pypi.org/project/wbxml/
    # $ sudo apt-get install libwbxml2-dev libwbxml2-0
    import wbxml

    file = open(inputfile, 'r')
    lines = file.readlines()
    file.close()
    myxml = ""
    for line in lines:
        myxml += line
    #print binascii.b2a_hex(wbxml.xml_to_wbxml(myxml)).upper()
    return binascii.b2a_hex(wbxml.xml_to_wbxml(myxml)).upper()


