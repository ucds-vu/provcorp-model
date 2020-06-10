from imports import *

class Attribute:
    def __init__(self, attribute):
        self.id = attribute.attrib.get("id")
        self.role = attribute[0].attrib.get("roleValue")
