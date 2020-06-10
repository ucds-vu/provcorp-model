from imports import *
import templates.tags as tags

class Sentence:
    def __init__ (self, beginIndex, sentence, number):
        self.text = str(sentence).replace("\"", "\\\"")
        self.text = self.text.replace("'", "\\\'")
        if self.text[len(self.text.encode('UTF-8')) - 1] == ' ':
            self.text = self.text[:len(self.text.encode('UTF-8')) - 1]
        if number > 0:
            if "   " in self.text:
                self.text = self.text[1:]
        self.beginIndex = int(beginIndex)
        self.endIndex = self.beginIndex + len(self.text.encode('UTF-8'))
        self.number = number
