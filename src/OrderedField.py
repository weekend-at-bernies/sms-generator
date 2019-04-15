import Names
import Field
import Utils

class OrderedField(Field.Field):

        myOrderedFieldNames = ""

        def __init__(self, name="", parent="", encoder="", orderedFieldNames=""):
		self.myOrderedFieldNames = orderedFieldNames
                super(OrderedField, self).__init__(name, parent, encoder)

	def getEncoding(self):
		encoding = ""
		for fieldName in self.myOrderedFieldNames:
			encoding += self.myFields[fieldName].getEncoding()
		return encoding

	def dump(self, verbosity, indent=0):
		rstr = ""
		if verbosity > 0:
			rstr += Utils.addIndent(self.myName, indent) + ": " + self.getEncoding()
			if self.getEncodedOctetCount() > 0:
				rstr += " (%d)"%(self.getEncodedOctetCount())
			rstr += "\r\n"
		for fieldName in self.myOrderedFieldNames:
			rstr += self.myFields[fieldName].dump(verbosity, indent+2)
		return rstr

