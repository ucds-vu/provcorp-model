import sys
import subprocess
import os
import getopt
import re
import nltk
from preprocess.preprocess_ann_fb import *
from preprocess.preprocess_txt import *
from classes.event import *
from classes.factvalue import *
from classes.sentence import Sentence
from classes.document import Document
from classes.text import *
import templates.tags as tags
