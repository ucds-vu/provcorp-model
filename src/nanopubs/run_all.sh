#! /bin/sh
NP="../np op filter --out-format nq"
INDEX="../np"
OUTPUT="../data/toLoad/"
#Creating needed directories
mkdir ../data/toLoad
mkdir ./Factbank/results/text
mkdir ./Facbank/results/annotations
mkdir ./PARC/results/text
mkdir ./PARC/results/annotations

echo "DID YOU EMPTY THE FACTBANK TEXT FOLDER?"

python3 create_nanopubs_shared.py

#Creating indexes for factbank
cat ./Factbank/results/texts/trusty.*.trig > factbank-texts-temp.trig

INDEXTEXT=$($INDEX mkindex -t "Factbank text nanopublications" -d "Index nanopublication containing all text nanopublications that are part of the Factbank corpus." -c "https://orcid.org/0000-0002-3429-2879" -a "https://catalog.ldc.upenn.edu/LDC2009T23" -u "https://w3id.org/provcorp/np/public/index/text-corpus/" -o ./Factbank/results/index-factbank_text.trig factbank-texts-temp.trig)
rm ./factbank-texts-temp.trig

cat ./Factbank/results/annotations/trusty*.trig > fb-annotations_temp.trig

INDEXANNOTATION=$($INDEX mkindex -t "Factbank annotation nanopublications" -d "Index nanopublication containing all annotation nanopublications that are part of the Factbank corpus." -c "https://orcid.org/0000-0002-3429-2879" -a "https://catalog.ldc.upenn.edu/LDC2009T23" -u "https://w3id.org/provcorp/np/public/index/annotation-corpus/" -o ./Factbank/results/index-factbank_all_annotations.trig fb-annotations_temp.trig)
rm ./fb-annotations_temp.trig

cd Factbank
python3 ./generate-factbank_corpus.py -a "${INDEXANNOTATION}" -t "${INDEXTEXT}"
$INDEX mktrusty -r ./results/factbank_annotation_corpus.trig
$INDEX mktrusty -r ./results/factbank_text_corpus.trig

cd ../
echo "Making NQuads..."
# FACTBANK
$NP ./Factbank/results/trusty.*corpus.trig > ${OUTPUT}factbank_corpus-nanopubs.nq
$NP ./Factbank/results/texts/trusty.*text.trig > ${OUTPUT}factbank_text-nanopubs.nq
$NP ./Factbank/results/texts/trusty.*document.trig > ${OUTPUT}factbank_document-nanopubs.nq

# separate per source
$NP ./Factbank/results/texts/trusty.wsj_00*word.trig > ${OUTPUT}wsj_00-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_00*event.trig > ${OUTPUT}wsj_00-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_00*factvalue.trig > ${OUTPUT}wsj_00-factbank_factvalue-nanopubs.nq

$NP ./Factbank/results/texts/trusty.wsj_01*word.trig > ${OUTPUT}wsj_01-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_01*event.trig > ${OUTPUT}wsj_01-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_01*factvalue.trig > ${OUTPUT}wsj_01-factbank_factvalue-nanopubs.nq

$NP ./Factbank/results/texts/trusty.wsj_02*word.trig > ${OUTPUT}wsj_02-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_02*event.trig > ${OUTPUT}wsj_02-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_02*factvalue.trig > ${OUTPUT}wsj_02-factbank_factvalue-nanopubs.nq

$NP ./Factbank/results/texts/trusty.wsj_03*word.trig > ${OUTPUT}wsj_03-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_03*event.trig > ${OUTPUT}wsj_03-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_03*factvalue.trig > ${OUTPUT}wsj_03-factbank_factvalue-nanopubs.nq

$NP ./Factbank/results/texts/trusty.wsj_04*word.trig > ${OUTPUT}wsj_04-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_04*event.trig > ${OUTPUT}wsj_04-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_04*factvalue.trig > ${OUTPUT}wsj_04-factbank_factvalue-nanopubs.nq

$NP ./Factbank/results/texts/trusty.wsj_05*word.trig > ${OUTPUT}wsj_05-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_05*event.trig > ${OUTPUT}wsj_05-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_05*factvalue.trig > ${OUTPUT}wsj_05-factbank_factvalue-nanopubs.nq

$NP ./Factbank/results/texts/trusty.wsj_06*word.trig > ${OUTPUT}wsj_06-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_06*event.trig > ${OUTPUT}wsj_06-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_06*factvalue.trig > ${OUTPUT}wsj_06-factbank_factvalue-nanopubs.nq

$NP ./Factbank/results/texts/trusty.wsj_07*word.trig > ${OUTPUT}wsj_07-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_07*event.trig > ${OUTPUT}wsj_07-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_07*factvalue.trig > ${OUTPUT}wsj_07-factbank_factvalue-nanopubs.nq

$NP ./Factbank/results/texts/trusty.wsj_08*word.trig > ${OUTPUT}wsj_08-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_08*event.trig > ${OUTPUT}wsj_08-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_08*factvalue.trig > ${OUTPUT}wsj_08-factbank_factvalue-nanopubs.nq

$NP ./Factbank/results/texts/trusty.wsj_09*word.trig > ${OUTPUT}wsj_09-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_09*event.trig > ${OUTPUT}wsj_09-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_09*factvalue.trig > ${OUTPUT}wsj_09-factbank_factvalue-nanopubs.nq

$NP ./Factbank/results/texts/trusty.wsj_10*word.trig > ${OUTPUT}wsj_10-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_10*event.trig > ${OUTPUT}wsj_10-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.wsj_10*factvalue.trig > ${OUTPUT}wsj_10-factbank_factvalue-nanopubs.nq

$NP ./Factbank/results/texts/trusty.ABC*word.trig > ${OUTPUT}ABC-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.ABC*event.trig > ${OUTPUT}ABC-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.ABC*factvalue.trig > ${OUTPUT}ABC-factbank_factvalue-nanopubs.nq

$NP ./Factbank/results/texts/trusty.AP*word.trig > ${OUTPUT}AP-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.AP*event.trig > ${OUTPUT}AP-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.AP*factvalue.trig > ${OUTPUT}AP-factbank_factvalue-nanopubs.nq

$NP ./Factbank/results/texts/trusty.CNN*word.trig > ${OUTPUT}CNN-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.CNN*event.trig > ${OUTPUT}CNN-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.CNN*factvalue.trig > ${OUTPUT}CNN-factbank_factvalue-nanopubs.nq

$NP ./Factbank/results/texts/trusty.e*word.trig > ${OUTPUT}e-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.e*event.trig > ${OUTPUT}e-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.e*factvalue.trig > ${OUTPUT}e-factbank_factvalue-nanopubs.nq

$NP ./Factbank/results/texts/trusty.NYT*word.trig > ${OUTPUT}NYT-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.NYT*event.trig > ${OUTPUT}NYT-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.NYT*factvalue.trig > ${OUTPUT}NYT-factbank_factvalue-nanopubs.nq

$NP ./Factbank/results/texts/trusty.PRI*word.trig > ${OUTPUT}PRI-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.PRI*event.trig > ${OUTPUT}PRI-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.PRI*factvalue.trig > ${OUTPUT}PRI-factbank_factvalue-nanopubs.nq

$NP ./Factbank/results/texts/trusty.VOA*word.trig > ${OUTPUT}VOA-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.VOA*event.trig > ${OUTPUT}VOA-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.VOA*factvalue.trig > ${OUTPUT}VOA-factbank_factvalue-nanopubs.nq

$NP ./Factbank/results/texts/trusty.XIE*word.trig > ${OUTPUT}XIE-factbank_word-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.XIE*event.trig > ${OUTPUT}XIE-factbank_event-nanopubs.nq
$NP ./Factbank/results/annotations/trusty.XIE*factvalue.trig > ${OUTPUT}XIE-factbank_factvalue-nanopubs.nq
$NP ./Factbank/results/index* > ${OUTPUT}factbank_index-nanopubs.nq

# PARC
$NP ./PARC/results/trusty.*corpus.trig > ${OUTPUT}parc_corpus-nanopubs.nq
$NP ./PARC/results/texts/trusty.wsj_00*word.trig > ${OUTPUT}wsj_00-parc_word-nanopubs.nq
$NP ./PARC/results/annotations/trusty.wsj_00*annotation.trig > ${OUTPUT}wsj_00-parc_annotation-nanopubs.nq

$NP ./PARC/results/texts/trusty.wsj_01*word.trig > ${OUTPUT}wsj_01-parc_word-nanopubs.nq
$NP ./PARC/results/annotations/trusty.wsj_01*annotation.trig > ${OUTPUT}wsj_01-parc_annotation-nanopubs.nq
$NP ./PARC/results/index* > ${OUTPUT}parc_index-nanopubs.nq


#DEFINITIONS
cat ../../np/public/vocab/trusty.*.trig > def_temp.trig

$INDEX mkindex -t "All definition nanopublications" -d "Index nanopublication containing all definition nanopublication used in the other nanopublications." -c "https://orcid.org/0000-0002-3429-2879" -u "https://w3id.org/provcorp/np/public/index/vocab/" -o ./index-definitions.trig def_temp.trig
rm ./def_temp.trig

$NP .../../np/public/vocab/trusty.*.trig > ${OUTPUT}definition-nanopubs.nq
$NP ./index-definitions.trig > ${OUTPUT}definition_index-nanopub.nq
