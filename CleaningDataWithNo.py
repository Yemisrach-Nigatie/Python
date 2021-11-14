# -*- coding: utf-8 -*-

import os #provides functions for interacting with the operating system
import math #gives access to the underlying C library functions for floating point math
import codecs #using UTF-8 characters of most languages in the world can be used simultaneously in string literals and comments
import sys #Common utility scripts often invoke processing command line arguments
import string

# The program introduces the class at first but all the program starts @ the end when we create an object for the class( ob=AMHARIC() )

class AMHARIC:# this is a class called (Amharic) that have only one function in it called(preprocessing). 
    def preprocessing(self, path):# a preprocessing function that have three sub functions and statements in it 
        def punct_remover(str):# function that helps to remove punctuation marks from the document
            if str.endswith('\n'):
                str=str.rstrip('\n')
            if str.startswith(' '):
                str=str.lstrip(' ')
            p=codecs.open("Punctuation.txt",'r', encoding = 'utf-8')
            Punctuation = p.read()
            for pc in Punctuation:
                if str.endswith(pc):
                    str=str.rstrip(pc)
                if str.startswith(pc):
                    str=str.lstrip(pc)
            for j in Punctuation:
                for i in range(1,len(str)):
                    if j in Punctuation and j in str:
                        str=str.strip(j)
            return str

        def Newline(str):# function that helps to remove punctuation marks from the document
            p=codecs.open("terminators.txt",'r', encoding = 'utf-8')
            Punctuation = p.read()
            c=''
            for j in Punctuation:
                if str[-1:] == j:
                    if str[-2:] == '፡፡':
                        c=str+"\n"
                        break
                    if str[-2:] != '፡፡':
                        if str[-1:] == '፡':
                            c=str[:len(str)-1]+" "
                            break
                    if str[-2:] == '::':
                        c=str+"\n"
                        break
                    if str[-2:] != '::':
                        if str[-1:] != ':':
                            c=str+"\n"
                            break
                        if str[-1:] == ':':
                            c=str[:len(str)-1]+" "
                            break
                if str[-1:] != j:
                    c=str+" "
            return c
        def Non_Amharic_Char_Remover(str):
            if str.endswith('\n'):
                str=str.rstrip('\n')
            if str.startswith(' '):
                str=str.lstrip(' ')
            k=[]
            beginNum = ord("ሀ")
            endNum = ord("፼")
            Exp1 = ord("?")
            Exp2 = ord("!")
            beginNo = ord("0")
            endNo = ord("9")
            punct = ord(":")
            for j in str: 
                if ord(j)>=beginNum and ord(j)<=endNum:
                    k.append(j)         
                if ord(j) == Exp1:
                    k.append(j)
                if ord(j) == Exp2:
                    k.append(j)
                if ord(j)>=beginNo and ord(j)<=endNo:
                    k.append(j)
                if ord(j) == punct:   
                    k.append(j)
                
            str=""
            for i in k:
                str=str+i
            return str
        def file_reader(filename):# this helps to read the file and return a list 
            indexterms=[]
            infile=codecs.open(filename, encoding='utf-8')
            lterms=infile.readlines()
            infile.close()
            for str in lterms:
                if str.endswith('\n'):
                    str=str.rstrip('\n')
                indexterms.append(str)
            return indexterms 
        fileterms=file_reader(path)#prepro statement that call the filereader function by passing an argument (path: is parameter in prepro function which is initialized when the prepro function is called)
        indexterms=[]# it is used to store each terms in the document after preprocessing 
        X=[]
        for term in fileterms:
            for index in term.split():
                # All the work have been done in this loop
                # The terms that are found in the fileterms are splited and the loop can access each term by (index) then it is passed as an argument on (PunctRemoverDef(index))
                indexterms.append(punct_remover(Non_Amharic_Char_Remover(index)))
        for x in indexterms:
            if (x!=""):
                X.append(x)
        f1=codecs.open('Amharic_Preprocessing.txt','w', encoding="utf-8")# opening a txt file to write; note that 'w': indicates writing and 'r': indicates reading
        for i in X:#indexterms:# A loop that accesses each term in the list indexterms
            s=Newline(i)
            #f1.write(i)
            f1.write(s)
        f1.close()
        #print ("before preprocessing!!!")
        #print ("...............................................................................")
        #f=codecs.open('Amharic_Sentences.txt','r', encoding="utf-8")#opens a raw file to read
        #print (" ",f.read()," ")#prints what is found in the file
        #f.close()
        print ('=========================================================================')
        print ('=========================================================================')
        print ("after preprocessing)!!!")
        print ("...............................................................................")
        f=codecs.open('Amharic_Preprocessing.txt','r', encoding="utf-8")#Opens a preprocessed file to read
        print (" ",f.read()," ")#prints what is found in the file
        f.close()
ob=AMHARIC()
ob.preprocessing("Amharic_Sentences.txt")# creation of an object for the class Amharic
