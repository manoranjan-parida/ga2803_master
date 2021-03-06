# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:34:22 2021

@author: manoranjan.parida
"""

import numpy
from preprocessors import PreprocessText
import flask
from flask import Flask, request

summaryapp = Flask(__name__)

class summerizeArticle:
    
    def __init__(self):
        processObj = PreprocessText()
        self.sentArray = processObj.preprocess()
    
    def groupSentences(self, sentArray):
        firstsent = sentArray[0]
        restSents = sentArray[1:]
        return firstsent,restSents
    
    def sortsentences(self, restSents):
        sentLength = [len(sent) for sent in restSents]
        sortedIdxs = numpy.argsort(sentLength)
        sortedSentenece = []
        for idx in sortedIdxs:
            sortedSentenece.append(restSents[len(restSents) - idx -1])
        return sortedSentenece
    
    def combineSentences(self, firstsent, sortedSentenece):
        
        combinedSentences = [firstsent] + sortedSentenece[:5]
        summary = ' '.join(combinedSentences)
        return summary
    
    def summerize(self):
        firstsent, restSents = self.groupSentences(self.sentArray)
        sortedSentenece = self.sortsentences(restSents)
        summary = self.combineSentences(firstsent, sortedSentenece)
        return summary

@summaryapp.route('/home/summary', methods=['GET'])
def summaryApi():
    summaryObj = summerizeArticle()
    summary =summaryObj.summerize()
    return summary
    # print('The Summary is:\n\n{}'.format(summary))
    
summaryapp.run(host='127.0.0.1', port = 8001)
            