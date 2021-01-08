#!/user/bin/python

import sys

print "How to run:"
print "python makeRunDirectoryExtread.py <TopDirName> <Input file> <File Id(used for dirname etc)>" 

import os
def makeDirectory(dirname):
	if not os.path.exists(dirname):
		os.mkdir(dirname)
		print "Created a new dierctory : " + dirname
	else :
		print dirname + " is already exist. Change RunId or remove the existing one."

def checkArgument():
	if len(sys.argv) < 4 :
		print "Some arguments missing. abort."
		sys.exit()
	elif len(sys.argv) > 4 :
		print "Too many arguments. abort."
		sys.exit()
	else :
		print "Top Dir Name : " + sys.argv[1]
		print "Input File   : " + sys.argv[2]
		print "Base Name    : " + sys.argv[3]

		if not os.path.exists(sys.argv[1]+"/fort.51"):
			print "No fort.51 found."
			print "Put fort.51 (detector file) into " + sys.argv[1] +"."
			sys.exit()

import re 
def makeSteerFile(dirname):
	inputfile = sys.argv[2]
	basename = sys.argv[3] 
	ofname = dirname + "/" + basename + "/fort.17" # will be used as steering file
	fout = open(ofname,'w')
	#template = open("template_steer/sgv_ild_lcio_template.steer",'r')
	template = open("template_steer/sgv_ild_lcio_extread.steer",'r')
	for t in template:
		if re.search("__OUTPUTLCIO__",t):
			tmp = re.sub("__OUTPUTLCIO__",basename+"_SGV"+".slcio",t)
			fout.write(tmp)
		elif re.search("__PROCESSNAME__",t):
			if "Pbb" in basename:
				tmp = re.sub("__PROCESSNAME__","bbar",t)
			elif "Pcc" in basename:
				tmp = re.sub("__PROCESSNAME__","ccar",t)
			elif "Pqq" in basename:
				tmp = re.sub("__PROCESSNAME__","qqar",t)
			fout.write(tmp)
		elif re.search("__INPUTFILES__",t):
			tmp = re.sub("__INPUTFILES__",inputfile,t)
			fout.write(tmp)
		else:
			fout.write(t)
			

# Main 
checkArgument()
dirName = sys.argv[1]
#seed = 19780503 + int(sys.argv[3]) 
#print "Seed : " + str(seed)
inputfile = sys.argv[2]
basename = sys.argv[3] 
makeDirectory(dirName)
makeDirectory(dirName+"/"+basename)
makeSteerFile(dirName)

import subprocess
output=subprocess.Popen(["pwd"],stdout=subprocess.PIPE)
response=output.communicate()
curDir = response[0].rstrip('\n')
os.system('ln -s ' + curDir + '/' + sys.argv[1] + '/fort.51 ' + curDir + '/' + dirName + "/" + basename + '/fort.51')
