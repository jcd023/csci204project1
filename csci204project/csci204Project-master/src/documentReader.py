"""
Class used to read a document.
Each document will be product by one instance of a DocumentReader

IF DATA IS MISSING, will be noted at ??? in the file 
"""

#Will be used when we find an exceptions
from userExceptions import *
#All documents contain multiple sentences
from sentence import *
#Will produce a document
from document import *
from userExceptions import * ##Import exceptions
import os, sys ##Import os to parse folders/files
import datetime

class DocumentReader:
    """
    Used to read in a document
    """
    
    def __init__(self, fname = ""):
        """Pre: fname is one of the files in the train directory, is a string
           Post: self.__fname is set, self.__fileRef is set given fname
        """
        self.__fname = fname
        self.__fileRef = None #Will store the reference to file when open
        '''
        #Check to see that fname given is an existing file
        curPath = os.getcwd() #The file we are in now, src
        projPath = os.path.dirname(curPath) #Go out to csci204Project-master folder
        trainPath = os.path.join(projPath, 'train') #Go into train file containing emails
        
        posPath1 = os.path.join(trainPath, 'phillip.allen@enron.com') #Possible email we are checking
        posPath2 = os.path.join(trainPath, 'tana.jones@enron.com') #The other possible email
        
        fullPath1 = os.path.join(posPath1, fname) #Full path for Phillip Allen
        fullPath2 = os.path.join(posPath2, fname) #Full path for Tana Jones

        #There are some files with the same name in both folders, specify
        if os.path.isfile(fullPath1) is True and os.path.isfile(fullPath2) is True:
            file = int(input('Please specify file, enter 1 for Phillip, 2 for Tana: '))
            if file == 1:
                self.__fileRef = fullPath1
            elif file == 2:
                self.__fileRef = fullPath2
        #If file is in Phillip's folder
        elif os.path.isfile(fullPath1) is True:
            self.__fileRef = fullPath1
        #If file is in Tara's folder
        elif os.path.isfile(fullPath2) is True:
            self.__fileRef = fullPath2
        else:
            raise OurInFileException('File does not exist')
        '''

    
    def getFName(self, fname):
        """Pre: fname is a file in the train directory
           Post: the full path of fname is returned
        """
        #FILLED
        return self.__fname
    
    def __openFile(self):
        """
        Private function used to open the file and test if it exists
        """
        fullPath = self.__fname #Get path name to open file
        
        doc = open(fullPath, 'r') #open file
        return doc
        
    
    def readFile(self):
        """
        Will open (if not already open)/read the file
        Make a Document and return
        If any Error, throws error
        Format of file is MIME EMAIL
        """
        doc = self.__openFile() #Get opened file from __openFile()
        readDoc = doc.read() #Read document contents

        ##GET BODY OF DOC EXCLUDING FORWARD/ORIGINAL MESSAGES
        #Get start of message
        for i in range(len(readDoc)):
            if readDoc[i:i+13] == '\nX-FileName: ':
                index = i+13
                message1 = readDoc[index:]
        for j in range(len(message1)):
            if message1[j:j+2] == '\n\n':
                index = j+2
                message2 = message1[index:]
                break
        #Get message excluding forwarded or original message
        for k in range(len(message2)):
            if message2[k:k+4] == '----' or message2[k:k+3] == '\n\n\n\n':
                index = k
                mesFinal = message2[:k]
                break
            else:
                mesFinal = message2

        ##GET SENTENCES FROM Body of Message (mesFinal)
        #sentences HOLDS INFO FOR self.__sentences
        sentences = []
        startIndex = 0
        for i in range(len(mesFinal)):
            if mesFinal[i] == '.' or mesFinal[i] == '!' or mesFinal[i] == '?':
                sentences += [Sentence(mesFinal[startIndex : i+1])]
                startIndex = i + 1

        ##GET FROM EMAIL INFO
        ##fromInfo HOLDS INFO NEEDED FOR __fromInfo
        fromInfo = os.path.basename(os.path.dirname(self.__fname))

        ##GET TO EMAIL INFO, NEED TO PARSE doc
        ##toEmail HOLDS INFO NEEDED FOR __toInfo
        for i in range(len(readDoc)):
            if readDoc[i:i+5] == '\nTo: ':
                index = i+5
                toInfo = ''
                for j in range(len(readDoc) - index):
                    if readDoc[index + j] == ',' or readDoc[index + j] == '\n'\
                       or readDoc[index + j] == '/':
                        break
                    else:
                        toInfo += readDoc[index + j]

        ##GET DATE, NEED TO PARSE doc
        ##day, month, year HOLDS INFO NEEDED FOR Document __date attribute
                        
        for i in range(len(readDoc)):
            if readDoc[i:i+6] == 'Date: ':
                
                dayIndex = i+6 + 5 #Account for the Mon, Tue, etc. in front of date
                day = '' #set up string to hold day
                month = '' #month
                year = '' #year
                
                #Find day
                for j in range(len(readDoc)):
                    if readDoc[dayIndex + j].isspace():
                        moIndex = dayIndex + j + 1
                        break
                    else:
                        day += readDoc[dayIndex + j]
                        
                #Find month
                for j in range(len(readDoc)):
                    if readDoc[moIndex + j].isspace():
                        yrIndex = moIndex + j + 1
                        break
                    else:
                        month += readDoc[moIndex + j]
                        
                #Find year
                for j in range(len(readDoc)):
                    if readDoc[yrIndex + j].isspace():
                        break
                    else:
                        year += readDoc[yrIndex + j]
                        
                #Convert to integers
                day = int(day)
                year = int(year)
                
                monthWord = str.lower(month)
                posMonths = ['jan','feb','mar', 'apr','may','jun','jul','aug','sep','oct','nov','dec']
                month = 0
                for i in range(len(posMonths)):
                    if posMonths[i] == monthWord:
                        month = i+1

        ##CREATE DOCUMENT, ADDING INFO FOUND ABOVE
        docRead = Document(toInfo, fromInfo)
        docRead.setDate(year, month, day)
        for i in range(len(sentences)):
            docRead[i] = sentences[i]

        ##FUNCTION RETURNS CREATED DOCUMENT
        return docRead

        ###NEED TO ADD COMMENTS
        ###NEED TO ADD DOCSTRINGS
        ###BETTER NAMES FOR VARIBALES IF NEEDED
        ###ADD EXCEPTIONS IF NEEDED

        
        

    def checkFileFormat():
        """
        Will open the file (if not already open)
        Will test if it is a correctly formatted MIME EMAIL
        """
        pass



def testDocumentReader():
    """
    Used to test your DocumentReader class
    """
    '''
    d = DocumentReader('14').readFile()
    print('Body of Email:')
    for i in range(d.getSCount()):
        print(d[i])
    print('\n')
    print('Date of email (year, month, day): ', d.getDate())
    print('\n')
    print('Email recipient: ', d.getToInfo())
    print('\n')
    print('Email sender: ', d.getFromInfo())
    '''
    pass
    
if __name__ == "__main__":
    testDocumentReader()
