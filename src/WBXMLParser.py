import Names
import Parser

class WBXMLParser(Parser.Parser):

	def __init__(self, overallSMS):
		self.myName = Names.Containers["WBXML"]
		super(WBXMLParser, self).__init__(overallSMS)
		
	def parse(self, inputdata):
	    	    	    
	        for data in inputdata:

			if (data[0] == Names.WBXML_parse["GenEncWBXML"]):
		    		if (data[1] == '1'):
					self.update([Names.WBXML["WBXML"]], Names.Common["NEEDSENCODING"], True)

			elif (data[0] == Names.WBXML_parse["EncWBXML"]):
				self.update([Names.WBXML["WBXML"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.WBXML_parse["DecWBXML"]):
		    		self.update([Names.WBXML["WBXML"]], Names.Common["DECODED"], data[1])
			
			elif (data[0] == Names.WBXML_parse["WBXMLVers"]):
		    		self.update("", Names.WBXML["WBXMLVERS"], data[1])

	    		else:
				self.myError = "Unsupported field: " + data[0]
				return False
		return True

