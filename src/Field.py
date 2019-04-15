import Names
import Utils

class Field(object):

	myName = ""
	needsEncoding = ""
	encoded = ""
	decoded = ""
	myParent = ""
	myEncoder = ""
	myFields = ""
	myDissector = ""

	def __init__(self, name="", parent="", encoder="", dissector=""):
		self.myName = name
		self.myParent = parent	
		self.myEncoder = encoder
		self.needsEncoding = False
		self.myFields = {}
		self.myDissector = dissector
		
	def getEncoding(self):
		encoding = ""
		if len(self.myFields) > 0:
			for k in self.myFields.keys():
				encoding += self.myFields[k].getEncoding()
		else:
			if (self.needsEncoding == False):
				encoding = self.encoded
			else:
				encoding = self.myEncoder(self)
		return encoding

	def update(self, varname, value):
		if varname == Names.Common["NEEDSENCODING"]:
			self.needsEncoding = value
		elif varname == Names.Common["ENCODED"]:
			self.encoded = value
		elif varname == Names.Common["DECODED"]:
			self.decoded = value
		elif varname == Names.Common["MYENCODER"]:
			self.myEncoder = value

	def getEncodedOctetCount(self):
		encoded = self.getEncoding()
		return len(encoded) / 2

	def getEncodedNibbleCount(self):
		encoded = self.getEncoding()
		return len(encoded)

	def getEncodedSeptetCount(self):
		encoded = self.getEncoding()
		return Utils.toSeptetCount(len(encoded) / 2)

	def __str__(self):
		return self.myName

	def dump(self, verbosity, indent=0):
		rstr = ""
		if len(self.myFields) > 0:
			if verbosity > 0:
				rstr += Utils.addIndent(self.myName, indent) + ": " + self.getEncoding()
				if self.getEncodedOctetCount() > 0:
					rstr += " (%d)"%(self.getEncodedOctetCount())
				rstr += "\r\n"				
			for k in self.myFields.keys():
				rstr += self.myFields[k].dump(verbosity, (indent+2))
		else:
			if verbosity > 0:
				rstr += Utils.addIndent(self.myName, indent) + ": "
			rstr += self.getEncoding()
			if verbosity > 0:
				if self.getEncodedOctetCount() > 0:
					rstr += " (%d)"%(self.getEncodedOctetCount())
				rstr += "\r\n"
			if (verbosity > 1) and (self.myDissector != ""):
				strs = self.myDissector(self)
				for s in strs:
					rstr += Utils.addIndent((s + "\r\n"), (indent+2))
		return rstr
