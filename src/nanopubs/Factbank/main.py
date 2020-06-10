from imports import *
def usage():
    print("Options:\n \
    -a / --annotations= (file with the annotations on a certain text)\n \
    -p / --path= (change the path to the nanopublication library)\n \
    -t / --text= (full text document) \n \
    -h / --help")

def main():
    libraryPath = "../../"
    annotations = False
    text = False
    sentences = []
    try:
        options, remainder = getopt.getopt(sys.argv[1:], "a:hp:t:", ['annotations=','help','path=', "text="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    for opt, arg in options:
        if opt in ('-a', '--annotations'):
            annotations = True
            annotationFile = arg
        elif opt in ('-h', '--help'):
            usage()
            sys.exit(0)
        elif opt in ('-p', '--path'):
            libraryPath = arg
        elif opt in ('-t', '--text'):
            text = True
            textFile = arg
        else:
            sys.stderr.write("ERROR: Unhandled option entered\n")
            sys.exit(2)

    #Get basic information
    try:
        currentDate = subprocess.check_output(['./np', 'now'], cwd=libraryPath)
        currentDate = currentDate.decode('utf-8')[:-1]
    except:
        sys.stderr.write("ERROR: Path to nanopublication library is not found or working\nuse -p to change the path\n")
        sys.exit(1)

    if text:
        print("Preprocessing text...")
        textFilename = os.path.basename(textFile)
        preprocessedText = preprocessText(textFile)
        sentences = preprocessedText[1]
        document = preprocessedText[0]
        openText = open(textFile, "r")
        textRead = openText.read()
        startText = textRead.index("<TEXT>") + 7
        endText = textRead.index("</TEXT>") -1
        fullText = textRead[startText:endText]
        textPublication = open(str("./results/texts/") + textFilename[:-4] + str("-text.trig"), "w+")
        tags.textTags()
        generateTextNanopub(textPublication, textFilename[:-4], fullText, document.date, currentDate, "https://w3id.org/provcorp/corpus/factbank-texts", document.journal)
        tags.documentTags()
        documentPublication = open(str("./results/texts/") + textFilename[:-4] + str("-document.trig"), "w+")
        document.generateNanopub(textFilename, documentPublication, currentDate, "https://w3id.org/provcorp/corpus/factbank-texts")
        differenceSentenceNum = getSentenceDifference(sentences, textFilename[:-4])
        #print(differenceSentenceNum)

    if annotations and text:
        print("Preprocessing annotations...")
        eventSentences = getTargetLines(annotationFile[:-4], "fb_event.txt")
        tokensForfile = getTargetLines(annotationFile[:-4], "tokens_tml.txt")
        eventObjects = []
        for event in eventSentences:
            eventObjects.append(Event(event, tokensForfile))

        print("Calculating indexes and generating nanopubs...")
        tags.eventTags()
        tags.wordTags()
        longerSentences = 0
        if "AP9" in annotationFile:
            longerSentences = 1
        annotationPublications = open(str("./results/annotations/") + annotationFile[:-4] + str("-fb_event.trig"), "w+")
        wordPublications = open(str("./results/texts/") + annotationFile[:-4] + str("-fb_word.trig"), "w+")
        for ev in range(len(eventObjects)):
            eventObjects[ev].calculateIndex(sentences, eventObjects[ev].sentenceID - differenceSentenceNum, longerSentences, document.subject)
            eventObjects[ev].generateNanopub(annotationPublications, wordPublications, annotationFile[:-4], "2009-09-15T00:00:00", currentDate,  \
                           "https://w3id.org/provcorp/corpus/factbank-annotations", "https://sites.google.com/site/rosersauri/>, <http://jamespusto.com/", ev, document.journal)

        factValueObjects = []
        sourceSentences = getTargetLines(annotationFile[:-4], "fb_source.txt")
        factvalueSentences = getTargetLines(annotationFile[:-4], "fb_factValue.txt")
        for fact in factvalueSentences:
            factValueObjects.append(FactValue(fact, sourceSentences, differenceSentenceNum))

        tags.factvalueTags()
        factValuePublications = open(str("./results/annotations/") + annotationFile[:-4] + str("-fb_factvalue.trig"), "w+")

        for fct in range(len(factValueObjects)):
            for src_obj in range(len(factValueObjects[fct].source)):
                current_src_obj = factValueObjects[fct].source[src_obj]

                if str(current_src_obj.sourceText) != "AUTHOR" and str(current_src_obj.sourceText) != "GEN" and str(current_src_obj.sourceText) != "DUMMY":
                    current_src_obj.calculateIndex(sentences, current_src_obj.sentenceNum, longerSentences, document.subject)
            factValueObjects[fct].generateNanopub(factValuePublications, annotationFile[:-4], "2009-09-15T00:00:00", currentDate,  \
                           "https://w3id.org/provcorp/corpus/factbank-annotations", "https://sites.google.com/site/rosersauri/>, <http://jamespusto.com/", fct)
    print("Done.")
    # count = 0
    # for i in sentences:
    #     print("%d : %s" % (count, i.text))
    #     count += 1

if __name__ == "__main__":
    main()
