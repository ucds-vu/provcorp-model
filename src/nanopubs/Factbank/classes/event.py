from imports import *
import templates.tags as tags

class Event:
    def __init__(self, sentence, tokens):
        parts = sentence.split('|||')
        self.eID =  parts[2].replace("'", "")
        self.eiID = parts[3].replace("'", "")
        self.text = parts[4][1:-1].replace("\"", "\\\"")
        self.sentenceID = int(parts[1])
        self.beginIndex = 0
        self.endIndex = 0
        self.tokenNum = -1
        for token_info in tokens:
            token_parts = token_info.split("|||")
            if (int(token_parts[1]) == self.sentenceID and token_parts[5][1:-1] == self.eID):
                self.tokenNum = int(token_parts[2])


    def calculateIndex(self, sentences, sentenceID, longerSentences, headline):
        # Some optimalizations to fix the ; exception error
        # print(self.text)
        # print(sentenceID)
        #
        if sentenceID < 0 :
            self.sentenceID = -1
            self.beginIndex = headline.index(self.text)
            self.endIndex = self.beginIndex + len(self.text)
            return
        if sentenceID >= len(sentences) - 1:
            sentenceID = len(sentences) -1
        while (sentenceID >= 0):
            sen = sentences[sentenceID]
            #nltk.download('punkt')
            # Is this the right sentence?
            if self.text not in sen.text:
                sentenceID = sentenceID - 1
                print("Note: Looking at previous sentence of %d for event word: %s.  %s" % (sentenceID, self.text, self.eID))
                continue

            #print(sen.text, end='\n\n')
            tokenized_sentence = nltk.word_tokenize(sen.text)
            start_index = 0
            token_start = self.tokenNum
            # Tokenizer could be different
            if self.tokenNum - 2 > len(tokenized_sentence):
                token_start = len(tokenized_sentence) - 2

            if longerSentences == 1:
                token_start = token_start - 5

            try:
                for i in range(token_start):
                    start_index += len(tokenized_sentence[i][1:-1])
                self.beginIndex = sen.text.index(self.text, start_index) + sen.beginIndex
            except:
                print("Note: Getting start index without start index: event. %s:%s\n" % (self.text, self.eID))
                print(sen.text)
                self.beginIndex = sen.text.index(self.text) + sen.beginIndex
            self.endIndex = self.beginIndex + len(self.text)
            self.sentenceID = sen.number
            return
        print("ERROR COULD NOT FIND THE RIGHT SENTENCE AND INDEX: EVENT\n")
        sys.exit(1)

    def generateNanopub(self, fileDescriptor, fileDescriptor_words, file, date, currentTime, uriCorp, uriCreator, index, journal):
        # Word of the event
        templateWord = open("./templates/fb_word.trig", "r")
        templateWordContent = templateWord.read()
        newWordContent = ""
        positionsWord = []
        for i in range(len(tags.word_tags)):
            positionsWord.append(templateWordContent.index(tags.word_tags[i]))
        if self.sentenceID != -1:
            newWordContent = templateWordContent[:positionsWord[0]] + file + "/" + str(index) + ".>.\n@prefix textoffset: <https://w3id.org/provcorp/np/protected/text/" + file + ".offset."
        else:
            newWordContent = templateWordContent[:positionsWord[0]] + file + "/" + str(index) + ".>.\n@prefix headlineoffset: <https://w3id.org/provcorp/np/public/document/" + file + ".headlineoffset.>.\n@prefix document: <https://w3id.org/provcorp/np/public/document/" + file
        newWordContent += templateWordContent[positionsWord[0] + len(tags.word_tags[0]): positionsWord[1]]
        newWordContent += file
        if self.sentenceID != -1:
            newWordContent += templateWordContent[positionsWord[1] + len(tags.word_tags[1]): positionsWord[2]]
            newWordContent += str(self.beginIndex) + "-" + str(self.endIndex)
        else:
            newWordContent += templateWordContent[positionsWord[1] + len(tags.word_tags[1]): positionsWord[2] -11]
            newWordContent += "headlineoffset:" + str(self.beginIndex) + "-" + str(self.endIndex)
        newWordContent += templateWordContent[positionsWord[2] + len(tags.word_tags[2]): positionsWord[3]]
        newWordContent += str(self.beginIndex)
        newWordContent += templateWordContent[positionsWord[3] + len(tags.word_tags[3]): positionsWord[4]]
        newWordContent += str(self.endIndex)
        newWordContent += templateWordContent[positionsWord[4] + len(tags.word_tags[4]): positionsWord[5]]
        newWordContent += self.text
        newWordContent += templateWordContent[positionsWord[5] + len(tags.word_tags[5]): positionsWord[6]]
        newWordContent += str(self.sentenceID)
        if self.sentenceID != -1:
            newWordContent += templateWordContent[positionsWord[6] + len(tags.word_tags[6]): positionsWord[7]]
        else:
            newWordContent += templateWordContent[positionsWord[6] + len(tags.word_tags[6]): positionsWord[6] + len(tags.word_tags[6]) + 14]
            newWordContent += "pvcp:isPartOfHeadline document:document."
            newWordContent += templateWordContent[positionsWord[6] + len(tags.word_tags[6]) + 42: positionsWord[7]]
        newWordContent += journal
        newWordContent += templateWordContent[positionsWord[7] + len(tags.word_tags[7]): positionsWord[8]]
        newWordContent += date
        newWordContent += templateWordContent[positionsWord[8] + len(tags.word_tags[8]): positionsWord[9]]
        newWordContent += currentTime
        newWordContent += templateWordContent[positionsWord[9] + len(tags.word_tags[9]):]
        fileDescriptor_words.write(newWordContent + "\n\n\n")


        #event itself
        templateEvent = open("./templates/fb_event.trig", "r")
        templateEventContent = templateEvent.read()
        newEventContent = ""
        positionsEvent = []
        for i in range(len(tags.event_tags)):
            positionsEvent.append(templateEventContent.index(tags.event_tags[i]))

        if self.sentenceID != -1:
            newEventContent = templateEventContent[:positionsEvent[0]] + file + "/" + self.eID + ".>.\n@prefix textoffset: <https://w3id.org/provcorp/np/protected/text/" + file + ".offset."
        else:
            newEventContent = templateEventContent[:positionsEvent[0]] + file + "/" + self.eID + ".>.\n@prefix headlineoffset: <https://w3id.org/provcorp/np/public/document/" + file + ".headlineoffset."
        newEventContent += templateEventContent[positionsEvent[0] + len(tags.event_tags[0]): positionsEvent[1]]
        newEventContent += file
        if self.sentenceID != -1:
            newEventContent += templateEventContent[positionsEvent[1] + len(tags.event_tags[1]): positionsEvent[2]]
            newEventContent += str(self.beginIndex) + "-" + str(self.endIndex)
        else:
            newEventContent += templateEventContent[positionsEvent[1] + len(tags.event_tags[1]): positionsEvent[2]-11]
            newEventContent += "headlineoffset:" + str(self.beginIndex) + "-" + str(self.endIndex)
        newEventContent += templateEventContent[positionsEvent[2] + len(tags.event_tags[2]): positionsEvent[3]]
        newEventContent += self.eID
        newEventContent += templateEventContent[positionsEvent[3] + len(tags.event_tags[3]): positionsEvent[4]]
        newEventContent += self.eiID
        newEventContent += templateEventContent[positionsEvent[4] + len(tags.event_tags[4]): positionsEvent[5]]
        newEventContent += uriCorp
        newEventContent += templateEventContent[positionsEvent[5] + len(tags.event_tags[5]): positionsEvent[6]]
        newEventContent += uriCreator
        newEventContent += templateEventContent[positionsEvent[6] + len(tags.event_tags[6]): positionsEvent[7]]
        newEventContent += date
        newEventContent += templateEventContent[positionsEvent[7] + len(tags.event_tags[7]): positionsEvent[8]]
        newEventContent += currentTime
        newEventContent += templateEventContent[positionsEvent[8] + len(tags.event_tags[8]):]

        fileDescriptor.write(newEventContent + "\n\n\n")
