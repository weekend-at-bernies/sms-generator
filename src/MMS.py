import Field
import FieldContainer
import Names
import Utils
import OrderedField

class MMS(FieldContainer.FieldContainer):
	

	def __init__(self, name, parent):
		super(MMS, self).__init__(name, parent)
		self.myFields[Names.MMS["MSGTYPE"]] = Field.Field(Names.MMS["MSGTYPE"], self)
		self.myFields[Names.MMS["TID"]] = Field.Field(Names.MMS["TID"], self)
		self.myFields[Names.MMS["VERS"]] = Field.Field(Names.MMS["VERS"], self)
		self.myFields[Names.MMS["FROM"]] = Field.Field(Names.MMS["FROM"], self)
		self.myFields[Names.MMS["SUBJ"]] = Field.Field(Names.MMS["SUBJ"], self)
		self.myFields[Names.MMS["MSGCLS"]] = Field.Field(Names.MMS["MSGCLS"], self)
		self.myFields[Names.MMS["MSGSIZE"]] = Field.Field(Names.MMS["MSGSIZE"], self)
		self.myFields[Names.MMS["EXP"]] = Field.Field(Names.MMS["EXP"], self)
		self.myFields[Names.MMS["CNTLOC"]] = Field.Field(Names.MMS["CNTLOC"], self)
		
	def update(self, fieldnames, varname, value):
		if fieldnames == "":
			pass
		else:
			super(MMS, self).update(fieldnames, varname, value)

###############################
# ENCODERS:	
		


###############################

	# Overrides
	def dump(self, verbosity):
		rstr = ""

		if verbosity > 0:
			rstr += "%s\r\n"%(Names.Containers["MMS"])
			rstr += Utils.getDash(len(Names.Containers["MMS"])) + "\r\n"
				
		rstr += self.myFields[Names.MMS["MSGTYPE"]].dump(verbosity)
		rstr += self.myFields[Names.MMS["TID"]].dump(verbosity)
		rstr += self.myFields[Names.MMS["VERS"]].dump(verbosity)
		rstr += self.myFields[Names.MMS["FROM"]].dump(verbosity)
		rstr += self.myFields[Names.MMS["SUBJ"]].dump(verbosity)
		rstr += self.myFields[Names.MMS["MSGCLS"]].dump(verbosity)
		rstr += self.myFields[Names.MMS["MSGSIZE"]].dump(verbosity)
		rstr += self.myFields[Names.MMS["EXP"]].dump(verbosity)
		rstr += self.myFields[Names.MMS["CNTLOC"]].dump(verbosity)

		return rstr

	
		
