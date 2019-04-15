import Field
import FieldContainer
import Names
import Utils
import OrderedField

class RPDU(FieldContainer.FieldContainer):
	

	def __init__(self, name, parent):
		super(RPDU, self).__init__(name, parent)
		self.myFields[Names.RPDU["RPDUMTI"]] = Field.Field(Names.RPDU["RPDUMTI"], self)
		self.myFields[Names.RPDU["RPDUMR"]] = Field.Field(Names.RPDU["RPDUMR"], self)
		RPOA = OrderedField.OrderedField(Names.RPDU["RPOA"], self, "", [Names.RPDU["RPOALEN"], Names.RPDU["RPOANO"]])
		RPOA.myFields[Names.RPDU["RPOALEN"]] = Field.Field(Names.RPDU["RPOALEN"], RPOA, self.encodeRPOALength)
		RPOA.myFields[Names.RPDU["RPOANO"]] = Field.Field(Names.RPDU["RPOANO"], RPOA, self.encodeDecode)
		self.myFields[Names.RPDU["RPOA"]] = RPOA
		RPDA = OrderedField.OrderedField(Names.RPDU["RPDA"], self, "", [Names.RPDU["RPDALEN"], Names.RPDU["RPDANO"]])
		RPDA.myFields[Names.RPDU["RPDALEN"]] = Field.Field(Names.RPDU["RPDALEN"], RPDA, self.encodeRPDALength)
		RPDA.myFields[Names.RPDU["RPDANO"]] = Field.Field(Names.RPDU["RPDANO"], RPDA, self.encodeDecode)
		self.myFields[Names.RPDU["RPDA"]] = RPDA
		self.myFields[Names.RPDU["RPUDL"]] = Field.Field(Names.RPDU["RPUDL"], self, self.encodeRPUDL)
		self.myFields[Names.RPDU["RPUDTYPE"]] = Field.Field(Names.RPDU["RPUDTYPE"], self)
		self.myFields[Names.RPDU["RPCAUSELEN"]] = Field.Field(Names.RPDU["RPCAUSELEN"], self, self.encodeRPCauseLength)
		self.myFields[Names.RPDU["RPCAUSE"]] = Field.Field(Names.RPDU["RPCAUSE"], self)	
		
	def update(self, fieldnames, varname, value):
		if fieldnames == "":
			pass
		else:
			super(RPDU, self).update(fieldnames, varname, value)

###############################
# ENCODERS:	
		
	def encodeRPCauseLength(self, field=""):      
		l = 0
		l += self.myFields[Names.RPDU["RPCAUSE"]].getEncodedOctetCount()
		return "%0.2X" % l

	def encodeRPOALength(self, field=""):      
		l = 0
		l += self.myFields[Names.RPDU["RPOA"]].myFields[Names.RPDU["RPOANO"]].getEncodedOctetCount()
		return "%0.2X" % l

	def encodeRPDALength(self, field=""):      
		l = 0
		l += self.myFields[Names.RPDU["RPDA"]].myFields[Names.RPDU["RPDANO"]].getEncodedOctetCount()
		return "%0.2X" % l

	def encodeRPUDL(self, field=""):
		l = 0
		l += self.myParent.getOctetCountAfter(self.myName)
		return "%0.2X" % l

###############################

	def getMTI(self):
		# Just one of the many corrections that will have to be made. The first byte
		# in the RP layer is: "RP-Message Type" (TS 124 011)
		MessageType = self.myFields[Names.RPDU["RPDUMTI"]]
		encoding = int(MessageType.getEncoding(), 16)
		# The first 3 bits in "RP-Message Type" is MTI (Message Type Indicator) 
		MTI = encoding & 0x7
		# The MTI determines what type of RP packet: RP-DATA, RP-ACK, RP-ERROR or RP-SMMA.
		# Each has a unique packet structure.
		return MTI

	# Overrides
	def dump(self, verbosity):
		rstr = ""

		MTI = self.getMTI()
		if verbosity > 0:			
			if MTI == 0 or MTI == 1:
				rstr += "RP-DATA\r\n"
				rstr += Utils.getDash(7) + "\r\n"
			elif MTI == 2 or MTI == 3:
				rstr += "RP-ACK\r\n"
				rstr += Utils.getDash(6) + "\r\n"
			elif MTI == 4 or MTI == 5:
				rstr += "RP-ERR\r\n"
				rstr += Utils.getDash(6) + "\r\n"
			elif MTI == 6:
				rstr += "RP-SMMA\r\n"
				rstr += Utils.getDash(7) + "\r\n"
			else:
				rstr += "%s\r\n"%(Names.Containers["RPDU"])
				rstr += Utils.getDash(len(Names.Containers["RPDU"])) + "\r\n"			
			
		rstr += self.myFields[Names.RPDU["RPDUMTI"]].dump(verbosity)
		rstr += self.myFields[Names.RPDU["RPDUMR"]].dump(verbosity)

		# RP-DATA
		if MTI == 0 or MTI == 1:
			rstr += self.myFields[Names.RPDU["RPOA"]].dump(verbosity)
			rstr += self.myFields[Names.RPDU["RPDA"]].dump(verbosity)
		# RP-ACK
		elif MTI == 2 or MTI == 3:
			rstr += self.myFields[Names.RPDU["RPUDTYPE"]].dump(verbosity) 
		# RP-ERR
		elif MTI == 4 or MTI == 5:
			rstr += self.myFields[Names.RPDU["RPCAUSELEN"]].dump(verbosity) 
			rstr += self.myFields[Names.RPDU["RPCAUSE"]].dump(verbosity) 
			rstr += self.myFields[Names.RPDU["RPUDTYPE"]].dump(verbosity) 

		if MTI != 6:
			rstr += self.myFields[Names.RPDU["RPUDL"]].dump(verbosity)

		return rstr


	
