
class Parser(object):

	myOverallSMS = ""
	myError = ""
	myName = ""

	def __init__(self, overallSMS):
		self.myOverallSMS = overallSMS
		self.myOverallSMS.addNewContainer(self.myName)
		
	def update(self, fieldnames, varname, value):
		self.myOverallSMS.update(self.myName, fieldnames, varname, value)

	
