#!/usr/bin/python
import os,string,shutil,sys,re,conf


def writeXMLs(fileId,lastEvt,nEvtProcess):

	for f in conf.InputFiles:
		basename = (f.split('/')[-1]).split('.slcio')[0]
		oxmlname = conf.XMLDIR + "/"+ basename + "_" + str(fileId) + ".xml"
		oslcioname = basename + "_" + str(fileId) + ".slcio"
		foutxml = open(oxmlname,'w')
		template = open(conf.TEMPLATEDIR+"/"+conf.TEMPLATEFILE,'r')
		for t in template:
			if re.search("__OUTPUTSLCIODIR__/__OUTPUTSLCIO__",t):		
				tmp = re.sub("__OUTPUTSLCIODIR__",conf.OUTDIR_SLCIO,t)
				tmp2 = re.sub("__OUTPUTSLCIO__",oslcioname,tmp)
				foutxml.write(tmp2)
			elif re.search("__MAXEVT__",t):		
				tmp = re.sub("__MAXEVT__",str(nEvtProcess),t)
				foutxml.write(tmp)
			elif re.search("__NSKIPEVT__",t):		
				tmp = re.sub("__NSKIPEVT__",str(lastEvt),t)
				foutxml.write(tmp)
			elif re.search("__INPUTSLCIO__",t):		
				tmp = re.sub("__INPUTSLCIO__",f,t)
				foutxml.write(tmp)
			else:
				foutxml.write(t)


