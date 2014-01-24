# -*- coding: utf-8 -*-
# source_update.py

import os, sys, shutil
import tarfile

# arg[0] : Project Existed Driectory (ex. /usr/local/workspace)
# arg[1] : Project Name Suggest_Trend
# arg[2] : Srouce File (ex. ~/src/Suggest_Trend.tar.gz)

#
# ((!$#)) && echo No arugments supplied! && exit 1
#

dirname = "/usr/local/workspace/"
proname = "Suggest_Trend"
srcpath = "~/"

if srcpath.startswith('~'):
	srcpath = os.path.expanduser('~')
	#print srcpath

oprname = proname+"_old/"
zprname = proname+".tar.gz"

filepath = os.path.abspath(os.path.join(dirname, proname))
oldpath = os.path.abspath(os.path.join(dirname, oprname))
sourcefile = os.path.abspath(os.path.join(dirname, zprname))
sourcepath = os.path.abspath(os.path.join(srcpath, zprname))

# {PROJECT}_old 있으면 지우기
try:
	if oldpath.startswith(dirname):
	   os.rmdir(oldpath)
except OSError, e:
	pass
	#print ("Error: %s - %s."%(e.filename, e.strerror))

# {PROJECT}.tar.gz 있으면 지우기
try:
	if sourcefile.startswith(dirname):
	   os.remove(sourcefile)
except OSError, e:
	pass
	#print ("Error: %s - %s."%(e.filename, e.strerror))

# 기존 {PROJECT} {PROJECT}_old 이동, 실패시 exit
try:
	if filepath.startswith(dirname):
	   os.rename(filepath, oldpath)
except OSError, e:
	#pass
	print ("Error: %s - %s."%(e.filename, e.strerror))
	exit

# {PROJECT}.tar.gz 있으면 가져오기, 없으면 exit
# {PROJECT}.tar.gz 압축 풀기, 실패시 exit
try:
	if sourcepath.endswith(zprname):
	   shutil.copy(sourcepath, sourcefile)
	   exittfile = tarfile.open(str(sourcefile), 'r:gz')
	   tfile.extractall('.')
except OSError, e:
	#pass
	print ("Error: %s - %s."%(e.filename, e.strerror))
	exit

	

"""
# if ( existed ) then 
rm -f -r ./Suggest_Trend_old
# if ( existed ) then 
rm -f Suggest_Trend.tar.gz
mv ./Suggest_Trend Suggest_Trend_old
cp /Users/gmyou/Suggest_Trend.tar.gz .

tar -xvzf Suggest_Trend.tar.gz

chown -R root:root ./Suggest_Trend
cp ./Suggest_Trend_old/src/log4j.xml ./Suggest_Trend/src
cp ./Suggest_Trend_old/web/WEB-INF/web.xml ./Suggest_Trend/web/WEB-INF/web.xml
cp ./Suggest_Trend_old/web/WEB-INF/conf/applicationContext.xml ./Suggest_Trend/web/WEB-INF/conf/applicationContext
mkdir ./Suggest_Trend/web/WEB-INF/classes
"""