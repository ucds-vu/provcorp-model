#!/usr/bin/env bash
TEXT="../corpora/factbank_v1/data/original/"
python3 ./main.py -a $1 -t $TEXT$1
