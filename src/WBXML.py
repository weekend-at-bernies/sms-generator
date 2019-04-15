import Field
import FieldContainer
import Names
import Utils
import OrderedField
import os

class WBXML(FieldContainer.FieldContainer):
	
	myWBXMLVersion = ""

	def __init__(self, name, parent):
		super(WBXML, self).__init__(name, parent)
		self.myFields[Names.WBXML["WBXML"]] = Field.Field(Names.WBXML["WBXML"], self, self.encodeXMLtoWBXML)
		
	def update(self, fieldnames, varname, value):
		if fieldnames == "":
			if varname == Names.WBXML["WBXMLVERS"]:
				self.myWBXMLVersion = value
		else:
			super(WBXML, self).update(fieldnames, varname, value)

###############################
# ENCODERS:	
	
	def encodeXMLtoWBXML(self, field):
		version = ""
		inputfile = field.decoded
		if (os.path.exists(inputfile) == False):
			print "Error: cannot find file: %s"%(inputfile)
			sys.exit()
		
		if self.myWBXMLVersion == "1":
			version = "1.1"
		elif self.myWBXMLVersion == "2":
			version = "1.2"
		elif self.myWBXMLVersion == "3":
			version = "1.3"
		else:
			version = "1.0"

		#return Utils.xml2wbxml_noversionsupport(inputfile)
		return Utils.xml2wbxml(inputfile, version)
		
###############################

	# Overrides
	def dump(self, verbosity):
		rstr = ""

		if verbosity > 0:
			rstr += "%s\r\n"%(Names.Containers["WBXML"])
			rstr += Utils.getDash(len(Names.Containers["WBXML"])) + "\r\n"
				
		rstr += self.myFields[Names.WBXML["WBXML"]].dump(verbosity)

		return rstr

	
		
