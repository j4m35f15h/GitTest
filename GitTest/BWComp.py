# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 15:48:06 2024

Carries out BW Compression, which is a text compression algorithm. Part of a 
bioinformatics project, so the intended use is with sequences from fasta/fastq
files

@author: James
"""

def BWComp(inputSequence = ""):
    rawString = ""
    compressedString = ""
    compressionTable = []
    
    #Add a '$' character to end of string
    inputSequence+="$"

    #For every position in the string, add rotated string to table
    for i in range(len(inputSequence)):
        compressionTable.append(inputSequence[i:]+inputSequence[:i])
    
    #Sort the compression table by first char
    compressionTable=sorted(compressionTable)
    
    #Extract final char of compression table
    for i in compressionTable:
        rawString+=i[-1]
    
    ##Final stage is to convert sequential duplicates into a numerical form
    
    #Create Gradient to find edges of similar regions. Add "0" for first
    #instance of character in sequence, add "1" for sequential identical chars
    gradString = "0"
    for i in range(1,len(rawString)):
        if rawString[i]==rawString[i-1]:
            gradString+="1"
        else:
            gradString+="0"
    
    #Add non indential sequential characters to the output. When identical
    #sequential characters are found, count number, and add the value then char
    #to the output. Continue looking from position after the count.
    offset = 0
    for i in range(len(gradString)):
        
        if i+offset>=len(gradString):
            break
        
        #If non identical char, add to output
        if gradString[i+offset] == "0":
            compressedString+=rawString[i+offset]
            continue
        
        #Step through string, and if identical char found, continue
        counter = 2
        offset+=1
        while(i+offset<len(gradString)): #Terminates if end of string or seq
            if gradString[i+offset] == "1":
                counter+=1
                offset+=1
                continue
            break
    
        #Remove single char and add number of sequential char followed by char
        compressedString=compressedString[:-1]
        compressedString+="{}{}".format(counter,rawString[i+offset-1])
        
        #If sequnce ended at end of string
        if (i+offset==len(gradString)):
            break
        
        #If sequence ended in new char, add to string and increment i
        if gradString[i+offset] == "0":
            compressedString+=rawString[i+offset]
            continue
        
    return compressedString
