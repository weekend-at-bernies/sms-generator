import os
import shutil

# This parses an .ini file.
# An .ini file is a bunch of statements like this:
# x1=val1
# x2=val2
# ... etc.
# Comments are denoted with a '%' and are ignored.
# This will return a list like this: [ [x1,val1], [x2,val2], ... etc. ]
# Otherwise [] is returned.
def getIniData(inputfile):   
	inidata = []
	try:
		f = open(inputfile, 'r')
		lines = f.readlines()
		f.close()

		for line in lines:
			line = line.strip(' \t\n\r')
			if (len(line) > 0):
				if (line.startswith('%') == False):
					inidata.append(line.split('='))
	except:
		pass
	return inidata


class IniHandler():

	inifilename = ""
	members = []

	# It is the responsibility of the caller to sanitize 'inputfile'.
	def __init__(self, inputfile):
		self.inifilename = inputfile
		self.members = getIniData(self.inifilename)	


	# Update an .ini member
	# There could be multiple member names, eg.
        # IELength=5
	# ...
	# IELength=4
	# 'index' (0-based) is used to differentiate them 
	def update(self, membername, newval, index=0):
		hitcount = 0
		for member in self.members:
			if member[0] == membername:
				if hitcount == index:
					member[1] = newval
					break
				else:
					hitcount += 1	

	# Dumps the .ini.
	# If outputfile == "": only print the dumped .ini (no file writing).
	# Otherwise write to outputfile (if it exists, you have to set the overwrite flag explicitly)
	def dump(self, outputfile, overwrite=False):
		strs = []

		for member in self.members:
			strs.append(member[0] + "=" + member[1])
			
		if outputfile == "":
			for s in strs:
				print s
			return True

		if os.path.exists(outputfile) and not overwrite:
			return False

		try:
	 		with open(outputfile, "w") as f:
				for s in strs:
					f.write(s + "\n")
				f.close()
		except:
			return False

		return True		

				
	
