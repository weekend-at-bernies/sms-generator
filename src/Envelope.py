import Field
import FieldContainer
import Names
import Utils
import OrderedField

class Envelope(FieldContainer.FieldContainer):

	SimpleTLVcount = 0
	currSimpleTLV = ""
	lastSimpleTLVLenFlag = ""
	
	def __init__(self, name, parent):
		super(Envelope, self).__init__(name, parent)
		self.lastSimpleTLVLenFlag = False
		self.myFields[Names.ENVELOPE["CLA"]] = Field.Field(Names.ENVELOPE["CLA"], self)
		self.myFields[Names.ENVELOPE["INS"]] = Field.Field(Names.ENVELOPE["INS"], self)
		self.myFields[Names.ENVELOPE["P1"]] = Field.Field(Names.ENVELOPE["P1"], self)
		self.myFields[Names.ENVELOPE["P2"]] = Field.Field(Names.ENVELOPE["P2"], self)
		self.myFields[Names.ENVELOPE["LEN"]] = Field.Field(Names.ENVELOPE["LEN"], self, self.encodeLEN)
		BERTLV = OrderedField.OrderedField(Names.ENVELOPE["BERTLV"], self, "", [Names.ENVELOPE["BERTLVTAG"], Names.ENVELOPE["BERTLVLEN"]])
		BERTLV.myFields[Names.ENVELOPE["BERTLVTAG"]] = Field.Field(Names.ENVELOPE["BERTLVTAG"], BERTLV, "", self.dissectBERTLV)
		BERTLV.myFields[Names.ENVELOPE["BERTLVLEN"]] = Field.Field(Names.ENVELOPE["BERTLVLEN"], BERTLV, self.encodeBERTLVLen)		
		self.myFields[Names.ENVELOPE["BERTLV"]] = BERTLV

		
	def update(self, fieldnames, varname, value):
		if fieldnames == "":
			pass
		else:
			super(RPDU, self).update(fieldnames, varname, value)

	def update(self, fieldnames, varname, value):
		newfieldnames = ""
		SimpleTLVname = ""		
		if fieldnames == "":
			if varname == Names.ENVELOPE["LASTSIMPLETLVLENFLAG"]:
				self.lastSimpleTLVLenFlag = value
		else:			
			if Names.ENVELOPE["SIMPLETLV"] in fieldnames:
				SimpleTLVname = Names.ENVELOPE["SIMPLETLV"] + "%d"%(self.SimpleTLVcount)
				newfieldnames = fieldnames
				newfieldnames.pop(0)
				newfieldnames = [SimpleTLVname] + newfieldnames
				if Names.ENVELOPE["SIMPLETLVTAG"] in fieldnames:
					#if Names.Common["NEEDSENCODING"] == varname:
						self.SimpleTLVcount += 1
						SimpleTLVname = Names.ENVELOPE["SIMPLETLV"] + "%d"%(self.SimpleTLVcount)
						self.currSimpleTLV = OrderedField.OrderedField(SimpleTLVname, self, "", [Names.ENVELOPE["SIMPLETLVTAG"], Names.ENVELOPE["SIMPLETLVLEN"], Names.ENVELOPE["SIMPLETLVVAL"]])	
						self.currSimpleTLV.myFields[Names.ENVELOPE["SIMPLETLVTAG"]] = Field.Field(Names.ENVELOPE["SIMPLETLVTAG"], self.currSimpleTLV, "", self.dissectSimpleTLV)			
						self.currSimpleTLV.myFields[Names.ENVELOPE["SIMPLETLVLEN"]] = Field.Field(Names.ENVELOPE["SIMPLETLVLEN"], self.currSimpleTLV, self.encodeSimpleTLVLen)						
						self.currSimpleTLV.myFields[Names.ENVELOPE["SIMPLETLVVAL"]] = Field.Field(Names.ENVELOPE["SIMPLETLVVAL"], self.currSimpleTLV)
						self.myFields[SimpleTLVname] = self.currSimpleTLV
						newfieldnames = [SimpleTLVname, Names.ENVELOPE["SIMPLETLVTAG"]]
				
			else:
				newfieldnames = fieldnames
			super(Envelope, self).update(newfieldnames, varname, value)

###############################
# DISSECTORS:

	def dissectBERTLV(self, field):
		rstrs = []
		tag = field.getEncoding()
		if tag == "D0":
			rstrs.append("Proactive SIM command")
		elif tag == "D1":
			rstrs.append("SMS-PP download")
		elif tag == "D2":
			rstrs.append("Cell Broadcast download")
		elif tag == "D3":
			rstrs.append("Menu Selection")
		elif tag == "D4":
			rstrs.append("Call Control")
		elif tag == "D5":
			rstrs.append("MO short message control")
		elif tag == "D6":
			rstrs.append("Event download")
		elif tag == "D7":
			rstrs.append("Timer Expiration")
		else:
			rstrs.append("Unknown BER-TLV Tag")
		return rstrs

	def dissectSimpleTLV(self, field):
		rstrs = []
		tag = field.getEncoding()
		n_org = int(tag, 16)
		n = n_org & 0x7F

		if n == 0x01:
			rstrs.append("Command Details")
		elif n == 0x02:
			rstrs.append("Device Identities")
		elif n == 0x03:
			rstrs.append("Result")
		elif n == 0x04:
			rstrs.append("Duration")
		elif n == 0x05:
			rstrs.append("Alpha")
		elif n == 0x06:
			rstrs.append("Address")
		elif n == 0x07:
			rstrs.append("Capability Configuration Parameters")
		elif n == 0x08:
			rstrs.append("Called Party Subaddress")
		elif n == 0x09:
			rstrs.append("SS String")
		elif n == 0x0A:
			rstrs.append("USSD String")
		elif n == 0x0B:
			rstrs.append("SMS TPDU")
		elif n == 0x0C:
			rstrs.append("Cell Broadcast Page")
		elif n == 0x0D:
			rstrs.append("Text String")
		elif n == 0x0E:
			rstrs.append("Tone")
		elif n == 0x0F:
			rstrs.append("Item")
		elif n == 0x10:
			rstrs.append("Item Identifier")
		elif n == 0x11:
			rstrs.append("Response Length")
		elif n == 0x12:
			rstrs.append("File List")
		elif n == 0x13:
			rstrs.append("Location Information")
		elif n == 0x14:
			rstrs.append("IMEI")
		elif n == 0x15:
			rstrs.append("Help Request")
		elif n == 0x16:
			rstrs.append("Network Measurement Results")
		elif n == 0x17:
			rstrs.append("Default Text")
		elif n == 0x18:
			rstrs.append("Items Next Action Indicator")
		elif n == 0x19:
			rstrs.append("Event List")
		elif n == 0x1A:
			rstrs.append("Cause")
		elif n == 0x1B:
			rstrs.append("Location Status")
		elif n == 0x1C:
			rstrs.append("Transaction Identifier")
		elif n == 0x1D:
			rstrs.append("BCCH Channel List")
		elif n == 0x1E:
			rstrs.append("Icon Identifier")
		elif n == 0x1F:
			rstrs.append("Item Icon Identifier List")
		elif n == 0x20:
			rstrs.append("Card Reader Status")
		elif n == 0x21:
			rstrs.append("Card ATR")
		elif n == 0x22:
			rstrs.append("C-APDU")
		elif n == 0x23:
			rstrs.append("R-APDU")
		else:
			rstrs.append("Unknown Simple-TLV Tag")
		if n_org & 0x80 == 0:
			rstrs.append("No comprehension required")
		else:
			rstrs.append("Comprehension required")
		return rstrs


###############################
# ENCODERS:	
		
	def encodeLEN(self, field): 
		l = 0
		l += self.myFields[Names.ENVELOPE["BERTLV"]].getEncodedOctetCount()
		for i in range(0, self.SimpleTLVcount):					
			l += self.myFields[Names.ENVELOPE["SIMPLETLV"] + "%d"%(i + 1)].getEncodedOctetCount()
		l += self.myParent.getOctetCountAfter(self.myName)		
		return "%0.2X" % l

	def encodeBERTLVLen(self, field):
		l = 0
		for i in range(0, self.SimpleTLVcount):					
			l += self.myFields[Names.ENVELOPE["SIMPLETLV"] + "%d"%(i + 1)].getEncodedOctetCount()
		l += self.myParent.getOctetCountAfter(self.myName)		
		return "%0.2X" % l

	def encodeSimpleTLVLen(self, field):
		l = 0
		mySimpleTLV = field.myParent
		if (mySimpleTLV.myName == Names.ENVELOPE["SIMPLETLV"] + "%d"%(self.SimpleTLVcount)) and (self.lastSimpleTLVLenFlag == True):
			l += self.myParent.getOctetCountAfter(self.myName)
		else:
			l += self.myFields[mySimpleTLV.myName].myFields[Names.ENVELOPE["SIMPLETLVVAL"]].getEncodedOctetCount()
		return "%0.2X" % l


	#def encodeRPDALength(self, field=""):      
	#	l = 0
	#	l += self.myFields[Names.ENVELOPE["RPDA"]].myFields[Names.ENVELOPE["RPDANO"]].getEncodedOctetCount()
	#	return "%0.2X" % l

	#def encodeRPUDL(self, field=""):
	#	l = 0
	#	l += self.myParent.getOctetCountAfter(self.myName)
	#	return "%0.2X" % l

###############################

	# Overrides
	def dump(self, verbosity):
		rstr = ""

		if verbosity > 0:
			rstr += "%s\r\n"%(Names.Containers["ENVELOPE"])
			rstr += Utils.getDash(len(Names.Containers["ENVELOPE"])) + "\r\n"
				
		rstr += self.myFields[Names.ENVELOPE["CLA"]].dump(verbosity)
		rstr += self.myFields[Names.ENVELOPE["INS"]].dump(verbosity)
		rstr += self.myFields[Names.ENVELOPE["P1"]].dump(verbosity)
		rstr += self.myFields[Names.ENVELOPE["P2"]].dump(verbosity)
		rstr += self.myFields[Names.ENVELOPE["LEN"]].dump(verbosity)
		rstr += self.myFields[Names.ENVELOPE["BERTLV"]].dump(verbosity)
		for i in range(0, self.SimpleTLVcount):
			rstr += self.myFields[Names.ENVELOPE["SIMPLETLV"] + "%d"%(i + 1)].dump(verbosity) 

		return rstr

	
		
