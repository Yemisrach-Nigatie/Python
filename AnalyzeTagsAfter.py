# -*- coding: utf-8 -*-

import os #provides functions for interacting with the operating system
import math #gives access to the underlying C library functions for floating point math
import codecs #using UTF-8 characters of most languages in the world can be used simultaneously in string literals and comments
import sys #Common utility scripts often invoke processing command line arguments
import string

# The program introduces the class at first but all the program starts @ the end when we create an object for the class( ob=AMHARIC() )

class AMHARIC:# this is a class called (Amharic) that have only one function in it called(preprocessing). 
    def preprocessing(self, path):# a preprocessing function that have three sub functions and statements in it 
        Sen1=[]
        Sen2=[]
        f1=codecs.open(path,'r', encoding="utf-8")
        Sen1=f1.readlines()
        f1.close()
        
        Str=""
        f1=codecs.open('AnalyzedTextAfter.txt','w', encoding="utf-8")
        for i in range(0,len(Sen1),3):
            Lis3=[]
            Lis1=[]
            f1.write(Sen1[i])
            for r in Sen1[i+1].split():
                n=1
                for i in range(0,len(Lis3),1):
                    if Lis3[i]==r:
                        Lis1[i]=Lis1[i]+1
                        n=n+1
                        break
                if n==1:
                    Lis3.append(r)
                    Lis1.append(n)
            for x in range(0,len(Lis3),1):
               f1.write(Lis3[x])
               f1.write("(")
               f1.write(str(Lis1[x]))
               f1.write(") ")
            f1.write("\n\n")
        f1.close()
##        print ("before preprocessing!!!")
##        print ("...............................................................................")
##        f1=codecs.open('TaggedText.txt','r', encoding="utf-8")#opens a raw file to read
##        print (" ",f1.read()," ")#prints what is found in the file
##        f1.close()
##        print ('=========================================================================')
##        print ('=========================================================================')
##        print ("after preprocessing)!!!")
##        print ("...............................................................................")
##        f=codecs.open('AnalyzedTextAfter.txt','r', encoding="utf-8")#Opens a preprocessed file to read
##        print (" ",f.read()," ")#prints what is found in the file
##        f.close()
ob=AMHARIC()
ob.preprocessing('TaggedText.txt')# creation of an object for the class Amharic
