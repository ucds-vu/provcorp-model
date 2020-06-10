#! /bin/sh
NP="../np"
echo "WORKING on FACTBANK"
cd Factbank
sh ./run.sh $1
echo "MAKING FILES TRUSTY"
cd ../
$NP mktrusty -R ./Factbank/results/texts/$2-text.trig ./Factbank/results/texts/$2-document.trig ./Factbank/results/texts/$2-fb_word.trig ./Factbank/results/annotations/$2-fb_event.trig ./Factbank/results/annotations/$2-fb_factvalue.trig
