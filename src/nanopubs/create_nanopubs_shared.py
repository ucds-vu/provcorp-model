import sys
import os
import subprocess

PATH_TEXT = "../corpora/factbank_v1/data/original"
PATH_PARC_ANN_00 = "../corpora/PARC3/00"
PATH_PARC_ANN_01 = "../corpora/PARC3/01"
INCORRECT_DOCUMENTS = ["NYT19981026.0446", "wsj_0781", "NYT19981121.0173", "NYT19981025.0216", "APW19990607.0041", "NYT19990312.0271", "APW19990206.0090", "NYT19981120.0362", "APW19991024.0075", "wsj_1014", "APW19990312.0251"]

def main():
    libraryPath = "/home/timo/Dropbox/provcorp"

    total_overlap = []
    original_files = []
    for r, d, f in os.walk(PATH_TEXT):
        for file in f:
            original_files.append(file[:-4])

    # WORKING ON 00 DIRECTORY OF PARC
    annotations_files = []
    for r, d, f in os.walk(PATH_PARC_ANN_00):
        for file in f:
            annotations_files.append(file[:-4])

    overlap = []
    for f in original_files:
        if f in annotations_files:
            overlap.append(f)
            total_overlap.append(f)

    for shared in overlap:
        filecontent = open(PATH_PARC_ANN_00 + "/" + shared + ".xml", "r")
        content = filecontent.read()
        if "attributionRole" in content:
            print("Working on %s\n" % shared)
            output = subprocess.check_output(['sh', './run+mktrusty.sh', shared + ".txt", "00/" + shared + ".xml", shared])
            print(output.decode('utf-8'))
        else:
            print("Working on %s\n" % shared)
            output = subprocess.check_output(['sh', './run+mktrusty_word_only.sh', shared + ".txt", "00/" + shared + ".xml", shared])
            print(output.decode('utf-8'))

    # WORKING ON 01 DIRECTORY OF PARC
    annotations_files = []
    for r, d, f in os.walk(PATH_PARC_ANN_01):
        for file in f:
            annotations_files.append(file[:-4])

    overlap = []
    for f in original_files:
        if f in annotations_files:
            overlap.append(f)
            total_overlap.append(f)


    for shared in overlap:
        filecontent = open(PATH_PARC_ANN_01 + "/" + shared + ".xml", "r")
        content = filecontent.read()
        if "attributionRole" in content:
            print("Working on %s\n" % shared)
            output = subprocess.check_output(['sh', './run+mktrusty.sh', shared + ".txt", "01/" + shared + ".xml", shared])
            print(output.decode('utf-8'))
        else:
            print("Working on %s\n" % shared)
            output = subprocess.check_output(['sh', './run+mktrusty_word_only.sh', shared + ".txt", "01/" + shared + ".xml", shared])
            print(output.decode('utf-8'))
    print("CREATING PARC indexes \n")
    result_index_creation = subprocess.check_output(['sh', './index_PARC.sh'])

    # PROCESSING THE REST OF FACTBANK

    print("STARTING ON DOCUMENTS THAT ARE ONLY IN FACTBANK\n")
    for text in original_files:
        if text in INCORRECT_DOCUMENTS:
            continue
        if text not in total_overlap and "SJMN" not in text and "WSJ" not in text:
            print("Working on %s\n" % text)
            output = subprocess.check_output(['sh', './run+mktrusty_fb.sh', text + ".txt", text])
            print(output.decode('utf-8'))




if __name__ == "__main__":
    main()
