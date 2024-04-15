# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 09:47:11 2024

Reverses the BW Compression.

@author: James
"""

def expandString(stringIn):
    """
    Replaces the shortened compressed sequences, replacing the idential 
    sequential characters that were removed. e.g.:
        ACA3G -> ACAGGG
    """
    outputString = ""
    
    i = 0
    while i<len(stringIn): #While char index < length of string
        
        #If end of string, add final character and exit
        if(i+1>len(stringIn)): 
            outputString+=stringIn[i] 
            break
        
        #If char is a number n, add the char that follows n times
        #and step across
        if(str.isdigit(stringIn[i])): #If character is a number...
            outputString+=int(stringIn[i])*stringIn[i+1]
            i+=2
            continue
        
        #Otherwise add current char to output
        outputString+=stringIn[i]
        i+=1
    return outputString    
    
def charRank(stringIn,index):
    """
    From a string, identifies the rank of the char for the sorted string:
        AAACCCT
            ^
    Returns 2, for the 2nd "C"
    """
    counter = 0
    
    #zeroeth char is always first
    if index == 0:
        return 1
    
    #Starting from char of interest, step back until different char and return 
    #number of steps
    for i in range(index,0,-1):
        if stringIn[i]!=stringIn[index]:
            break
        counter+=1
    return counter

def findIndexRank(compString,key,index,rank):
    """
    Finds the corresponding index of the char of the same rank from the key in
    the compressed string
    """
    counter = 0
    #For all chars in the reference string
    for newIndex,i in enumerate(compString):
        #If the char in reference matches the char of interest in key...
        if i==key[index]:
            #...increment a counter
            counter+=1
            #If the counter mathces rank, index of char is returned
            if counter == rank:
                return newIndex

def BWDecomp(compString):
    outputString = ""
    #Add back in the duplicate characters.
    compString = expandString(compString)
    
    #Create the ordered key
    key = sorted(compString)
    
    #Find the end character
    index = compString.index("$")
    
    #Add char of same index in key to output
    outputString+=key[index]
    
    #While the end char not reached again
    while 1:
        
        #Identify the rank of the char in the key
        rank = charRank(key,index)
        
        #Look through the compString to find index of the same char w/ rank
        index = findIndexRank(compString,key,index,rank)
        
        #If its the end key, terminate...
        if key[index] == "$":
            break
        #...otherwise add the char to the output, and repeat
        outputString+=key[index]
    
    return outputString