import Names
import Parser

class MMSParser(Parser.Parser):

	def __init__(self, overallSMS):
		self.myName = Names.Containers["MMS"]
		super(MMSParser, self).__init__(overallSMS)
		
	def parse(self, inputdata):
	    	    	    
	        for data in inputdata:

			if (data[0] == Names.MMS_parse["MsgType"]):
				self.update([Names.MMS["MSGTYPE"]], Names.Common["ENCODED"], data[1])	

			elif (data[0] == Names.MMS_parse["TID"]):
				self.update([Names.MMS["TID"]], Names.Common["ENCODED"], data[1])				

			elif (data[0] == Names.MMS_parse["Vers"]):
				self.update([Names.MMS["VERS"]], Names.Common["ENCODED"], data[1])
	       
			elif (data[0] == Names.MMS_parse["From"]):
				self.update([Names.MMS["FROM"]], Names.Common["ENCODED"], data[1])
			
			elif (data[0] == Names.MMS_parse["Subj"]):
				self.update([Names.MMS["SUBJ"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.MMS_parse["MsgCls"]):
				self.update([Names.MMS["MSGCLS"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.MMS_parse["MsgSize"]):
				self.update([Names.MMS["MSGSIZE"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.MMS_parse["Exp"]):
				self.update([Names.MMS["EXP"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.MMS_parse["CntLoc"]):
				self.update([Names.MMS["CNTLOC"]], Names.Common["ENCODED"], data[1])

	    		else:
				self.myError = "Unsupported field: " + data[0]
				return False
		return True

