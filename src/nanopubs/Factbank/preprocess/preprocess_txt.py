from imports import *
from classes.sentence import Sentence
from classes.document import Document

def preprocessText(text_file):
    number = 0
    currentIndex = 0 # Could be 6 to keep the current numbers of the original annotations
    sentences = []
    subject = ""
    additionalInformation = ""

    file = open(text_file, 'r')
    text = file.read()
    separateLines = text.splitlines()
    beginIndex = separateLines.index("<TEXT>") + 1
    endIndex = separateLines.index("</TEXT>")

    # For wsj files
    if "wsj" in text_file:
        for s in range(len(separateLines)):
            if "DOCNO" in separateLines[s]:
                documentNo = separateLines[s][8:-9]
            if "<HL>" in separateLines[s]:
                beginSubject = s
            if "</HL>" in separateLines[s]:
                endSubject = s

        # Getting document data
        date = separateLines[endSubject + 1]
        journal = separateLines[endSubject + 2]
        for part in range (0, beginIndex - 1):
            if beginSubject <= part <= endSubject - 1:
                subject += separateLines[part] + str(" ")
            elif part == endSubject:
                subject += separateLines[part]

            if part > endSubject + 2:
                if "<DATELINE>" in separateLines[part]:
                    additionalInformation += separateLines[part][10:-11]
                else:
                    additionalInformation += separateLines[part]


        subject = subject[5:-6]

        dateParts = date.split("/")
        if (int(dateParts[2])) > 20:
            newDate = "19" + dateParts[2][:2]
        else:
            newDate = "20" + dateParts[2][:2]
        newDate = newDate + "-" + dateParts[0][1:] + "-" + dateParts[1] + "T00:00:00"

    # FOR ABC files
    if "ABC" in text_file:
        beginIndex = beginIndex + 1 # Extra enter between <TEXT> and the text
        subject = "NEWS STORY"
        journal = "broadcast news"
        for s in range(len(separateLines)):
            if "DOCNO" in separateLines[s]:
                documentNo = separateLines[s][8:-9]
                break
        newDate = documentNo[3:7] + "-" + documentNo[7:9] + "-" + documentNo[9:11] + "T00:00:00"

    if "ea" in text_file or "ed" in text_file:
        beginIndex = beginIndex + 1 # Extra enter between <TEXT> and the text
        subject = "NEWS STORY"
        journal = "broadcast"
        for s in range(len(separateLines)):
            if "DOCNO" in separateLines[s]:
                documentNo = separateLines[s][8:-9]
                break
        newDate = "19" + documentNo[2:4] + "-" + documentNo[4:6] + "-" + documentNo[6:8] + "T00:00:00"

    if "PRI" in text_file:
        beginIndex = beginIndex + 1 # Extra enter between <TEXT> and the text
        subject = "NEWS STORY"
        journal = "broadcast"
        for s in range(len(separateLines)):
            if "DOCNO" in separateLines[s]:
                documentNo = separateLines[s][8:-9]
                break
        newDate = documentNo[3:7] + "-" + documentNo[7:9] + "-" + documentNo[9:11] + "T00:00:00"


    if "CNN" in text_file:
        beginIndex = beginIndex + 1 # Extra enter between <TEXT> and the text
        subject = "NEWS STORY"
        journal = "CNN"
        for s in range(len(separateLines)):
            if "DOCNO" in separateLines[s]:
                documentNo = separateLines[s][8:-9]
                break
        newDate = documentNo[3:7] + "-" + documentNo[7:9] + "-" + documentNo[9:11] + "T00:00:00"

    if "VOA" in text_file:
        beginIndex = beginIndex + 1 # Extra enter between <TEXT> and the text
        subject = "NEWS STORY"
        journal = "VOA"
        for s in range(len(separateLines)):
            if "DOCNO" in separateLines[s]:
                documentNo = separateLines[s][8:-9]
                break
        newDate = documentNo[3:7] + "-" + documentNo[7:9] + "-" + documentNo[9:11] + "T00:00:00"

    if "XIE" in text_file:
        subject = "NEWS STORY"
        journal = "broadcast"
        for s in range(len(separateLines)):
            if "DOCNO" in separateLines[s]:
                documentNo = separateLines[s][9:-9]
            if "DATE_TIME" in separateLines[s]:
                datefile = separateLines[s][12:-13]
            if "<HEADLINE>" in separateLines[s]:
                start_subject = s + 1
            if "</HEADLINE>" in separateLines[s]:
                end_subject = s

        for line in range(start_subject, end_subject):
            subject += separateLines[line] + " "
        newDate = datefile[1:] + "T00:00:00"

    # FOR AP files
    if "AP9" in text_file:
        subject = ""
        journal = "Associated Press Writer"
        for s in range(len(separateLines)):
            if "DOCNO" in separateLines[s]:
                documentNo = separateLines[s][8:-9]
            if "<SECOND>" in separateLines[s]:
                start_subject = s + 1
            if "LaserPhotos" in separateLines[s]:
                end_subject = s

        for line in range(start_subject, end_subject):
            subject += separateLines[line]

        newDate = "19" + documentNo[2:4] + "-" + documentNo[4:6] + "-" + documentNo[6:8] + "T00:00:00"

    if "APW" in text_file or "NYT" in text_file:
        subject = ""
        journal = "Associated Press Writer"
        if "NYT" in text_file:
            journal = "NYT"
        for s in range(len(separateLines)):
            if "DOCNO" in separateLines[s]:
                documentNo = separateLines[s][8:-9]
            if "DATE_TIME" in separateLines[s]:
                datefile = separateLines[s][12:-13]
            if "<HEADLINE>" in separateLines[s]:
                start_subject = s + 1
            if "</HEADLINE>" in separateLines[s]:
                end_subject = s

        for line in range(start_subject, end_subject):
            subject += separateLines[line] + " "

        for add in range(end_subject + 1, beginIndex -1):
            additionalInformation += separateLines[add] + " "

        newDate = datefile[6:10] + "-" + datefile[:2] + "-" + datefile[3:5] + "T" + datefile[11:19]

    # Generate sentence objects
    for sentence in range(beginIndex, endIndex):
        if (len(separateLines[sentence]) == 0):
             currentIndex +=1 # empty line as extra index
             continue
        if "---" in separateLines[sentence]:
            currentIndex +=4
            continue

        sentences.append(Sentence(currentIndex, separateLines[sentence], number))
        currentIndex = sentences[-1].endIndex + 1
        number += 1

    document = Document(subject, journal, documentNo, additionalInformation, newDate)
    return (document, sentences)

def getSentenceDifference(sentences, file):
    target_sentences = getTargetLines(file, "sentences.txt")
    compare_sentence = sentences[0].text.replace("\\", "")
    #print(compare_sentence)
    for i in range(len(target_sentences)):
        parts_sentence = target_sentences[i].split("|||")
        text_part = parts_sentence[2][1:-1].replace("\\", "")
        #print(text_part)
        if text_part in compare_sentence:
            return i
    print("COULD NOT FIND THE SAME START SENTENCE")
    sys.exit(1)
