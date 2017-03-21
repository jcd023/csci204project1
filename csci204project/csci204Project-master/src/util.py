"""
This file will contain utility classes and functions
"""


class UserInput:
    """
    Class that will keep a record of user inputs
    """
    def __init__(self):
        self.tPath = ""
        self.ePath = ""
        self.__tDocument = [] #A List of training documents
        self.__eDocument = [] #A List of evaluation documents
        self.__textFilter = [] #A List of text filters

    def setTDocumnet(self, docList):
        pass

    def addTDocument(self, doc):
        """
        Add a training document
        """
        pass

    def getTDocument(self):
        """
        Returns the training document list
        """
        pass

    def setEDocument(self, docList):
        pass


    def addEDocument(self, doc):
        """
        Add an eval document
        """
        pass

    def setTextFilter(self, filter):
        pass
    
    def getTextFilter(self):
        pass
        


class TimerStats:
    """
    This class may be used to keep information on performance of your code
    """
    
    def __init__(self):
        pass
