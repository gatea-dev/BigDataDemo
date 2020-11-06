#!/bin/bash

NROW=60
TYPE=RecordUDP
SKIP=09:29:45
DATE=20201102

clear
read -p "Date [${DATE}]: " dt
read -p "Skip [${SKIP}]: " sk
dt=${dt:-${DATE}} ; DATE=${dt}
sk=${sk:-${SKIP}} ; SKIP=${sk}
FILE=./${DATE}/mon/${TYPE}-qchic209.out.gz

./py/DumpMon.py ${FILE} -rows ${NROW} ${XTRA} -s ${SKIP}
