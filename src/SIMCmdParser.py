import Names
import Parser
import Utils

class SIMCmdParser(Parser.Parser):

	def __init__(self, overallSMS):
		self.myName = Names.Containers["SIMCMD"]
		super(SIMCmdParser, self).__init__(overallSMS)
		
	def parse(self, inputdata):
	    
	        SPI1Bits = ""    
		SPI2Bits = ""  
	        KiCBits = ""    
	        KiDBits = ""
	    	    
	        for data in inputdata:
						
			if (data[0] == Names.SIMCMD_parse["GenCPL"]):
		    		if (data[1] == '1'):
					self.update([Names.SIMCMD["CPL"]], Names.Common["NEEDSENCODING"], True)

			elif (data[0] == Names.SIMCMD_parse["CPL"]):
				self.update([Names.SIMCMD["CPL"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.SIMCMD_parse["GenCHL"]):
		    		if (data[1] == '1'):
					self.update([Names.SIMCMD["CHL"]], Names.Common["NEEDSENCODING"], True)

			elif (data[0] == Names.SIMCMD_parse["CHL"]):
				self.update([Names.SIMCMD["CHL"]], Names.Common["ENCODED"], data[1])


			elif ( Utils.inRange(Names.SIMCMD_parse["SPI"], 8, 15, data[0])[0] == True):
				SPI1Bits += data[1]
			elif ( Utils.inRange(Names.SIMCMD_parse["SPI"], 0, 7, data[0]) == (True, 0)):
				SPI2Bits += data[1]
				if (len(SPI1Bits) > 0) and (len(SPI2Bits) > 0):
					self.update([Names.SIMCMD["SPI"]], Names.Common["ENCODED"], ("%02X%02X" % (int(SPI1Bits,2), int(SPI2Bits,2))))
			elif ( Utils.inRange(Names.SIMCMD_parse["SPI"], 0, 7, data[0])[0] == True):
				SPI2Bits += data[1]

			elif ( Utils.inRange(Names.SIMCMD_parse["KiC"], 0, 7, data[0]) == (True, 0)):
				KiCBits += data[1] 
				if len(KiCBits) > 0:
					self.update([Names.SIMCMD["KiC"]], Names.Common["ENCODED"], ("%02X" % int(KiCBits,2)))
			elif ( Utils.inRange(Names.SIMCMD_parse["KiC"], 0, 7, data[0])[0] == True):
				KiCBits += data[1]

			elif ( Utils.inRange(Names.SIMCMD_parse["KiD"], 0, 7, data[0]) == (True, 0)):
				KiDBits += data[1] 
				if len(KiDBits) > 0:
					self.update([Names.SIMCMD["KiD"]], Names.Common["ENCODED"], ("%02X" % int(KiDBits,2)))
			elif ( Utils.inRange(Names.SIMCMD_parse["KiD"], 0, 7, data[0])[0] == True):
				KiDBits += data[1]
				

			elif (data[0] == Names.SIMCMD_parse["TAR"]):
				self.update([Names.SIMCMD["TAR"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.SIMCMD_parse["CNTR"]):
				self.update([Names.SIMCMD["CNTR"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.SIMCMD_parse["PCNTR"]):
				self.update([Names.SIMCMD["PCNTR"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.SIMCMD_parse["RC_CC_DS"]):
				self.update([Names.SIMCMD["RC_CC_DS"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.SIMCMD_parse["GenSecData"]):
		    		if (data[1] == '1'):
					self.update([Names.SIMCMD["SECDATA"]], Names.Common["NEEDSENCODING"], True)
	       
			elif (data[0] == Names.SIMCMD_parse["EncSecData"]):
		    		self.update([Names.SIMCMD["SECDATA"]], Names.Common["ENCODED"], data[1])

			elif (data[0] == Names.SIMCMD_parse["DecSecData"]):
		    		self.update([Names.SIMCMD["SECDATA"]], Names.Common["DECODED"], data[1])


	    		else:
				self.myError = "Unsupported field: " + data[0]
				return False
		return True

