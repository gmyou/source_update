#!/bin/bash

# arg[0] : Project Name $1

if [ $# -eq 0 ]
  then
    echo "No Arguments Supplied, Require Project Name. (ex. ./source_recover.sh Suggest_Trend)"
    exit
fi

rm -f -r $1
mv $1_old/ $1
rm -f $1.tar.gz
