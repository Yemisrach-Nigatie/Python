# -*- coding: utf-8 -*-

import os #provides functions for interacting with the operating system
import math #gives access to the underlying C library functions for floating point math
import codecs #using UTF-8 characters of most languages in the world can be used simultaneously in string literals and comments
import sys #Common utility scripts often invoke processing command line arguments
import string
import l3
# The program introduces the class at first but all the program starts @ the end when we create an object for the class( ob=AMHARIC() )

class AMHARIC:# this is a class called (Amharic) that have only one function in it called(preprocessing). 
    def preprocessing(self, path):# a preprocessing function that have three sub functions and statements in it                
        def hornmorpho(path):
            l3.anal_file('am',path,'MorphoAnaTrainSet.txt')
        hornmorpho(path)
        # then the following will be displayed on the screen
##        print ('=========================================================================')
##        print ('=========================================================================')
##        print ("after preprocessing!!!")
##        print ("...............................................................................")
##        f=codecs.open('trainset.txt','r', encoding="utf-8")#Opens a preprocessed file to read
##        print (" ",f.read()," ")#prints what is found in the file
##        f.close()
##        print ('=========================================================================')
##        print ('=========================================================================')
##        print ("after morphological analysis!!!")
##        print ("...............................................................................")
##        f=codecs.open('MorphologicalAnalysisOne.txt','r', encoding="utf-8")#Opens a preprocessed file to read
##        print (" ",f.read()," ")#prints what is found in the file
##        f.close()
ob=AMHARIC()# creation of an object for the class Amharic
ob.preprocessing("trainset.txt")# calling a function  preprocessing by using the object name and by passing an argument.
