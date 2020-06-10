from imports import *
class Source:
    def __init__(self, sourceid, text, loc, sentenceNum):
        self.sourceId = sourceid
        self.sourceText = text
        self.sourceLoc = loc
        self.sentenceNum = sentenceNum
        self.beginIndex = 0
        self.endIndex = 0

    def calculateIndex(self, sentences, sentenceID, longerSentences, headline):
        # print(self.sourceText)
        # print(self.sentenceNum)
        if sentenceID < 0 :
            self.sentenceID = -1
            self.beginIndex = headline.index(self.sourceText)
            self.endIndex = self.beginIndex + len(self.sourceText)
            return
        if sentenceID >= len(sentences) - 1:
            sentenceID = len(sentences) -1
        while (sentenceID >= 0):
            sen = sentences[sentenceID]
            #nltk.download('punkt')
            # Is this the right sentence?
            if self.sourceText not in sen.text:
                sentenceID = sentenceID - 1
                print("Note: Looking at previous sentence of %d for source word: %s." % (sentenceID, self.sourceText))
                continue

            tokenized_sentence = nltk.word_tokenize(sen.text)
            start_index = 0
            token_start = int(self.sourceLoc)
            # Tokenizer could be different
            if int(self.sourceLoc) - 2 > len(tokenized_sentence):
                token_start = len(tokenized_sentence) - 2

            if longerSentences == 1:
                token_start = token_start - 5

            try:
                for i in range(token_start):
                    start_index += len(tokenized_sentence[i][1:-1])
                self.beginIndex = sen.text.index(self.sourceText, start_index) + sen.beginIndex
            except:
                print("Note: Getting start index without start index:source\n")
                self.beginIndex = sen.text.index(self.sourceText) + sen.beginIndex
            self.endIndex = self.beginIndex + len(self.sourceText)
            self.sentenceID = sen.number
            return
        print("ERROR COULD NOT FIND THE RIGHT SENTENCE AND INDEX: FACTVALUE\n")
        sys.exit(1)





class FactValue:
    def __init__(self, sentence, sourceinfo, sentenceDifference):
        parts = sentence.split('|||')
        self.sentenceNum = parts[1]
        self.eID =  parts[3].replace("'", "")
        self.factValue = parts[8].replace("'", "")
        self.relSourceId = parts[5].replace("'", "")
        self.relSourceText = parts[7][1:-1].replace("'", "\'")
        self.source = []
        part_id = re.split("=|_", self.relSourceId)
        part_text = re.split("=|_", self.relSourceText)
        for i in range(len(part_id)):
            source_loc = ""
            source_sentenceNum = -1
            if part_text[i] == "AUTHOR" or part_text[i] == "GEN" or part_text[i] == "DUMMY":
                source_loc = "-1"
            else:
                for src in sourceinfo:
                    data_source = src.split('|||')
                    if data_source[1] == self.sentenceNum and data_source[2].replace("'", "") == part_id[i]:
                        source_loc = data_source[3]
                        source_sentenceNum = int(data_source[1]) - sentenceDifference
            self.source.append(Source(part_id[i], part_text[i], source_loc, source_sentenceNum))

    def generateNanopub(self, fileDescriptor, file, date, currentTime, uriCorp, uriCreator, index):
        template = open("./templates/fb_factvalue.trig", "r")
        templateContent = template.read()
        newContent = ""
        positions = []
        for i in range(len(tags.factvalue_tags)):
            positions.append(templateContent.index(tags.factvalue_tags[i]))

        newContent = templateContent[:positions[0]] + file + "/" + str(index)
        newContent += templateContent[positions[0] + len(tags.factvalue_tags[0]): positions[1]]

        newContent += file + ">.\n@prefix textoffset: <https://w3id.org/provcorp/np/protected/text/" + file + ".offset.>.\n@prefix headlineoffset: <https://w3id.org/provcorp/np/public/document/" + file + ".headlineoffset."
        newContent += templateContent[positions[1] + len(tags.factvalue_tags[1]): positions[2]]

        for src_content in range(len(self.source)):
            newContent += templateContent[positions[2] + len(tags.factvalue_tags[2]): positions[3]]
            newContent += str(src_content+1)
            if self.source[src_content].sourceText == "AUTHOR":
                newContent += " a pvcpf:AuthorAsSourceAnnotation;\n\tpvcp:sourceID \"s0\"^^xsd:string;\n\tpvcpf:hasSourceText \"AUTHOR\"^^xsd:string.\n"
            elif self.source[src_content].sourceText == "GEN":
                newContent += " a pvcpf:GenAsSourceAnnotation;\n\tpvcp:sourceID \"" + self.source[src_content].sourceId + "\"^^xsd:string;\n\tpvcpf:hasSourceText \"GEN\"^^xsd:string.\n"
            elif self.source[src_content].sourceText == "DUMMY":
                newContent += " a pvcpf:DummyasSourceAnnotation;\n\tpvcp:sourceID \"" + self.source[src_content].sourceId + "\"^^xsd:string;\n\tpvcpf:hasSourceText \"DUMMY\"^^xsd:string.\n"
            else:
                newContent += templateContent[positions[3] + len(tags.factvalue_tags[3]): positions[4]]
                newContent += self.source[src_content].sourceId
                newContent += templateContent[positions[4] + len(tags.factvalue_tags[4]): positions[5]]
                newContent += str(self.source[src_content].sentenceNum)
                newContent += templateContent[positions[5] + len(tags.factvalue_tags[5]): positions[6]]
                newContent += self.source[src_content].sourceText
                newContent += templateContent[positions[6] + len(tags.factvalue_tags[6]): positions[7]]
                newContent += str(self.source[src_content].beginIndex)
                newContent += templateContent[positions[7] + len(tags.factvalue_tags[7]): positions[8]]
                newContent += str(self.source[src_content].endIndex)
                if self.source[src_content].sentenceNum != -1:
                    newContent += templateContent[positions[8] + len(tags.factvalue_tags[8]): positions[9]]
                    newContent += str(self.source[src_content].beginIndex) + "-" + str(self.source[src_content].endIndex)
                else:
                    newContent += templateContent[positions[8] + len(tags.factvalue_tags[8]): positions[9] -11]
                    newContent += "headlineoffset:" + str(self.source[src_content].beginIndex) + "-" + str(self.source[src_content].endIndex)
                newContent += templateContent[positions[9] + len(tags.factvalue_tags[9]): positions[10]]

        newContent += templateContent[positions[10] + len(tags.factvalue_tags[10]): positions[11]]
        newContent += self.factValue
        newContent += templateContent[positions[11] + len(tags.factvalue_tags[11]): positions[12]]
        newContent += self.relSourceId
        newContent += templateContent[positions[12] + len(tags.factvalue_tags[12]): positions[13]]
        newContent += self.relSourceText
        newContent += templateContent[positions[13] + len(tags.factvalue_tags[13]): positions[14]]
        newContent += "https://w3id.org/provcorp/np/protected/annotation-fb/event/" + file + "/" + self.eID
        newContent += templateContent[positions[14] + len(tags.factvalue_tags[14]): positions[15]]

        for src_content  in range(len(self.source)):
            newContent += templateContent[positions[15] + len(tags.factvalue_tags[15]): positions[16]]
            newContent += str(src_content+1)
            newContent += templateContent[positions[16] + len(tags.factvalue_tags[16]): positions[17]]

        newContent += templateContent[positions[17] + len(tags.factvalue_tags[17]): positions[18]]
        newContent += uriCorp
        newContent += templateContent[positions[18] + len(tags.factvalue_tags[18]): positions[19]]
        newContent += uriCreator
        newContent += templateContent[positions[19] + len(tags.factvalue_tags[19]): positions[20]]
        newContent += date
        newContent += templateContent[positions[20] + len(tags.factvalue_tags[20]): positions[21]]
        newContent += currentTime
        newContent += templateContent[positions[21] + len(tags.factvalue_tags[21]):]

        fileDescriptor.write(newContent + "\n\n\n")
