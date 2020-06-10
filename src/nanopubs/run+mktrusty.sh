#! /bin/sh
NP="../np"
echo "WORKING on FACTBANK"
cd Factbank
sh ./run.sh $1
echo "WORKING on PARC"
cd ../PARC
sh ./run.sh $1 $2

echo "MAKING FILES TRUSTY"
cd ../
$NP mktrusty -R ./Factbank/results/texts/$3-text.trig ./Factbank/results/texts/$3-document.trig ./Factbank/results/texts/$3-fb_word.trig ./Factbank/results/annotations/$3-fb_event.trig ./Factbank/results/annotations/$3-fb_factvalue.trig ./PARC/results/texts/$3-parc_word.trig ./PARC/results/annotations/$3-parc_annotation.trig
