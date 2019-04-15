import Names
import Parser
import Utils

class SMSParser(Parser.Parser):

	def __init__(self, overallSMS):
		self.myName = Names.Containers["SMS"]
		super(SMSParser, self).__init__(overallSMS)
		
	def parse(self, inputdata):
	    
	        PDUTypeBits = ""    
	        TPIDBits = ""    
	        TPDCSBits = ""
	    	    
	        for data in inputdata:

			if (data[0] == Names.SMS_parse["ExclSMSCHdr"]):
		    		if (data[1] == '1'):
					self.update("", Names.SMS["EXCLSMSCHDR"], True)		

			elif (data[0] == Names.SMS_parse["SMSType"]):
			    	if (data[1] >= 0 or data[1] < 6):
					self.update("", Names.SMS["SMSTYPE"], data[1])
			
			elif (data[0] == Names.SMS_parse["GenSMSCLen"]):
		    		if (data[1] == '1'):
					self.update([Names.SMS["SMSC"], Names.SMS["SMSCLEN"]], Names.Common["NEEDSENCODING"], True)

			elif (data[0] == Names.SMS_parse["SMSCLen"]):
				self.update([Names.SMS["SMSC"], Names.SMS["SMSCLEN"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.SMS_parse["SMSCType"]):
				self.update([Names.SMS["SMSC"], Names.SMS["SMSCTYPE"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.SMS_parse["GenEncSMSCNum"]):
		    		if (data[1] == '1'):
					self.update([Names.SMS["SMSC"], Names.SMS["SMSCNUM"]], Names.Common["NEEDSENCODING"], True)
	       
			elif (data[0] == Names.SMS_parse["EncSMSCNum"]):
				self.update([Names.SMS["SMSC"], Names.SMS["SMSCNUM"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.SMS_parse["DecSMSCNum"]):
		    		self.update([Names.SMS["SMSC"], Names.SMS["SMSCNUM"]], Names.Common["DECODED"], data[1])


			elif (data[0] == Names.SMS_parse["GenSendLen"]):
		    		if (data[1] == '1'):
					self.update([Names.SMS["SEND"], Names.SMS["SENDLEN"]], Names.Common["NEEDSENCODING"], True)

			elif (data[0] == Names.SMS_parse["SendLen"]):
		    		self.update([Names.SMS["SEND"], Names.SMS["SENDLEN"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.SMS_parse["SendType"]):
		    		self.update([Names.SMS["SEND"], Names.SMS["SENDTYPE"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.SMS_parse["GenEncSendNum"]):
		    		if (data[1] == '1'):
					self.update([Names.SMS["SEND"], Names.SMS["SENDNUM"]], Names.Common["NEEDSENCODING"], True)
	       
			elif (data[0] == Names.SMS_parse["EncSendNum"]):
		    		self.update([Names.SMS["SEND"], Names.SMS["SENDNUM"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.SMS_parse["DecSendNum"]):
		    		self.update([Names.SMS["SEND"], Names.SMS["SENDNUM"]], Names.Common["DECODED"], data[1])
			

			elif (data[0] == Names.SMS_parse["MR"]):
				self.update([Names.SMS["MR"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.SMS_parse["SCTS"]):
				self.update([Names.SMS["SCTS"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.SMS_parse["VP"]):
				self.update([Names.SMS["VP"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.SMS_parse["PI"]):
				self.update([Names.SMS["PI"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.SMS_parse["FCS"]):
				self.update([Names.SMS["FCS"]], Names.Common["ENCODED"], data[1])


			elif (data[0] == Names.SMS_parse["RPDUfile"]):
			    	self.myOverallSMS.myRPDUFile = data[1]

			elif (data[0] == Names.SMS_parse["UDFile"]):
			    	self.myOverallSMS.myUDFile = data[1]

			elif (data[0] == Names.SMS_parse["WSPFile"]):
			    	self.myOverallSMS.myWSPFile = data[1]

			elif (data[0] == Names.SMS_parse["WBXMLFile"]):
			    	self.myOverallSMS.myWBXMLFile = data[1]

			elif (data[0] == Names.SMS_parse["SIMCMDFile"]):
			    	self.myOverallSMS.mySIMCmdFile = data[1]

			elif (data[0] == Names.SMS_parse["MMSFile"]):
			    	self.myOverallSMS.myMMSFile = data[1]

			elif (data[0] == Names.SMS_parse["EnvelopeFile"]):
			    	self.myOverallSMS.myEnvelopeFile = data[1]

			
			elif ( Utils.inRange(Names.SMS_parse["PDUType"], 0, 7, data[0]) == (True, 0)):
				PDUTypeBits += data[1] 
				self.update([Names.SMS["PDUTYPE"]], Names.Common["ENCODED"], ("%02X" % int(PDUTypeBits,2)))
			elif ( Utils.inRange(Names.SMS_parse["PDUType"], 0, 7, data[0])[0] == True):
				PDUTypeBits += data[1]

			elif ( Utils.inRange(Names.SMS_parse["PID"], 0, 7, data[0]) == (True, 0)):
				TPIDBits += data[1] 
				self.update([Names.SMS["PID"]], Names.Common["ENCODED"], ("%02X" % int(TPIDBits,2)))
			elif ( Utils.inRange(Names.SMS_parse["PID"], 0, 7, data[0])[0] == True):
				TPIDBits += data[1]

			elif ( Utils.inRange(Names.SMS_parse["DCS"], 0, 7, data[0]) == (True, 0)):
				TPDCSBits += data[1] 
				self.update([Names.SMS["DCS"]], Names.Common["ENCODED"], ("%02X" % int(TPDCSBits,2)))
			elif ( Utils.inRange(Names.SMS_parse["DCS"], 0, 7, data[0])[0] == True):
				TPDCSBits += data[1]

	    		else:
				self.myError = "Unsupported field: " + data[0]
				return False
		return True

