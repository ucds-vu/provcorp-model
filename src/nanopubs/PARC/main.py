from imports import *
def usage():
    print("Options:\n \
    -a / --annotations= (file with the annotations on a certain text)\n \
    -t / --text= (file with the original text)\n \
    -r / --recalculate (recalculate the annotation indexes based on the original text)\n \
    -p / --path= (change the path to the nanopublication library)\n \
    -w / --word (only generate the word nanopublication)\n \
    -h / --help")

def main():
    libraryPath = "../" #"/Users/Timo-PC/Dropbox/provcorp"
    annotations = False
    text = False
    recalculate = False
    sentences = []
    wordOnly = False
    try:
        options, remainder = getopt.getopt(sys.argv[1:], "a:hp:rt:w", ['annotations=','help','path=','recalculate','secure','text=', 'word'])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    for opt, arg in options:
        if opt in ('-a', '--annotations'):
            annotations = True
            annotationFile = arg
        elif opt in ('-t', '--text'):
            text = True
            textFile = arg
        elif opt in ('-h', '--help'):
            usage()
            sys.exit(0)
        elif opt in ('-p', '--path'):
            libraryPath = arg
        elif opt in ('-r', '--recalculate'):
            recalculate = True
        elif opt in ('-w', '--word'):
            wordOnly = True
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

    # Preprocessing text
    if text:
        print("Preprocessing text...")
        preprocessedText = preprocessText(textFile)
        sentences = preprocessedText[1]
        document = preprocessedText[0]

    # Preprocess annotations
    if annotations and text:
        print("Preprocessing annotations...")
        wordObjects = preprocessAnnotations(annotationFile, sentences, recalculate)
    elif recalculate and not text:
        sys.stderr.write("ERROR: text is not given to recalculate the indexes\n")
        sys.exit(1)
    elif recalculate and not annotations:
        sys.stderr.write("ERROR: annotations are not given for the recalculation\n")
        sys.exit(1)

    if annotations:
        annotationFilename = os.path.basename(annotationFile)
        wordPublications = open(str("./results/texts/") + annotationFilename[:-4] + str("-parc_word.trig"), "w+")
        annotationGroups = dict()
        tags.wordTags()
        for anObj in range(len(wordObjects)):
            wordObjects[anObj].generateNanopub(wordPublications, "2016-05-01T00:00:00", currentDate, annotationFilename[:-4], \
            "https://orcid.org/0000-0003-0955-6104", \
            "https://w3id.org/provcorp/corpus/parc-texts", anObj)
            if not wordOnly:
                for atrObj in wordObjects[anObj].attributions:
                    if atrObj.id in annotationGroups and anObj not in annotationGroups[atrObj.id]:
                        annotationGroups[atrObj.id].append(wordObjects[anObj])
                    else:
                        annotationGroups[atrObj.id] = [wordObjects[anObj]]
        if not wordOnly:
            tags.annotationTags()
            annotationPublications = open(str("./results/annotations/") + annotationFilename[:-4] + str("-parc_annotation.trig"), "w+")
            max_group_length = 0
            for group in annotationGroups.keys():
                if len(annotationGroups.get(group)) > max_group_length:
                    max_group_length = len(annotationGroups.get(group))
                generateNanopub(annotationPublications, "2016-05-01T00:00:00", currentDate, annotationFilename[:-4], group, annotationGroups.get(group), \
                "https://orcid.org/0000-0003-0955-6104", "https://w3id.org/provcorp/corpus/parc-annotations")
    #print("Maximum group max_group_length = %d\n" % max_group_length)
    print("Done.")

if __name__ == "__main__":
    main()
