"""
This is the file that contains your dicision tree
"""



class DTreeNode:
    """
    Your Node Class for your dicision tree
    """
    
    def __init__(self, key, data=None):
        """
        I am allowing these to be public to manipulate them easy
        """
        self.key = key
        self.data = data
        



class MyDecisionTree:
    """
    Will contain your deicision tree algorithm
    """
    
    def __init__(self):
        self.__myRoot = None
        self.__maxHeight = -1
        self.__minHeight = -1


    def train(self, xData, yData, maxDepth):
        """
        External interface for building the tree
        """
        pass


    def eval(self, xData):
        """
        External interface for evaluating the tree (Predicting)
        """
        pass

    
    def __recursiveBuild(self, root, xData, yData, maxDepth):
        """
        Where you really will build the tree
        """
        pass



def testMyDecisionTree():
    """
    Used for your testing
    """
    pass


if __name__ == "__main__":
    testMyDecisionTree()
