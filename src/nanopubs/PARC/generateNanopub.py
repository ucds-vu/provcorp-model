from imports import *
import templates.tags as tags

def generateNanopub(fileDescriptor, date, currentDate, file, set, words, URIcreator, URIcorpus):
    contentWords = []
    cueWords = []
    sourceWords = []
    # Grouping the words
    for word in words:
        for wordattr in word.attributions:
            if (wordattr.id == set and wordattr.role == "content"):
                contentWords.append(word)
            elif (wordattr.id == set and wordattr.role == "cue"):
                cueWords.append(word)
            elif (wordattr.id == set and wordattr.role == "source"):
                sourceWords.append(word)

    template = open("./templates/parc_template.trig", "r")
    templateContent = template.read()
    newContent = ""
    positions = []
    for i in range(len(tags.annotation_tags)):
        positions.append(templateContent.index(tags.annotation_tags[i]))

    newContent = templateContent[:positions[0]] + file + "/" + set
    newContent += templateContent[positions[0] + len(tags.annotation_tags[0]): positions[1]]
    newContent += file + ">.\n@prefix textoffset: <https://w3id.org/provcorp/np/protected/text/" + file + ".offset."
    newContent += templateContent[positions[1] + len(tags.annotation_tags[1]): positions[2]]


    if len(contentWords) > 0:
        newContent += templateContent[positions[2] + len(tags.annotation_tags[2]): positions[3]]
        for word_num in range(len(contentWords)):
            if word_num != len(contentWords) - 1:
                newContent += "textoffset:" + str(contentWords[word_num].beginIndex) + "-" +  str(contentWords[word_num].endIndex) + ", "
            else:
                newContent += "textoffset:" + str(contentWords[word_num].beginIndex) + "-" +  str(contentWords[word_num].endIndex)
        newContent += templateContent[positions[3] + len(tags.annotation_tags[3]): positions[4]]

    newContent += templateContent[positions[4] + len(tags.annotation_tags[4]): positions[5]]
    if len(cueWords) > 0:
        newContent += templateContent[positions[5] + len(tags.annotation_tags[5]): positions[6]]
        for word_num in range(len(cueWords)):
            if word_num != len(cueWords) - 1:
                newContent += "textoffset:" + str(cueWords[word_num].beginIndex) + "-" +  str(cueWords[word_num].endIndex) + ", "
            else:
                newContent += "textoffset:" + str(cueWords[word_num].beginIndex) + "-" +  str(cueWords[word_num].endIndex)
        newContent += templateContent[positions[6] + len(tags.annotation_tags[6]): positions[7]]

    newContent += templateContent[positions[7] + len(tags.annotation_tags[7]): positions[8]]
    if len(sourceWords) > 0:
        newContent += templateContent[positions[8] + len(tags.annotation_tags[8]): positions[9]]
        for word_num in range(len(sourceWords)):
            if word_num != len(sourceWords) - 1:
                newContent += "textoffset:" + str(sourceWords[word_num].beginIndex) + "-" +  str(sourceWords[word_num].endIndex) + ", "
            else:
                newContent += "textoffset:" + str(sourceWords[word_num].beginIndex) + "-" +  str(sourceWords[word_num].endIndex)
        newContent += templateContent[positions[9] + len(tags.annotation_tags[9]): positions[10]]

    newContent += templateContent[positions[10] + len(tags.annotation_tags[10]): positions[11]]
    newContent += set
    if "Nested" in set:
        newContent += "\"^^xsd:string;\n\tpvcpp:hasNestedRelationWith <https://w3id.org/provcorp/np/public/annotation-parc/" + file + "/" + contentWords[0].attributions[0].id + ".>."
    else:
        newContent += templateContent[positions[11] + len(tags.annotation_tags[11]): positions[12]]
    newContent += templateContent[positions[12] + len(tags.annotation_tags[12]): positions[13]]
    newContent += URIcorpus
    newContent += templateContent[positions[13] + len(tags.annotation_tags[13]): positions[14]]
    newContent += URIcreator
    newContent += templateContent[positions[14] + len(tags.annotation_tags[14]): positions[15]]
    newContent += date
    newContent += templateContent[positions[15] + len(tags.annotation_tags[15]): positions[16]]
    newContent += currentDate
    newContent += templateContent[positions[16] + len(tags.annotation_tags[16]):]
    fileDescriptor.write(newContent + "\n\n\n")
