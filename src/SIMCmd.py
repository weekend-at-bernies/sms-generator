import Field
import FieldContainer
import Names
import Utils
import OrderedField

class SIMCmd(FieldContainer.FieldContainer):
	
	def __init__(self, name, parent):
		super(SIMCmd, self).__init__(name, parent)
		self.myFields[Names.SIMCMD["CPL"]] = Field.Field(Names.SIMCMD["CPL"], self, self.encodeCPL)	
		self.myFields[Names.SIMCMD["CHL"]] = Field.Field(Names.SIMCMD["CHL"], self, self.encodeCHL)	
		self.myFields[Names.SIMCMD["SPI"]] = Field.Field(Names.SIMCMD["SPI"], self, "", self.dissectSPI)
		self.myFields[Names.SIMCMD["KiC"]] = Field.Field(Names.SIMCMD["KiC"], self, "", self.dissectKI)
		self.myFields[Names.SIMCMD["KiD"]] = Field.Field(Names.SIMCMD["KiD"], self, "", self.dissectKI)
		self.myFields[Names.SIMCMD["TAR"]] = Field.Field(Names.SIMCMD["TAR"], self)
		self.myFields[Names.SIMCMD["CNTR"]] = Field.Field(Names.SIMCMD["CNTR"], self)
		self.myFields[Names.SIMCMD["PCNTR"]] = Field.Field(Names.SIMCMD["PCNTR"], self)
		self.myFields[Names.SIMCMD["RC_CC_DS"]] = Field.Field(Names.SIMCMD["RC_CC_DS"], self)
		self.myFields[Names.SIMCMD["SECDATA"]] = Field.Field(Names.SIMCMD["SECDATA"], self) #, self.encodeSECDATA)
		
	def update(self, fieldnames, varname, value):
		if fieldnames == "":
			pass
		else:
			super(SIMCmd, self).update(fieldnames, varname, value)
		
###############################
# ENCODERS:

	def encodeCPL(self, field):
		l = 0
		l += self.myFields[Names.SIMCMD["CHL"]].getEncodedOctetCount()
		l += self.myFields[Names.SIMCMD["SPI"]].getEncodedOctetCount()
		l += self.myFields[Names.SIMCMD["KiC"]].getEncodedOctetCount()
		l += self.myFields[Names.SIMCMD["KiD"]].getEncodedOctetCount()
		l += self.myFields[Names.SIMCMD["TAR"]].getEncodedOctetCount()
		l += self.myFields[Names.SIMCMD["CNTR"]].getEncodedOctetCount()
		l += self.myFields[Names.SIMCMD["PCNTR"]].getEncodedOctetCount()
		l += self.myFields[Names.SIMCMD["RC_CC_DS"]].getEncodedOctetCount()
		l += self.myFields[Names.SIMCMD["SECDATA"]].getEncodedOctetCount()
		return "%0.4X" % l

	def encodeCHL(self, field):      
		l = 0
		l += self.myFields[Names.SIMCMD["SPI"]].getEncodedOctetCount()
		l += self.myFields[Names.SIMCMD["KiC"]].getEncodedOctetCount()
		l += self.myFields[Names.SIMCMD["KiD"]].getEncodedOctetCount()
		l += self.myFields[Names.SIMCMD["TAR"]].getEncodedOctetCount()
		l += self.myFields[Names.SIMCMD["CNTR"]].getEncodedOctetCount()
		l += self.myFields[Names.SIMCMD["PCNTR"]].getEncodedOctetCount()
		l += self.myFields[Names.SIMCMD["RC_CC_DS"]].getEncodedOctetCount()
		return "%0.2X" % l

	#def encodeSECDATA(self, field|field=""):   	
	#	return "%0.2X" % l

###############################
# DISSECTORS:

	def dissectKI(self, field):
		rstrs = []
		KI = field.getEncoding()[:2]
		if len(KI) > 0:
			# FIX ME: 2nd parameter should be 'field'
			rstrs += self.dissectKI1(int(KI, 16), (field.myName == Names.SIMCMD["KiC"]))
		return rstrs

	# FIX ME: 3rd parameter should be 'field'
	def dissectKI1(self, n_org, isKIc):
		rstrs = []
		# FIX ME: comparison should involve 'field.myName'
		if isKIc:
			rstrs.append("Key and algorithm identifier for: ciphering")
		else:
			rstrs.append("Key and algorithm identifier for: RC/CC/DS")
		rstrs.append("---")
		n = n_org & 0x03
		if n == 0:
			rstrs.append("Algorithm known implicitly by both entities")
		elif n == 1:
			rstrs.append("DES")
		elif n == 2: 
			rstrs.append("Reserved")
		elif n == 3:
			rstrs.append("Proprietary implementations")
		n = n_org >> 2
		n = n & 0x03
		if n == 0:
			rstrs.append("CBC")
		elif n == 1:
			rstrs.append("Triple/Outer CBC/2 keys")
		elif n == 2: 
			rstrs.append("Triple/Outer CBC/3 keys")
		elif n == 3:
			if isKIc:
				rstrs.append("ECB")
			else:
				rstrs.append("Reserved")
			
		n = n_org >> 4
		n = n & 0x0F
		rstrs.append("Key %d"%(n))
		return rstrs

	def dissectSPI(self, field):
		rstrs = []
		SPI1 = field.getEncoding()[:2]
		SPI2 = field.getEncoding()[2:4]
		if (len(SPI1) > 0) and (len(SPI2) > 0):
			rstrs += ["Security Parameters Indication"] + ["---"] + self.dissectSPI1(int(SPI1, 16)) + ["---"] + self.dissectSPI2(int(SPI2, 16))
		return rstrs

	def dissectSPI1(self, n_org):
		rstrs = []
		n = n_org & 0x03
		if n == 0:
			rstrs.append("Command has no RC/CC/DS")
		elif n == 1:
			rstrs.append("Command has RC")
		elif n == 2: 
			rstrs.append("Command has CC")
		elif n == 3:
			rstrs.append("Command has DS")
		n = n_org >> 2
		n = n & 0x01
		if n == 0:
			rstrs.append("Command has no encryption applied")
		elif n == 1:
			rstrs.append("Command has encryption applied")
		n = n_org >> 3
		n = n & 0x03
		if n == 0:
			rstrs.append("Ignore CNTR")
		elif n == 1:
			rstrs.append("CNTR for info purposes")
		elif n == 2: 
			rstrs.append("CNTR for security purposes 1")
		elif n == 3:
			rstrs.append("CNTR for security purposes 2")
		n = n_org >> 5
		n = n & 0x07
		if n != 0:
			rstrs.append("Reserved")
			#rstrs.append("WARNING: bits 7 & 8 in 1st octet are reserved (ie. should be 0)")
		return rstrs

	def dissectSPI2(self, n_org):
		rstrs = []
		n = n_org & 0x03
		if n == 0:
			rstrs.append("No PoR required")
		elif n == 1:
			rstrs.append("PoR always required")
		elif n == 2: 
			rstrs.append("PoR required only for errors")
		elif n == 3:
			rstrs.append("Reserved (ie. should not be this!)")
		n = n_org >> 2
		n = n & 0x03
		if n == 0:
			rstrs.append("Do not apply RC/CC/DS to PoR")
		elif n == 1:
			rstrs.append("Apply RC to PoR")
		elif n == 2: 
			rstrs.append("Apply CC to PoR")
		elif n == 3:
			rstrs.append("Apply DS to PoR")
		n = n_org >> 4
		n = n & 0x01
		if n == 0:
			rstrs.append("Do not apply encryption to PoR")
		elif n == 1:
			rstrs.append("Apply encryption to PoR")
		n = n_org >> 5
		n = n & 0x01
		if n == 0:
			rstrs.append("Send PoR using SMS-DELIVER-REPORT")
		elif n == 1:
			rstrs.append("Send PoR using SMS-SUBMIT")
		n = n_org >> 6
		n = n & 0x03
		if n != 0:
			rstrs.append("Reserved")
			#rstrs.append("WARNING: bits 7 & 8 in 2nd octet are reserved (ie. should be 0)")
		return rstrs
			


###############################

	# Overrides
	def dump(self, verbosity):
		rstr = ""

		if verbosity > 0:
			rstr += "%s\r\n"%(Names.Containers["SIMCMD"])
			rstr += Utils.getDash(len(Names.Containers["SIMCMD"])) + "\r\n"
				
		rstr += self.myFields[Names.SIMCMD["CPL"]].dump(verbosity)
		rstr += self.myFields[Names.SIMCMD["CHL"]].dump(verbosity)
		rstr += self.myFields[Names.SIMCMD["SPI"]].dump(verbosity)
		rstr += self.myFields[Names.SIMCMD["KiC"]].dump(verbosity)
		rstr += self.myFields[Names.SIMCMD["KiD"]].dump(verbosity)
		rstr += self.myFields[Names.SIMCMD["TAR"]].dump(verbosity)
		rstr += self.myFields[Names.SIMCMD["CNTR"]].dump(verbosity)
		rstr += self.myFields[Names.SIMCMD["PCNTR"]].dump(verbosity)
		rstr += self.myFields[Names.SIMCMD["RC_CC_DS"]].dump(verbosity)
		rstr += self.myFields[Names.SIMCMD["SECDATA"]].dump(verbosity)

		return rstr

	
		
