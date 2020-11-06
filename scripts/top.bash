#!/bin/bash

FILE=./20201102/top/RecordUDP-qpic209.out
NROW=60
XTRA=""
if [ -n "${1}" ]; then
   FILE=$1
   if [ -n "${2}" ]; then
      NROW=$2
      if [ -n "${3}" ]; then
         XTRA=$3
      fi
   fi
fi
./py/DumpMon.py ${FILE} -top True -rows ${NROW} ${XTRA}
