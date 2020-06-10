#! /bin/sh
PATH_NP="../"
ANNOTATIONS="../corpora/PARC3/"
TEXT="../corpora/factbank_v1/data/original/"

python3 main.py -t $TEXT$1 -a $ANNOTATIONS$2  -r -p $PATH_NP -w
