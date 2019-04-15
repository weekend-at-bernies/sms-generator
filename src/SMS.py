import Field
import FieldContainer
import Names
import Utils
import OrderedField

class SMS(FieldContainer.FieldContainer):
	
	excludeSMSCHeader = ""
	explicitSMSType = ""

	def __init__(self, name, parent):
		super(SMS, self).__init__(name, parent)
		self.excludeSMSCHeader = False
		self.explicitSMSType = -1
		SMSC = OrderedField.OrderedField(Names.SMS["SMSC"], self, "", [Names.SMS["SMSCLEN"], Names.SMS["SMSCTYPE"], Names.SMS["SMSCNUM"]])				
		SMSC.myFields[Names.SMS["SMSCLEN"]] = Field.Field(Names.SMS["SMSCLEN"], SMSC, self.encodeSMSCLength)
		SMSC.myFields[Names.SMS["SMSCTYPE"]] = Field.Field(Names.SMS["SMSCTYPE"], SMSC)
		SMSC.myFields[Names.SMS["SMSCNUM"]] = Field.Field(Names.SMS["SMSCNUM"], SMSC, self.encodeNumber)
		self.myFields[Names.SMS["SMSC"]] = SMSC
		self.myFields[Names.SMS["PDUTYPE"]] = Field.Field(Names.SMS["PDUTYPE"], self)
		self.myFields[Names.SMS["MR"]] = Field.Field(Names.SMS["MR"], self)
		Sender = OrderedField.OrderedField(Names.SMS["SEND"], self, "", [Names.SMS["SENDLEN"], Names.SMS["SENDTYPE"], Names.SMS["SENDNUM"]])
		Sender.myFields[Names.SMS["SENDLEN"]] = Field.Field(Names.SMS["SENDLEN"], Sender, self.encodeSenderLength)
		Sender.myFields[Names.SMS["SENDTYPE"]] = Field.Field(Names.SMS["SENDTYPE"], Sender)
		Sender.myFields[Names.SMS["SENDNUM"]] = Field.Field(Names.SMS["SENDNUM"], Sender, self.encodeNumber)
		self.myFields[Names.SMS["SEND"]] = Sender
		self.myFields[Names.SMS["PID"]] = Field.Field(Names.SMS["PID"], self)
		self.myFields[Names.SMS["DCS"]] = Field.Field(Names.SMS["DCS"], self)
		self.myFields[Names.SMS["SCTS"]] = Field.Field(Names.SMS["SCTS"], self)
		self.myFields[Names.SMS["VP"]] = Field.Field(Names.SMS["VP"], self)
		self.myFields[Names.SMS["PI"]] = Field.Field(Names.SMS["PI"], self)
		self.myFields[Names.SMS["FCS"]] = Field.Field(Names.SMS["FCS"], self)
		
	def update(self, fieldnames, varname, value):
		if fieldnames == "":
			if varname == Names.SMS["SMSTYPE"]:
				self.explicitSMSType = value
			elif varname == Names.SMS["EXCLSMSCHDR"]:
				self.excludeSMSCHeader = value
		else:
			super(SMS, self).update(fieldnames, varname, value)
		
###############################
# ENCODERS:	

	def encodeNumber(self, field):
		return Utils.encodeNumber(field.decoded)

	def encodeSMSCLength(self, field=""):      
		l = 0
		l += self.myFields[Names.SMS["SMSC"]].myFields[Names.SMS["SMSCNUM"]].getEncodedOctetCount()
		l += self.myFields[Names.SMS["SMSC"]].myFields[Names.SMS["SMSCTYPE"]].getEncodedOctetCount()
		return "%0.2X" % l

	def encodeSenderLength(self, field=""):      
		l = 0
		l += self.myFields[Names.SMS["SEND"]].myFields[Names.SMS["SENDNUM"]].getEncodedNibbleCount()
		encoding = self.myFields[Names.SMS["SEND"]].myFields[Names.SMS["SENDNUM"]].getEncoding()
		if encoding[len(encoding) - 2] == 'F':
			l -= 1			
		return "%0.2X" % l

###############################

	# A function for getting the RP layer MTI.
	# Currently unused.
	def getRPMTI(self):
		try:
			return self.myParent.getContainer(Names.Containers["RPDU"]).getMTI()
		except:
			return -1

	# <MTI> <SMS TYPE>
	# 0	SMS-DELIVER or DELIVER-REPORT
	# 1	SMS-SUBMIT or SUBMIT-REPORT
	# 2	SMS-STATUS-REPORT or SMS-COMMAND
	# 3	RESERVED
	# Ambiguity is auto-resolved by regarding the RP layer MTI	
	def getMTI(self):
		# The first byte in the SMS layer is: "PDU Type" (TS 123 040).
		# This byte encodes a lot of information, including MTI (Message Type Indicator) in the first 2 bits.
		# The MTI determines what type of SMS: SMS-DELIVER, SMS-DELIVER-REPORT, SMS-STATUS-REPORT, SMS-COMMAND, SMS-SUBMIT, SMS-SUBMIT-REPORT
		PDUType = self.myFields[Names.SMS["PDUTYPE"]]
		encoding = int(PDUType.getEncoding(), 16)
		MTI = encoding & 0x3
		return MTI

	# OBSOLETE
	def isSMSDeliver(self):
		PDUType = self.myFields[Names.SMS["PDUTYPE"]]
		encoding = int(PDUType.getEncoding(), 16)
		MTI = encoding & 0x3
		if MTI == 0x00:
			return True
		else:
			return False

	# OBSOLETE
	def isSMSSubmit(self):
		PDUType = self.myFields[Names.SMS["PDUTYPE"]]
		encoding = int(PDUType.getEncoding(), 16)
		MTI = encoding & 0x3
		if MTI == 0x01:
			return True
		else:
			return False


	def defines8bitEncoding(self):
		
		TPDCS = self.myFields[Names.SMS["DCS"]]
		encoding = int(TPDCS.getEncoding(), 16)
		
		codinggroup = encoding & 0xF0
		bit2 = encoding & 0x04

# Data coding/Message Class
		if codinggroup == 0xF0:
			if bit2 == 0x04:
				return True

		return False

	def defines7bitEncoding(self):
		TPDCS = self.myFields[Names.SMS["DCS"]]
		encoding = int(TPDCS.getEncoding(), 16)
		
		codinggroup = encoding & 0xF0
		lower4bits = encoding & 0x0F
		bit2 = encoding & 0x04

		if codinggroup == 0x00:
# Alphabet indication coding group
			if lower4bits == 0x00:
				return True

# Data coding/Message Class (0xF0)
# Reserved coding group (0x10), but have observed its use(!)
		elif codinggroup == 0xF0 or codinggroup == 0x10 or codinggroup == 0xC0:
			if bit2 == 0x00:
				return True

		return False

	# Overrides
	def dump(self, verbosity):
		if self.explicitSMSType == 0:
			return self.dumpSMSDeliver(verbosity)
		elif self.explicitSMSType == 1:
			return self.dumpSMSDeliverReport(verbosity)
		elif self.explicitSMSType == 2:
			return self.dumpSMSStatusReport(verbosity)
		elif self.explicitSMSType == 3:
			return self.dumpSMSCommand(verbosity)
		elif self.explicitSMSType == 4:
			return self.dumpSMSSubmit(verbosity)
		elif self.explicitSMSType == 5:
			return self.dumpSMSSubmitReport(verbosity)
		# SMS type has not been explicitly defined.
		# Attempt to derive it from MTI + available fields.
		MTI = self.getMTI()
		if MTI == 0:
			if len(self.myFields[Names.SMS["PI"]].dump(False)) > 0:
				# Probably a SMS-DELIVER-REPORT
				return self.dumpSMSDeliverReport(verbosity)
			else:
				return self.dumpSMSDeliver(verbosity)
		elif MTI == 1:
			if len(self.myFields[Names.SMS["PI"]].dump(False)) > 0:
				# Probably a SMS-SUBMIT-REPORT
				return self.dumpSMSSubmitReport(verbosity)
			else:
				return self.dumpSMSSubmit(verbosity)
		elif MTI == 2:
			if len(self.myFields[Names.SMS["CT"]].dump(False)) > 0:
				# Probably a SMS-COMMAND
				return self.dumpSMSCommand(verbosity)
			else:
				return self.dumpSMSStatusReport(verbosity)
		else:
			# Maybe better to return "" ??
			raise ValueError("Ambiguous SMS Type: please define '%s' in your input config file"%(Names.SMS_parse["SMSType"]))



	def dumpSMSDeliver(self, verbosity):
		rstr = ""
		
		if verbosity > 0:
			rstr += "SMS-DELIVER\r\n"
			rstr += Utils.getDash(11) + "\r\n"					
		if self.excludeSMSCHeader == False:
			rstr += self.myFields[Names.SMS["SMSC"]].dump(verbosity)
		rstr += self.myFields[Names.SMS["PDUTYPE"]].dump(verbosity)
		rstr += self.myFields[Names.SMS["SEND"]].dump(verbosity)
		rstr += self.myFields[Names.SMS["PID"]].dump(verbosity)
		rstr += self.myFields[Names.SMS["DCS"]].dump(verbosity)
		rstr += self.myFields[Names.SMS["SCTS"]].dump(verbosity)

		return rstr

	def dumpSMSSubmit(self, verbosity):
		rstr = ""
		
		if verbosity > 0:
			rstr += "SMS-SUBMIT\r\n"
			rstr += Utils.getDash(10) + "\r\n"		
		if self.excludeSMSCHeader == False:
			rstr += self.myFields[Names.SMS["SMSC"]].dump(verbosity)
		rstr += self.myFields[Names.SMS["PDUTYPE"]].dump(verbosity)		
		rstr += self.myFields[Names.SMS["MR"]].dump(verbosity)
		rstr += self.myFields[Names.SMS["SEND"]].dump(verbosity)
		rstr += self.myFields[Names.SMS["PID"]].dump(verbosity)
		rstr += self.myFields[Names.SMS["DCS"]].dump(verbosity)
		rstr += self.myFields[Names.SMS["VP"]].dump(verbosity)

		return rstr

	def dumpSMSSubmitReport(self, verbosity):
		rstr = ""
		# Note that FCS should only be included if encapsulated inside RP-ERR 
		if verbosity > 0:
			rstr += "SMS-SUBMIT-REPORT\r\n"
			rstr += Utils.getDash(17) + "\r\n"		
		rstr += self.myFields[Names.SMS["PDUTYPE"]].dump(verbosity)		
		rstr += self.myFields[Names.SMS["FCS"]].dump(verbosity)
		rstr += self.myFields[Names.SMS["PI"]].dump(verbosity)
		rstr += self.myFields[Names.SMS["SCTS"]].dump(verbosity)
		rstr += self.myFields[Names.SMS["PID"]].dump(verbosity)
		rstr += self.myFields[Names.SMS["DCS"]].dump(verbosity)

		return rstr

	def dumpSMSDeliverReport(self, verbosity):
		rstr = ""
		# Note that FCS should only be included if encapsulated inside RP-ERR
		if verbosity > 0:
			rstr += "SMS-DELIVER-REPORT\r\n"
			rstr += Utils.getDash(18) + "\r\n"	
		rstr += self.myFields[Names.SMS["PDUTYPE"]].dump(verbosity)	
		rstr += self.myFields[Names.SMS["FCS"]].dump(verbosity)
		rstr += self.myFields[Names.SMS["PI"]].dump(verbosity)
		rstr += self.myFields[Names.SMS["PID"]].dump(verbosity)
		rstr += self.myFields[Names.SMS["DCS"]].dump(verbosity)

		return rstr

	def dumpSMSStatusReport(self, verbosity):
		rstr = ""
		
		if verbosity > 0:
			rstr += "SMS-STATUS-REPORT\r\n"
			rstr += Utils.getDash(17) + "\r\n"
		# IMPLEMENT ME
		return rstr

	def dumpSMSCommand(self, verbosity):
		rstr = ""
		
		if verbosity > 0:
			rstr += "SMS-COMMAND\r\n"
			rstr += Utils.getDash(11) + "\r\n"
		# IMPLEMENT ME
		return rstr
