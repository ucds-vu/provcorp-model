import sys
import subprocess
import os
import getopt
import xml.etree.ElementTree as ET
from classes.sentence import Sentence
from classes.word import Word
from classes.attribute import Attribute
from classes.document import Document
from preprocess.preprocess_txt import *
from preprocess.preprocess_ann_parc import *
import templates.tags as tags
from generateNanopub import *
