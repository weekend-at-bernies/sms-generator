import Field

class FieldContainer(object):

	myName = ""
	myParent = ""
	myFields = ""

	def __init__(self, name="", parent=""):
		self.myName = name
		self.myParent = parent
		self.myFields = {}
	
	def update(self, fieldnames, varname, value):
		currfield = ""	
		currfields = self.myFields		
		for fieldname in fieldnames:
			currfield = currfields[fieldname]
			currfields = currfield.myFields
		currfield.update(varname, value)
		

	def __str__(self):
		return self.myName

	def dump(self, verbosity):
		rstr = ""
		for field in myFields:
			rstr += field.dump(verbosity)
		return rstr

	# Encoding == decoding, return the decoded data
	def encodeDecode(self, field):
		return field.decoded

	def getEncodedOctetCount(self):
		encoded = self.dump(False)
		return len(encoded) / 2


		
				
