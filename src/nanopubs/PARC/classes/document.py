from imports import *
import templates.tags as tags

class Document:
    def __init__ (self, subject, journal, docno, info, date):
        self.subject = subject
        self.journal = journal
        self.docno = docno
        # include exception for when additional_information is empty
        self.additional_information = info
        try:
            if self.additional_information[0] == " ":
                self.additional_information = self.additional_information[1:]
            if self.additional_information[-1] == " ":
                self.additional_information = self.additional_information[:-1]
        except:
            print("Additional information is empty")
        self.date = date
        if "WALL STREET JOURNAL (J)" in self.journal:
            self.journal = "http://dbpedia.org/resource/The_Wall_Street_Journal"
        elif "broadcast news" in self.journal:
            self.journal = "http://dbpedia.org/resource/ABC_News"
        elif "Associated Press Writer" in self.journal:
            self.journal = "http://dbpedia.org/resource/Associated_Press"
        elif "CNN" in self.journal:
            self.journal = "http://dbpedia.org/resource/CNN"
        elif "broadcast" in self.journal:
            self.journal = "http://dbpedia.org/resource/News_broadcasting"
        elif "NYT" in self.journal:
            self.journal = "http://dbpedia.org/resource/NYT"
        elif "VOA" in self.journal:
                self.journal = "http://dbpedia.org/resource/Voice_of_America"
    def generateNanopub(self, file, fileDescriptor, currentTime, uriCorp):
        template = open("./templates/document_template.trig", "r")
        templateContent = template.read()
        newContent = ""
        positions = []
        for i in range(len(tags.document_tags)):
            positions.append(templateContent.index(tags.document_tags[i]))
        newContent = templateContent[:positions[0]] + file[:-4]
        newContent += templateContent[positions[0] + len(tags.document_tags[0]): positions[1]]
        newContent += self.subject
        newContent += templateContent[positions[1] + len(tags.document_tags[1]): positions[2]]
        newContent += self.docno
        newContent += templateContent[positions[2] + len(tags.document_tags[2]): positions[3]]
        newContent += self.journal
        newContent += templateContent[positions[3] + len(tags.document_tags[3]): positions[4]]
        newContent += self.date
        if len(self.additional_information) == 0:
            newContent += templateContent[positions[4] + len(tags.document_tags[4]): positions[5] - 16]
            newContent += templateContent[positions[5] + len(tags.document_tags[5]) + 15: positions[6]]
        else:
            newContent += templateContent[positions[4] + len(tags.document_tags[4]): positions[5]]
            newContent += self.additional_information
            newContent += templateContent[positions[5] + len(tags.document_tags[5]): positions[6]]
        newContent += file[:-4]
        newContent += templateContent[positions[6] + len(tags.document_tags[6]): positions[7]]
        newContent += uriCorp
        newContent += templateContent[positions[7] + len(tags.document_tags[7]): positions[8]]
        newContent += currentTime
        newContent += templateContent[positions[8] + len(tags.document_tags[8]):]
        fileDescriptor.write(newContent + "\n\n\n")
