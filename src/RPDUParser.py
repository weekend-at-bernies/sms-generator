import Names
import Parser

class RPDUParser(Parser.Parser):

	def __init__(self, overallSMS):
		self.myName = Names.Containers["RPDU"]
		super(RPDUParser, self).__init__(overallSMS)
		
	def parse(self, inputdata):
	    	    	    
	        for data in inputdata:

			if (data[0] == Names.RPDU_parse["MTI"]):
				self.update([Names.RPDU["RPDUMTI"]], Names.Common["ENCODED"], data[1])	

			elif (data[0] == Names.RPDU_parse["MR"]):
				self.update([Names.RPDU["RPDUMR"]], Names.Common["ENCODED"], data[1])	

			elif (data[0] == Names.RPDU_parse["RPCause"]):
				self.update([Names.RPDU["RPCAUSE"]], Names.Common["ENCODED"], data[1])	

			elif (data[0] == Names.RPDU_parse["GenRPCauseLen"]):
		    		if (data[1] == '1'):
					self.update([Names.RPDU["RPCAUSELEN"]], Names.Common["NEEDSENCODING"], True)

			elif (data[0] == Names.RPDU_parse["RPCauseLen"]):
				self.update([Names.RPDU["RPCAUSELEN"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.RPDU_parse["RPUDType"]):
				self.update([Names.RPDU["RPUDTYPE"]], Names.Common["ENCODED"], data[1])			

			elif (data[0] == Names.RPDU_parse["GenRPOALen"]):
		    		if (data[1] == '1'):
					self.update([Names.RPDU["RPOA"], Names.RPDU["RPOALEN"]], Names.Common["NEEDSENCODING"], True)

			elif (data[0] == Names.RPDU_parse["RPOALen"]):
				self.update([Names.RPDU["RPOA"], Names.RPDU["RPOALEN"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.RPDU_parse["GenEncRPOA"]):
		    		if (data[1] == '1'):
					self.update([Names.RPDU["RPOA"], Names.RPDU["RPOANO"]], Names.Common["NEEDSENCODING"], True)
	       
			elif (data[0] == Names.RPDU_parse["EncRPOA"]):
				self.update([Names.RPDU["RPOA"], Names.RPDU["RPOANO"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.RPDU_parse["DecRPOA"]):
		    		self.update([Names.RPDU["RPOA"], Names.RPDU["RPOANO"]], Names.Common["DECODED"], data[1])

			elif (data[0] == Names.RPDU_parse["GenRPDALen"]):
		    		if (data[1] == '1'):
					self.update([Names.RPDU["RPDA"], Names.RPDU["RPDALEN"]], Names.Common["NEEDSENCODING"], True)

			elif (data[0] == Names.RPDU_parse["RPDALen"]):
				self.update([Names.RPDU["RPDA"], Names.RPDU["RPDALEN"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.RPDU_parse["GenEncRPDA"]):
		    		if (data[1] == '1'):
					self.update([Names.RPDU["RPDA"], Names.RPDU["RPDANO"]], Names.Common["NEEDSENCODING"], True)
	       
			elif (data[0] == Names.RPDU_parse["EncRPDA"]):
				self.update([Names.RPDU["RPDA"], Names.RPDU["RPDANO"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.RPDU_parse["DecRPDA"]):
		    		self.update([Names.RPDU["RPDA"], Names.RPDU["RPDANO"]], Names.Common["DECODED"], data[1])
			
			elif (data[0] == Names.RPDU_parse["GenRPUDL"]):
		    		if (data[1] == '1'):
					self.update([Names.RPDU["RPUDL"]], Names.Common["NEEDSENCODING"], True)

			elif (data[0] == Names.RPDU_parse["RPUDL"]):
				self.update([Names.RPDU["RPUDL"]], Names.Common["ENCODED"], data[1])

	    		else:
				self.myError = "Unsupported field: " + data[0]
				return False
		return True

