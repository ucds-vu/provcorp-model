def eventTags():
    global event_tags
    event_tags = []
    event_tags.append("@numberevent")
    event_tags.append("@text")
    event_tags.append("@UriToText2")
    event_tags.append("@eID")
    event_tags.append("@eiID")
    event_tags.append("@corpus")
    event_tags.append("@URIcreator")
    event_tags.append("@date")
    event_tags.append("@datepub")


def wordTags():
    global word_tags
    word_tags = []
    word_tags.append("@numberevent")
    word_tags.append("@text")
    word_tags.append("@UriToText1")
    word_tags.append("@Bind")
    word_tags.append("@Eind")
    word_tags.append("@EventText")
    word_tags.append("@SenNum")
    word_tags.append("@journal")
    word_tags.append("@date")
    word_tags.append("@datepub")

def factvalueTags():
    global factvalue_tags
    factvalue_tags = []
    factvalue_tags.append("@numberfactvalue")
    factvalue_tags.append("@textDocument")
    factvalue_tags.append("@beginsource")
    factvalue_tags.append("@sourcenumber")
    factvalue_tags.append("@sourceID")
    factvalue_tags.append("@sentenceNUM")
    factvalue_tags.append("@sourceText")
    factvalue_tags.append("@beginIndex")
    factvalue_tags.append("@endIndex")
    factvalue_tags.append("@offIndex")
    factvalue_tags.append("@endsource")
    factvalue_tags.append("@factvalue")
    factvalue_tags.append("@relSourceId")
    factvalue_tags.append("@relSourceText")
    factvalue_tags.append("@eventURI")
    factvalue_tags.append("@bsrc")
    factvalue_tags.append("@sourcelink")
    factvalue_tags.append("@esrc")
    factvalue_tags.append("@corpus")
    factvalue_tags.append("@URIcreator")
    factvalue_tags.append("@date")
    factvalue_tags.append("@datepub")

def documentTags():
    global document_tags
    document_tags = []
    document_tags.append("@document")
    document_tags.append("@title")
    document_tags.append("@docno")
    document_tags.append("@creator")
    document_tags.append("@creationdate")
    document_tags.append("@otherinfo")
    document_tags.append("@textnanopub")
    document_tags.append("@URICORP")
    document_tags.append("@dateNanopub")


def textTags():
    global text_tags
    text_tags = []
    text_tags.append("@textfile")
    text_tags.append("@textcontent")
    text_tags.append("@URICORP")
    text_tags.append("@creator")
    text_tags.append("@date")
    text_tags.append("@dateNanopub")
