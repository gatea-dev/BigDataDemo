#!/bin/bash

NROW=60
TYPE=RecordUDP
SKIP=09:29:45
DATE=`ls | grep 2020 | head -1`
clear
#
# Tapes
#
DIR='Tapes : '
for dir in `ls | grep 2020`; do
   DIR="${DIR} ${dir}"
done
echo ${DIR}
#
# Input from user w/ defaults
#
read -p "Date [${DATE}]: " dt
read -p "Skip [${SKIP}]: " sk
dt=${dt:-${DATE}} ; DATE=${dt}
sk=${sk:-${SKIP}} ; SKIP=${sk}
FILE=./${DATE}/mon/${TYPE}-qchic209.out.gz

## echo "./py/DumpMon.py ${FILE} -rows ${NROW} ${XTRA} -s ${SKIP}" ; sleep 1
./py/DumpMon.py ${FILE} -rows ${NROW} ${XTRA} -s ${SKIP}
