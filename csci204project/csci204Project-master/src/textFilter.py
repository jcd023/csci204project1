"""
This class will filter the information inside a Document
and return a filtered (SAME) Document.
"""


from document import *


class TextFilter:
    """
    Applies a list of filter to a document and returns same filtered Document
    """

    def __init__(self, filterList=None, doc=None):
        self.__filterList = filterList
        self.__doc = doc

    def setFilterList(self, filterList):
        self.__filterList = filterList

    def setDoc(self, doc):
        self.__doc = doc

    def appy(self, doc=None):
        """
        doc is the Document we are applying each filter in the filterlist to
        """
        pass

    def normalizeWhiteSpace(self):
        pass

    def normalizeCase(self):
        pass
    
    def stripNull(self):
        pass

    def stripNumbers(self):
        pass

    def stripFiles(self):
        pass



def testTestFilter():
    """
    Put your test for the filter class here
    """
    pass


if __name__ == "__main__":
    testTestFilter()





