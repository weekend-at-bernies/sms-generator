import SMS
import RPDU
import Envelope
import UD
import WSP
import WBXML
import SIMCmd
import MMS
import Names
import Utils

class OverallSMS:

	myContainers = {}

	myWBXMLFile = ""
	myWSPFile = ""
	myUDFile = ""
	myRPDUFile = ""
        mySIMCmdFile = ""
	myMMSFile = ""
	myEnvelopeFile = ""

	containerNameOrder = [ 
			       Names.Containers["ENVELOPE"],
			       Names.Containers["RPDU"],
			       Names.Containers["SMS"],
			       Names.Containers["UD"],
			       Names.Containers["WSP"],
			       Names.Containers["WBXML"],
			       Names.Containers["SIMCMD"],
			       Names.Containers["MMS"],	
			     ]

	def getContainer(self, containername):
		if containername in self.myContainers:
			return self.myContainers[containername]
		else:
			return None
	
	def update(self, containername, fieldnames, varname, value):
		container = self.getContainer(containername)
		if container != None:
			container.update(fieldnames, varname, value)		
	
	def addNewContainer(self, containername):
		if containername == Names.Containers["SMS"]:
			self.myContainers[containername] = SMS.SMS(containername, self)
		elif containername == Names.Containers["RPDU"]:
			self.myContainers[containername] = RPDU.RPDU(containername, self)
		elif containername == Names.Containers["UD"]:
			self.myContainers[containername] = UD.UD(containername, self)
		elif containername == Names.Containers["WSP"]:
			self.myContainers[containername] = WSP.WSP(containername, self)
		elif containername == Names.Containers["WBXML"]:
			self.myContainers[containername] = WBXML.WBXML(containername, self)
		elif containername == Names.Containers["SIMCMD"]:
			self.myContainers[containername] = SIMCmd.SIMCmd(containername, self)
		elif containername == Names.Containers["MMS"]:
			self.myContainers[containername] = MMS.MMS(containername, self)
		elif containername == Names.Containers["ENVELOPE"]:
			self.myContainers[containername] = Envelope.Envelope(containername, self)

	def __init__(self):
		pass

	 	
	def getOctetCountAfter(self, containername):
		index = self.containerNameOrder.index(containername)
		index += 1
		count = 0
		while index < len(self.containerNameOrder):
			currname = self.containerNameOrder[index]
			container = self.getContainer(currname)
			if container != None:
				count += self.myContainers[currname].getEncodedOctetCount()				
			index +=1
		return count

	def getEncodedOctetCount(self, containername=""):
		count = 0
		container = self.getContainer(containername)
		if container != None:
			count = container.getEncodedOctetCount()
		elif containername == "":
			for k in self.myContainers:
				container = self.myContainers[k]
				count += container.getEncodedOctetCount()
		return count
		
		
	def defines7bitEncoding(self):
		container = self.getContainer(Names.Containers["SMS"])
		if container != None:
			return container.defines7bitEncoding()

	
	def defines8bitEncoding(self):
		container = self.getContainer(Names.Containers["SMS"])
		if container != None:
			return container.defines8bitEncoding()

	def dumpContainer(self, containername, verbosity):
		rstr = ""
		container = self.getContainer(containername)
		if container != None:
			if container.getEncodedOctetCount() > 0:
				rstr += container.dump(verbosity)
				if (verbosity > 0):
					rstr += "\r\n"
					rstr += container.dump(False) + " (%d)\r\n\r\n"%(container.getEncodedOctetCount())
		return rstr

	def dump(self, verbosity):
		rstr = ""
		if (verbosity > 0):
			rstr += "\r\n"

		for containerName in self.containerNameOrder:
			rstr += self.dumpContainer(containerName, verbosity)

		if (verbosity > 0):
			rstr += "\r\nOverall\r\n" + Utils.getDash(7) + "\r\n"
			for containerName in self.containerNameOrder:
				rstr += self.dumpContainer(containerName, False)
			rstr += " (%d)\r\n"%(self.getEncodedOctetCount())

		return rstr
	


			
		
