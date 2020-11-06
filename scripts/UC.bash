#!/bin/bash

NROW=60
SKIP=09:29:45
DATE=20201102
XTRA="-o Capacity,GIF,ARCAB,ICE"

clear
read -p "Date [${DATE}]: " dt
read -p "Skip [${SKIP}]: " sk
dt=${dt:-${DATE}} ; DATE=${dt}
sk=${sk:-${SKIP}} ; SKIP=${sk}
FILE=./${DATE}/mon/UC-quodd173.out.gz

./py/DumpMon.py ${FILE} -rows ${NROW} ${XTRA} -s ${SKIP}
