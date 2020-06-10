from imports import *
def usage():
    print("Options:\n \
    -a / --annotations= (the annotation index nanopub)\n \
    -t / --text= (the text index nanopub)\n")

def main():
    libraryPath = "../../" 
    tag_index = "@index"
    tag_date = "@date"
    try:
        options, remainder = getopt.getopt(sys.argv[1:], "a:t:", ['annotations=','text='])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    for opt, arg in options:
        if opt in ('-a', '--annotations'):
            indexAnnotations = arg
        elif opt in ('-t', '--text'):
            indexTexts = arg
        else:
            sys.stderr.write("ERROR: Unhandled option entered\n")
            sys.exit(2)

    #Get basic information
    try:
        currentDate = subprocess.check_output(['./np', 'now'], cwd=libraryPath)
        currentDate = currentDate.decode('utf-8')[:-1]
    except:
        sys.stderr.write("ERROR: Path to nanopublication library is not found or working\nuse -p to change the path\n")
        sys.exit(1)

    annotation = open("./results/factbank_annotation_corpus.trig", "w+")
    annotation_template = open("./templates/factbank-annotation-corpus.trig", "r")
    annotationTemplateContent = annotation_template.read()
    in_index = annotationTemplateContent.index(tag_index)
    in_date = annotationTemplateContent.index(tag_date)
    newAnnotation = annotationTemplateContent[:in_index]
    newAnnotation += indexAnnotations[11:]
    newAnnotation += annotationTemplateContent[in_index + len(tag_index): in_date]
    newAnnotation += currentDate
    newAnnotation += annotationTemplateContent[in_date + len(tag_date):]
    annotation.write(newAnnotation)

    text = open("./results/factbank_text_corpus.trig", "w+")
    text_template = open("./templates/factbank-text-corpus.trig", "r")
    textTemplateContent = text_template.read()
    in_index = textTemplateContent.index(tag_index)
    in_date = textTemplateContent.index(tag_date)
    newText = textTemplateContent[:in_index]
    newText += indexTexts[11:]
    newText += textTemplateContent[in_index + len(tag_index): in_date]
    newText += currentDate
    newText += textTemplateContent[in_date + len(tag_date):]
    text.write(newText)

if __name__ == "__main__":
    main()
