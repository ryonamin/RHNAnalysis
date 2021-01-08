#!/usr/bin/python
import os,shutil,conf,makeSteeringFiles

# This is the main script.

def makeDirectory(dirname):
	if not os.path.exists(dirname):
		os.mkdir(dirname)
			
# prepare directories if necessary
makeDirectory(conf.XMLDIR)
makeDirectory(conf.OUTDIR_SLCIO)

lastEvt = 0 
print "Total events = " + str(conf.nMaxEvt)
print "lastEvent = " + str(lastEvt)
fileId = 1
while (1):
	if lastEvt < conf.nMaxEvt:
		makeSteeringFiles.writeXMLs(fileId,lastEvt,conf.nEvtsInFile);
		lastEvt = lastEvt + conf.nEvtsInFile
		fileId = fileId + 1
	else :
		break;

