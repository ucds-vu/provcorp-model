from imports import *
corporaPath = "../corpora/factbank_v1/data/annotation/"
def getTargetLines(document, file):
    targetLines = []
    file = open(corporaPath + file, "r")
    fileData = file.read()
    lines = fileData.splitlines()
    for l in lines:
        if document in l:
            targetLines.append(l)


    return targetLines
