from imports import *

def processWord(word, list):
    wordObject = Word(word)
    list.append(wordObject)

def moveDeeper(part, list):
    for p in part:
        if (p.tag == "WORD"):
            processWord(p, list)
        else:
            moveDeeper(p, list)

def recalculateIndex(word, sentence, wri, indoff, previousIndex):
    searchedIndex = previousIndex - sentence.beginIndex
    if searchedIndex < 2:
        searchedIndex = 0


    """ Need to look into more thing like the () which causes execeptions and making things more clear. Use global variables """
    if word.originalText == "-LRB-":
        indexInSentence = sentence.text.find("(", searchedIndex)
        lengthWord = 1
    elif word.originalText == "-RRB-":
        indexInSentence = sentence.text.find(")", searchedIndex)
        lengthWord = 1
    elif word.originalText == "&":
        indexInSentence = sentence.text.find("amp", searchedIndex)
        lengthWord = 3
    elif word.originalText == "S.p.EA.":
        indexInSentence = sentence.text.find("S.p.A.", searchedIndex)
        lengthWord = 6
    else:
        indexInSentence = sentence.text.find(word.originalText, searchedIndex)
        lengthWord = len(word.originalText.encode('UTF-8'))
    if indexInSentence < 0:
        sys.stderr.write("Error recalculating offsets. Word not in given sentence. \n Word: %s\n Sentence: %s \n" % (word.originalText, sentence.text))
        sys.exit(1)
    newIndex = indexInSentence + sentence.beginIndex
    difference = abs((newIndex + 6) - word.beginIndex) # +6 due to the fact that we don't count the <TEXT>

    if difference > 0:
        #print(difference)
        #print(word.originalText)
        wri += 1
        indoff += difference

    word.beginIndex = newIndex
    word.endIndex = word.beginIndex + lengthWord
    return (wri, indoff, word.endIndex)

def preprocessAnnotations(annotation_file, sentences, recalculate):
    wrongIndex = 0
    indexOff = 0
    prevIndex = 0
    wordObjects = []

    tree = ET.parse(annotation_file)
    root = tree.getroot()
    moveDeeper(root, wordObjects)

    if recalculate:
        print("Recalculating indexes")
        for wordObj in range(len(wordObjects)):
            try:
                if (wordObj > 0):
                    resultTuple  = recalculateIndex(wordObjects[wordObj], sentences[wordObjects[wordObj].sentenceNum], wrongIndex, indexOff, prevIndex)
                else:
                    resultTuple  = recalculateIndex(wordObjects[wordObj], sentences[wordObjects[wordObj].sentenceNum], wrongIndex, indexOff, 0)
            except:
                print("Could not find index probably due to ; issue. Going to the next sentence")
                if (wordObj > 0):
                    resultTuple  = recalculateIndex(wordObjects[wordObj], sentences[wordObjects[wordObj].sentenceNum + 1], wrongIndex, indexOff, prevIndex)
                else:
                    resultTuple  = recalculateIndex(wordObjects[wordObj], sentences[wordObjects[wordObj].sentenceNum + 1], wrongIndex, indexOff, 0)
            wrongIndex = resultTuple[0]
            indexOff = resultTuple[1]
            prevIndex = resultTuple[2]
        if wrongIndex > 0:
            averageOff = indexOff / wrongIndex
        else:
            averageOff = 0
        print("In total %0.2f%% of the words had a wrong index. \nOn average the index was %d off" % (wrongIndex / (len(wordObjects) / 100), averageOff))

    return wordObjects
