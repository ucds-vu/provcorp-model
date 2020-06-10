from imports import *
import templates.tags as tags


def generateTextNanopub(fileDescriptor, file, text, date, currentTime, uriCorp, uriCreator):
    textformatted = text.replace("'", "\\'")
    textformatted = textformatted.replace("\"", "\\\"")
    template = open("./templates/text_template.trig", "r")
    templateContent = template.read()
    newContent = ""
    positions = []
    for i in range(len(tags.text_tags)):
        positions.append(templateContent.index(tags.text_tags[i]))

    newContent = templateContent[:positions[0]] + file
    newContent += templateContent[positions[0] + len(tags.text_tags[0]): positions[1]]
    newContent += textformatted
    newContent += templateContent[positions[1] + len(tags.text_tags[1]): positions[2]]
    newContent += uriCorp
    newContent += templateContent[positions[2] + len(tags.text_tags[2]): positions[3]]
    newContent += uriCreator
    newContent += templateContent[positions[3] + len(tags.text_tags[3]): positions[4]]
    newContent += date
    newContent += templateContent[positions[4] + len(tags.text_tags[4]): positions[5]]
    newContent += currentTime
    newContent += templateContent[positions[5] + len(tags.text_tags[5]):]
    fileDescriptor.write(newContent + "\n\n\n")
