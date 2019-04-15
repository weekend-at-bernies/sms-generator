import Field
import FieldContainer
import Names
import Utils
import OrderedField

class UD(FieldContainer.FieldContainer):
	
	IEcount = 0
	currIE = ""

	def __init__(self, name, parent):
		super(UD, self).__init__(name, parent)
		self.myFields[Names.UD["UDL"]] = Field.Field(Names.UD["UDL"], self, self.encodeUDL)		
		self.myFields[Names.UD["UDHL"]] = Field.Field(Names.UD["UDHL"], self, self.encodeUDHL)
		self.myFields[Names.UD["USRDATA"]] = Field.Field(Names.UD["USRDATA"], self, self.encodeUD)
		
		
	def update(self, fieldnames, varname, value):
		newfieldnames = ""
		IEname = ""		
		if fieldnames == "":
			pass
		else:	
			if Names.UD["IE"] in fieldnames:
				IEname = Names.UD["IE"] + "%d"%(self.IEcount)
				newfieldnames = fieldnames
				newfieldnames.pop(0)
				newfieldnames = [IEname] + newfieldnames
				if Names.UD["IELEN"] in fieldnames:
					if Names.Common["NEEDSENCODING"] == varname:
						self.IEcount += 1
						IEname = Names.UD["IE"] + "%d"%(self.IEcount)
						self.currIE = OrderedField.OrderedField(IEname, self, "", [Names.UD["IETYPE"], Names.UD["IELEN"], Names.UD["IEDATA"]])				
						self.currIE.myFields[Names.UD["IELEN"]] = Field.Field(Names.UD["IELEN"], self.currIE, self.encodeIELEN)
						self.currIE.myFields[Names.UD["IETYPE"]] = Field.Field(Names.UD["IETYPE"], self.currIE)
						self.currIE.myFields[Names.UD["IEDATA"]] = Field.Field(Names.UD["IEDATA"], self.currIE, self.encodeDecode)
						self.myFields[IEname] = self.currIE
						newfieldnames = [IEname, Names.UD["IELEN"]]				
			else:
				newfieldnames = fieldnames
			super(UD, self).update(newfieldnames, varname, value)
		
###############################
# ENCODERS:

	def encodeUDL(self, field=""):
		l = 0
		l += self.myFields[Names.UD["UDHL"]].getEncodedOctetCount()
		for i in range(0, self.IEcount):					
			l += self.myFields[Names.UD["IE"] + "%d"%(i + 1)].getEncodedOctetCount()
		l += self.myFields[Names.UD["USRDATA"]].getEncodedOctetCount()
		l += self.myParent.getOctetCountAfter(self.myName)
		if self.myParent.defines7bitEncoding() == True: 
			l = Utils.toSeptetCount(l)
		return "%0.2X" % l

		
	def encodeUDHL(self, field=""):
		l = 0;
		for i in range(0, self.IEcount):
			l += self.myFields[Names.UD["IE"] + "%d"%(i + 1)].getEncodedOctetCount() 
		return "%0.2X" % l

	def encodeIELEN(self, field):      
		l = 0
		myIE = field.myParent
		l += self.myFields[myIE.myName].myFields[Names.UD["IEDATA"]].getEncodedOctetCount()
		return "%0.2X" % l


	def encodeUD(self, field):
		encoding = ""
		data = field.decoded
		if self.myParent.defines7bitEncoding() == True: 
# Do we have a User Data Header?
			if self.hasUDH() == True:
# Yes. OK bit trickier.
# NOTE: '+1' is a bug. For some reason '+IEcount' is the correct calculation. 
				encoding = Utils.encode7bit(data, (int(self.myFields[Names.UD["UDHL"]].getEncoding(), 16) + self.IEcount))
# These are equivalent: 
#				encoding = Utils.encode7bit(data, (int(self.encodeUDHL(), 16) + 1))
#				encoding = Utils.encode7bit(data, (int(self.myFields[Names.UD["UDHL"]].getEncoding(), 16) + 1))
			else:
# No. Well that's easy then. Encode all of UD.
				encoding = Utils.encode7bit(data)
		return encoding

###############################

	def hasUDH(self):
		if self.myFields[Names.UD["UDHL"]].getEncodedOctetCount() > 0:
			return True
		return False

	# Overrides
	def dump(self, verbosity):
		rstr = ""

		if verbosity > 0:
			rstr += "%s\r\n"%(Names.Containers["UD"])
			rstr += Utils.getDash(len(Names.Containers["UD"])) + "\r\n"
				
		rstr += self.myFields[Names.UD["UDL"]].dump(verbosity)
		rstr += self.myFields[Names.UD["UDHL"]].dump(verbosity)
		for i in range(0, self.IEcount):
			rstr += self.myFields[Names.UD["IE"] + "%d"%(i + 1)].dump(verbosity) 
		rstr += self.myFields[Names.UD["USRDATA"]].dump(verbosity)

		return rstr

	
		
