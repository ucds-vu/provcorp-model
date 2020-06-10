from imports import *
from classes.attribute import Attribute
import templates.tags as tags


class Word:
    def __init__(self, word):
        self.originalText = word.attrib.get("text").replace("\"", "\\\"")
        self.originalText = self.originalText.replace("\\/", "/")
        self.originalText = self.originalText.replace("``", "\"")
        self.originalText = self.originalText.replace("''", "\"")
        self.originalText = self.originalText.replace("'", "\\\'")

        self.lemma = word.attrib.get("lemma").replace("\"", "\\\"")
        self.lemma = self.lemma.replace("\\/", "/")
        self.lemma = self.lemma.replace("``", "\"")
        self.lemma = self.lemma.replace("''", "\"")
        self.lemma = self.lemma.replace("'", "\'")
        self.pos = word.attrib.get("pos")
        self.sentenceWord = int(word.attrib.get("sentenceWord"))
        self.word = int(word.attrib.get("word"))
        self.gorn = word.attrib.get("gorn")
        self.ByteCount = word.attrib.get("ByteCount").split(',')
        self.beginIndex = int(self.ByteCount[0])
        self.endIndex = int(self.ByteCount[1])
        self.attributions = []
        self.sentenceNum = int(self.gorn.split(',')[0])
        for attr in word:
            self.attributions.append(Attribute(attr))

    def generateNanopub(self, fileDescriptor, date, currentDate, file, URIcreator, URIcorpus, index):
        template = open("./templates/parc-word_template.trig", "r")
        templateContent = template.read()
        newContent = ""
        positions = []
        for i in range(len(tags.word_tags)):
            positions.append(templateContent.index(tags.word_tags[i]))

        newContent = templateContent[:positions[0]] + file + "/" + str(index) + "."
        newContent += templateContent[positions[0] + len(tags.word_tags[0]): positions[1]]
        newContent += file + ">.\n@prefix textoffset: <https://w3id.org/provcorp/np/protected/text/" + file + ".offset."
        newContent += templateContent[positions[1] + len(tags.word_tags[1]): positions[2]]
        newContent += str(self.beginIndex) + "-" + str(self.endIndex)
        newContent += templateContent[positions[2] + len(tags.word_tags[2]): positions[3]]
        newContent += self.originalText
        newContent += templateContent[positions[3] + len(tags.word_tags[3]): positions[4]]
        newContent += self.lemma
        newContent += templateContent[positions[4] + len(tags.word_tags[4]): positions[5]]
        newContent += str(self.beginIndex)
        newContent += templateContent[positions[5] + len(tags.word_tags[5]): positions[6]]
        newContent += str(self.endIndex)
        newContent += templateContent[positions[6] + len(tags.word_tags[6]): positions[7]]
        newContent += str(self.sentenceWord)
        newContent += templateContent[positions[7] + len(tags.word_tags[7]): positions[8]]
        newContent += str(self.word)
        newContent += templateContent[positions[8] + len(tags.word_tags[8]): positions[9]]
        newContent += str(self.sentenceNum)
        newContent += templateContent[positions[9] + len(tags.word_tags[9]): positions[10]]
        newContent += self.gorn
        newContent += templateContent[positions[10] + len(tags.word_tags[10]): positions[11]]
        newContent += self.pos
        newContent += templateContent[positions[11] + len(tags.word_tags[11]): positions[12]]
        newContent += URIcreator
        newContent += templateContent[positions[12] + len(tags.word_tags[12]): positions[13]]
        newContent += date
        newContent += templateContent[positions[13] + len(tags.word_tags[13]): positions[14]]
        newContent += currentDate
        newContent += templateContent[positions[14] + len(tags.word_tags[14]):]
        fileDescriptor.write(newContent + "\n\n\n")
