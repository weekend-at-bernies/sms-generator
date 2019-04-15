import Names
import Parser

class EnvelopeParser(Parser.Parser):

	def __init__(self, overallSMS):
		self.myName = Names.Containers["ENVELOPE"]
		super(EnvelopeParser, self).__init__(overallSMS)
		
	def parse(self, inputdata):
	    	    	    
	        for data in inputdata:

			if (data[0] == Names.ENVELOPE_parse["CLA"]):
				self.update([Names.ENVELOPE["CLA"]], Names.Common["ENCODED"], data[1])	

			elif (data[0] == Names.ENVELOPE_parse["INS"]):
				self.update([Names.ENVELOPE["INS"]], Names.Common["ENCODED"], data[1])		

			elif (data[0] == Names.ENVELOPE_parse["P1"]):
				self.update([Names.ENVELOPE["P1"]], Names.Common["ENCODED"], data[1])	

			elif (data[0] == Names.ENVELOPE_parse["P2"]):
				self.update([Names.ENVELOPE["P2"]], Names.Common["ENCODED"], data[1])			

			elif (data[0] == Names.ENVELOPE_parse["GenLEN"]):
		    		if (data[1] == '1'):
					self.update([Names.ENVELOPE["LEN"]], Names.Common["NEEDSENCODING"], True)

			elif (data[0] == Names.ENVELOPE_parse["LEN"]):
				self.update([Names.ENVELOPE["LEN"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.ENVELOPE_parse["BERTLVTag"]):
				self.update([Names.ENVELOPE["BERTLV"], Names.ENVELOPE["BERTLVTAG"]], Names.Common["ENCODED"], data[1])
				
			elif (data[0] == Names.ENVELOPE_parse["GenBERTLVLen"]):
		    		if (data[1] == '1'):
					self.update([Names.ENVELOPE["BERTLV"], Names.ENVELOPE["BERTLVLEN"]], Names.Common["NEEDSENCODING"], True)					

			elif (data[0] == Names.ENVELOPE_parse["BERTLVLen"]):
				self.update([Names.ENVELOPE["BERTLV"], Names.ENVELOPE["BERTLVLEN"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.ENVELOPE_parse["GenSimpleTLVLen"]):
		    		if (data[1] == '1'):
					self.update([Names.ENVELOPE["SIMPLETLV"], Names.ENVELOPE["SIMPLETLVLEN"]], Names.Common["NEEDSENCODING"], True)
				# DO WE REALLY NEED THIS ELSE CONDITION???
				else:
					self.update([Names.ENVELOPE["SIMPLETLV"], Names.ENVELOPE["SIMPLETLVLEN"]], Names.Common["NEEDSENCODING"], False)

			elif (data[0] == Names.ENVELOPE_parse["SimpleTLVLen"]):
				self.update([Names.ENVELOPE["SIMPLETLV"], Names.ENVELOPE["SIMPLETLVLEN"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.ENVELOPE_parse["SimpleTLVTag"]):
				self.update([Names.ENVELOPE["SIMPLETLV"], Names.ENVELOPE["SIMPLETLVTAG"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.ENVELOPE_parse["SimpleTLVVal"]):
		    		self.update([Names.ENVELOPE["SIMPLETLV"], Names.ENVELOPE["SIMPLETLVVAL"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.ENVELOPE_parse["LastSimpleTLVLenFlag"]):
		    		if (data[1] == '1'):
					self.update("", Names.ENVELOPE["LASTSIMPLETLVLENFLAG"], True)	

	    		else:
				self.myError = "Unsupported field: " + data[0]
				return False
		return True

