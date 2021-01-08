#!/usr/bin/python

InputFiles=["../E250.Pe1qqe1qq.eLpR_MN20_MZp75.slcio",
            "../E250.Pe1qqe1qq.eRpL_MN20_MZp75.slcio",
            "../E250.Pe2qqe2qq.eLpR_MN20_MZp75.slcio",
            "../E250.Pe2qqe2qq.eRpL_MN20_MZp75.slcio",
            "../E250.Pe3qqe2qq.eLpR_MN20_MZp75.slcio",
            "../E250.Pe3qqe2qq.eRpL_MN20_MZp75.slcio"]

# number of events per file 
nEvtsInFile = 200; 
nMaxEvt     = 10000; 

# no need to change below
# common
TEMPLATEXMLORIGDIR="."
LOGDIR = "log"
XMLDIR = "generatedXMLs"
TEMPLATEDIR = "templateXMLs"
OUTDIR_ROOT="root"
OUTDIR_SLCIO="slcio"
SPACE = "             "

TEMPLATEFILE = "split.xml.in"

