import Field
import FieldContainer
import Names
import Utils
import OrderedField

class WSP(FieldContainer.FieldContainer):
	

	def __init__(self, name, parent):
		super(WSP, self).__init__(name, parent)
		self.myFields[Names.WSP["WSPTID"]] = Field.Field(Names.WSP["WSPTID"], self)
		self.myFields[Names.WSP["WSPTYPE"]] = Field.Field(Names.WSP["WSPTYPE"], self)
		self.myFields[Names.WSP["WSPHL"]] = Field.Field(Names.WSP["WSPHL"], self, self.encodeWSPHL)
		self.myFields[Names.WSP["WSPCONTTYPE"]] = Field.Field(Names.WSP["WSPCONTTYPE"], self, self.encodeDecode)
		self.myFields[Names.WSP["WSPHDRS"]] = Field.Field(Names.WSP["WSPHDRS"], self, self.encodeDecode)
		
	def update(self, fieldnames, varname, value):
		if fieldnames == "":
			pass
		else:
			super(WSP, self).update(fieldnames, varname, value)

###############################
# ENCODERS:	
		
	def encodeWSPHL(self, field=""):      
		l = 0
		l += self.myFields[Names.WSP["WSPCONTTYPE"]].getEncodedOctetCount()
		l += self.myFields[Names.WSP["WSPHDRS"]].getEncodedOctetCount()
		return "%0.2X" % l


###############################

	# Overrides
	def dump(self, verbosity):
		rstr = ""

		if verbosity > 0:
			rstr += "%s\r\n"%(Names.Containers["WSP"])
			rstr += Utils.getDash(len(Names.Containers["WSP"])) + "\r\n"
				
		rstr += self.myFields[Names.WSP["WSPTID"]].dump(verbosity)
		rstr += self.myFields[Names.WSP["WSPTYPE"]].dump(verbosity)
		rstr += self.myFields[Names.WSP["WSPHL"]].dump(verbosity)
		rstr += self.myFields[Names.WSP["WSPCONTTYPE"]].dump(verbosity)
		rstr += self.myFields[Names.WSP["WSPHDRS"]].dump(verbosity)

		return rstr

	
		
