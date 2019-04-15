import Names
import Parser

class UDParser(Parser.Parser):

	def __init__(self, overallSMS):
		self.myName = Names.Containers["UD"]
		super(UDParser, self).__init__(overallSMS)
		
	def parse(self, inputdata):

		decodedUD = ""
	    	    	    
	        for data in inputdata:

			if (data[0] == Names.UD_parse["GenUDL"]):
		    		if (data[1] == '1'):
					self.update([Names.UD["UDL"]], Names.Common["NEEDSENCODING"], True)

			elif (data[0] == Names.UD_parse["UDL"]):
				self.update([Names.UD["UDL"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.UD_parse["GenEncUD"]):
		    		if (data[1] == '1'):
					self.update([Names.UD["USRDATA"]], Names.Common["NEEDSENCODING"], True)
	       
			elif (data[0] == Names.UD_parse["EncUD"]):
				self.update([Names.UD["USRDATA"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.UD_parse["DecUD"]):
		    		self.update([Names.UD["USRDATA"]], Names.Common["DECODED"], data[1])

			elif (data[0] == Names.UD_parse["GenUDHL"]):
		    		if (data[1] == '1'):
					self.update([Names.UD["UDHL"]], Names.Common["NEEDSENCODING"], True)

			elif (data[0] == Names.UD_parse["UDHL"]):
				self.update([Names.UD["UDHL"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.UD_parse["GenIELen"]):
		    		if (data[1] == '1'):
					self.update([Names.UD["IE"], Names.UD["IELEN"]], Names.Common["NEEDSENCODING"], True)
				# DO WE REALLY NEED THIS ELSE CONDITION???
				else:
					self.update([Names.UD["IE"], Names.UD["IELEN"]], Names.Common["NEEDSENCODING"], False)

			elif (data[0] == Names.UD_parse["IELen"]):
				self.update([Names.UD["IE"], Names.UD["IELEN"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.UD_parse["IEType"]):
				self.update([Names.UD["IE"], Names.UD["IETYPE"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.UD_parse["GenEncIED"]):
		    		if (data[1] == '1'):
					self.update([Names.UD["IE"], Names.UD["IEDATA"]], Names.Common["NEEDSENCODING"], True)
	       
			elif (data[0] == Names.UD_parse["EncIED"]):
				self.update([Names.UD["IE"], Names.UD["IEDATA"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.UD_parse["DecIED"]):
		    		self.update([Names.UD["IE"], Names.UD["IEDATA"]], Names.Common["DECODED"], data[1])
	
	    		else:
				self.myError = "Unsupported field: " + data[0]
				return False
		return True

