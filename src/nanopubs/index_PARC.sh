#!/bin/sh
NP="../np"
cat ./Factbank/results/texts/trusty.*-document.trig > parc-documents-temp.trig
cat ./Factbank/results/texts/trusty.*-text.trig > parc-text-temp.trig
cat ./PARC/results/texts/trusty.*parc_word.trig > parc-word-temp.trig
cat parc-*-temp.trig > all_texts-temp.trig
TEXTINDEX=$($NP mkindex -t "PARC text nanopublications" -d "Index nanopublication containing all text nanopublications that are part of the PARC corpus." -c "https://orcid.org/0000-0002-3429-2879" -a "https://www.aclweb.org/anthology/L16-1619.pdf" -u "https://w3id.org/provcorp/np/public/index/text-corpus/" -o ./PARC/results/index-parc_texts.trig all_texts-temp.trig)
echo "${TEXTINDEX}"
rm parc-documents-temp.trig
rm parc-text-temp.trig
rm parc-word-temp.trig
rm ./all_texts-temp.trig

cat ./PARC/results/annotations/trusty.*.trig > parc-annotations_temp.trig

ANNOTATIONINDEX=$($NP mkindex -t "PARC annotations nanopublications" -d "Index nanopublication containing all annotation nanopublications of the parc corpus." -c "https://orcid.org/0000-0002-3429-2879" -a "https://www.aclweb.org/anthology/L16-1619.pdf" -u "https://w3id.org/provcorp/np/public/index/annotation-corpus/" -o ./PARC/results/index-parc_all_annotations.trig parc-annotations_temp.trig)
rm ./parc-annotations_temp.trig

cd PARC
python3 ./generate-parc_corpus.py -a "${ANNOTATIONINDEX}" -t "${TEXTINDEX}"
$NP mktrusty -r ./results/parc_text_corpus.trig
$NP mktrusty -r ./results/parc_annotation_corpus.trig
