# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 15:09:47 2021

@author: manoranjan.parida
"""

class ReadArticles:
    
    def __init__(self):
        self.dataPath = r'C:\Users\manoranjan.parida\deployment\ga2803-master\data\article1.txt'
        self.stopWordPath = r'C:\Users\manoranjan.parida\deployment\ga2803-master\data\stopWords.txt'
            
    def loadArticlesFromFile(self):
        with open(self.dataPath,'r') as fl:
            text = fl.read()
        return text
    
    def stopWordsFromFile(self):
        with open(self.stopWordPath,'r') as fl:
            text = fl.read()
        return text.split('\n')
        
    def loadArticlesFromDb(self):
        pass
    
    def loadArticlesFromApi(self):
        pass
    
#readObj = ReadArticles()
#articleText = readObj.loadArticlesFromFile()
#print('The text is:\n\n{}'.format(articleText))