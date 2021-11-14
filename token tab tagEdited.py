# -*- coding: utf-8 -*-

import os #provides functions for interacting with the operating system
import math #gives access to the underlying C library functions for floating point math
import codecs #using UTF-8 characters of most languages in the world can be used simultaneously in string literals and comments
import sys #Common utility scripts often invoke processing command line arguments
import string

# The program introduces the class at first but all the program starts @ the end when we create an object for the class( ob=AMHARIC() )

class AMHARIC:# this is a class called (Amharic) that have only one function in it called(preprocessing). 
    def preprocessing(self, path):# a preprocessing function that have three sub functions and statements in it 
        Sen=[]
        f2=codecs.open('OOV.tagged','r', encoding="utf-8")
        Sen=f2.readlines()
        f2.close()
        Lis=[]
        f1=codecs.open('OOVT.txt','w', encoding="utf-8")
        for i in range(0,len(Sen),1):
            a=str(i+1)
            
            Lis=[]
            f1.write('\n')
            f1.write(Sen[i])
            f1.write('\n')
            for index in Sen[i].split():
                Lis.append(index)
            for j in range(0,len(Lis),1):
                for x in Lis[j]:
                    if x != "|" and x != " ":
                        f1.write(x)
                    if x == "|":
                        f1.write("\t")
                f1.write("\n")
            
        f1.close()
        print ("before preprocessing!!!")
        print ("...............................................................................")
        f=codecs.open('OOV.tagged','r', encoding="utf-8")#opens a raw file to read
        print (" ",f.read()," ")#prints what is found in the file
        f.close()
        print ('=========================================================================')
        print ('=========================================================================')
        print ("after preprocessing)!!!")
        print ("...............................................................................")
        f=codecs.open('OOVT.txt','r', encoding="utf-8")#Opens a preprocessed file to read
        print (" ",f.read()," ")#prints what is found in the file
        f.close()
ob=AMHARIC()
ob.preprocessing("OOV.tagged")# creation of an object for the class Amharic
