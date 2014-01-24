#!/bin/bash

# condition[0] : Project Existed Driectory (/usr/local/workspace)
# condition[1] : Srouce File (~/$1.tar.gz)
# arg[0] : Project Name $1

if [ $# -eq 0 ]
  then
    echo "No Arguments Supplied, Require Project Name. (ex. ./source_update.sh Suggest_Trend)"
    exit
fi

cd /usr/local/workspace
rm -f -r ./$1_old
rm -f $1.tar.gz
mv ./$1 $1_old
cp ~/$1.tar.gz .
tar -xvzf $1.tar.gz
chown -R root:root ./$1
cp ./$1_old/src/log4j.xml ./$1/src
cp ./$1_old/web/WEB-INF/web.xml ./$1/web/WEB-INF/web.xml
cp ./$1_old/web/WEB-INF/conf/applicationContext.xml ./$1/web/WEB-INF/conf/applicationContext
mkdir ./$1/web/WEB-INF/classes
rm -f $1.tar.gz