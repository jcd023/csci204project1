"""
Class that will contain a document (Basic unit -- "Primary Data-Structure)
"""

from util import *
from sentence import *
import datetime
from userExceptions import * #Import exceptions

class Document:
    
    def __init__(self, toInfo = None, fromInfo = None, date=None):
        self.__sentences = []
        self.__sCount = -1 #Number of sentences
        self.__toInfo = toInfo #Who was the document to
        self.__fromInfo = fromInfo #Who was the document from
        self.__date = date
        self.__fwd = False
        self.__reply = False


    def __getitem__(self, index):
        """Pre: Index is an integer
           Post: returns the sentence containted in the document at the given index
        """
        return self.__sentences[index].getSString()

    def __setitem__(self, index, value):
        """Pre: Index is an integer, Value is a Sentence object
           Post: self[index] is set to be the inputted value
        """
        if isinstance(value, Sentence) is True:
            self.__sentences = self.__sentences + [None]
            self.__sentences[index] = value
        else:
            raise OurInFileException('Inputted value is not a sentence object')

    def getSCount(self):
        """Pre: A nonempty Document() is being acted upon
           Post: The number of sentences in the document is returned
        """
        #fill me (we should not have to ever set sCount)
        return len(self.__sentences)

    def setToInfo(self, value):
        """Pre: Value is a name or email, a string
           Post: self.__toInfo is set to given value
        """
        #fill me
        self.__toInfo = value

    def getToInfo(self):
        """Pre: A Document() is being acted upon
           Post: the information (name or email) of the receiver is returned
        """
        #fill me
        return self.__toInfo

    def setFromInfo(self, value):
        """Pre: Value is a name or email, a string
           Post: self.__fromInfo is set to given value
        """
        #fill me
        self.__fromInfo = value

    def getFromInfo(self):
        """Pre: A Document() is being acted upon
           Post: the information (name or email) of the sender is returned
        """
        #fill me
        return self.__fromInfo
    
    
    def setDate(self, year, month, day):
        """Pre: Year, month, day are all integers
           Post: self.__date is set utilizing datetime package
        """
        #should use date object in python datetime package
        mydate = datetime.date(year, month, day)
        #fill me
        self.__date = mydate

    def getDate(self):
        """Pre: A Document() is being acted upon
           Post: the date of the document is returned (Year, Month, Day)
        """
        #returns year,month,day
        return self.__date.year, self.__date.month, self.__date.day


    def setFwd(self, value):
        """Pre: Value is a name or email, a string
           Post: self.__fwd is set to given value
        """
        #fill me 
        self.__fwd = value

    def getFwd(self):
        """Pre: A Document() is being acted upon
           Post: the information (name or email) of the forwarder is returned
        """
        #fill me
        return self.__fwd

    def setReply(self,value):
        """Pre: Value is a name or email, a string
           Post: self.__reply is set to given value
        """
        #fill me
        self.__reply = value
    
    def getReply(self):
        """Pre: A Document() is being acted upon
           Post: the information (name or email) of the replier is returned
        """
        #fill me 
        return self.__reply



def testDocument():
    """
    Used to test your Document Class
    """
    #Set up a mock document
    d = Document()
    #Set document's sentences
    d[0] = Sentence('This is the first sentence in my email.')
    d[1] = Sentence('This is the second sentence in my email!')
    d[2] = Sentence('Sincerely, last sentence')
    #Get document's setences
    print(d[0])
    print(d[1])
    print(d[2])
    #Test getSCount()
    print('self.__sCount should be 3: ', d.getSCount())
    #Set toInfo
    d.setToInfo('friend@gmail.com')
    #Get toInfo
    print('To Info: ', d.getToInfo())
    #Set fromInfo
    d.setFromInfo('me@work.org')
    #Get fromInfo
    print('From Info: ', d.getFromInfo())
    #Set Date
    d.setDate(2017, 3, 6)
    #Get Date
    print('(Year, Month, Day): ', d.getDate())
    #Get Fwd
    d.setFwd('forward@gmail.com')
    #Set Fwd
    print('Forward Info: ', d.getFwd())
    #Set Reply
    d.setReply('reply@gmail.com')
    #Get Reply
    print('Reply Info: ', d.getReply())
    
if __name__ == "__main__":
    testDocument()





    
