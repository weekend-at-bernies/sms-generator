import Names
import Parser

class WSPParser(Parser.Parser):

	def __init__(self, overallSMS):
		self.myName = Names.Containers["WSP"]
		super(WSPParser, self).__init__(overallSMS)
		
	def parse(self, inputdata):
	    	    	    
	        for data in inputdata:

			if (data[0] == Names.WSP_parse["WSPTID"]):
				self.update([ Names.WSP["WSPTID"] ], Names.Common["ENCODED"], data[1])	

			elif (data[0] == Names.WSP_parse["WSPType"]):
				self.update([Names.WSP["WSPTYPE"]], Names.Common["ENCODED"], data[1])				

			elif (data[0] == Names.WSP_parse["GenWSPHL"]):
		    		if (data[1] == '1'):
					self.update([Names.WSP["WSPHL"]], Names.Common["NEEDSENCODING"], True)

			elif (data[0] == Names.WSP_parse["WSPHL"]):
				self.update([Names.WSP["WSPHL"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.WSP_parse["GenEncContType"]):
		    		if (data[1] == '1'):
					self.update([Names.WSP["WSPCONTTYPE"]], Names.Common["NEEDSENCODING"], True)
	       
			elif (data[0] == Names.WSP_parse["EncContType"]):
				self.update([Names.WSP["WSPCONTTYPE"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.WSP_parse["DecContType"]):
		    		self.update([Names.WSP["WSPCONTTYPE"]], Names.Common["DECODED"], data[1])

			elif (data[0] == Names.WSP_parse["GenEncHdrs"]):
		    		if (data[1] == '1'):
					self.update([Names.WSP["WSPHDRS"]], Names.Common["NEEDSENCODING"], True)
	       
			elif (data[0] == Names.WSP_parse["EncHdrs"]):
				self.update([Names.WSP["WSPHDRS"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.WSP_parse["DecHdrs"]):
		    		self.update([Names.WSP["WSPHDRS"]], Names.Common["DECODED"], data[1])
	       
			
	    		else:
				self.myError = "Unsupported field: " + data[0]
				return False
		return True

