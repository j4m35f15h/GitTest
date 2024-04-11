# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 12:21:29 2024

@author: James

Minor project to find a maximum sum for any possible sequence given a finite
list of integers. Minimises access to the original sequence when data struct
replaced with file (TBD). Prints the start index, end index and value of the 
sum of the optimum sequence.
"""
import copy
def CreateList(start,end):
    return [val for val in range(start,end)]

class infoStruct():
    
    def __init__(self,InputSequence = []):
        self.Seq = InputSequence # Store for the sequence
        self.IndexCombs = []     #Preallocation for the list of all possible sub-sequences
        self.ValCombs = []       #As above but contating values as opposed to indices
        
        ##Create all possible index combs
        CombList = []
        for i in range(len(self.Seq)): #For each starting intex
            for j in range(len(self.Seq)-i): #For each possible end given start
                CombList.append(CreateList(i,i+j+1)) #Add list of indexes 
            self.IndexCombs.append(CombList)
            CombList = []
    
    ##Convert Index lists of sub-sequences into Value lists
    def produceValCombs(self):
        self.ValCombs = copy.deepcopy(self.IndexCombs)  #Copy of indexes to be edited
        for index,val in enumerate(self.Seq):           #For each value in the original sequence
            for startIndex,j in enumerate(self.IndexCombs): #Look over each start index ...
                for CombCount,k in enumerate(j):        #... and into each sub-sequence
                    for EleCount,CombEle in enumerate(k):   #... and finally the values in each sub-sequence
                        if CombEle == index:             #Replace when values match
                            self.ValCombs[startIndex][CombCount][EleCount] = val
        

def MaxSeqSum(Seq = []):
    
    SeqCont = infoStruct(Seq)

    SeqCont.produceValCombs()
    
    startIndex = []
    endIndex = []
    combSum = []    
    print("Start index = {}; End index = {}; Sum = {}".format(startIndex,endIndex,combSum))
    return SeqCont