#!/usr/bin/python

# Input files will be chosen from the follwoing directory.
LISTDIR="/home/ilc/yonamine/work/LCFIPlusDev/run/dbd91GeV_gen/SplitLcioFile/slcio"
# Input file suffix
FILESUFFIX="slcio"
# samples will be chosen by searching the follwoing strings in the file names under LISTDIR directories.
PROCESSES=["Pe1qqe1qq.eLpR"]
#PROCESSES=["Pe1qqe1qq.eLpR","Pe1qqe1qq.eRpL","Pe2qqe2qq.eLpR","Pe2qqe2qq.eRpL","Pe3qqe3qq.eLpR","Pe3qqe3qq.eRpL"]

# Number of files per one submit (Number of input files incerted in one Marlin-steering file by makeSteeringFiles.py) 
# This should be small for heavy tasks e.g. full detector simulation.
nfilesInOneshot = 1; 

# Normally, no need to change below
# common
TEMPLATEXMLORIGDIR="./template_steer"
LOGDIR = "log"
XMLDIR = "generatedXMLs"
TEMPLATEDIR = "templateXMLs"
OUTDIR_SLCIO="slcio"
SPACE = "             "

TEMPLATEFILE = "sgv_ild_lcio_extread.steer"
OUTPUT_PREFIX="sgv."

