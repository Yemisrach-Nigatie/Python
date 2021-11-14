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
        f2=codecs.open(path,'r', encoding="utf-8")
        Sen=f2.readlines()
        f2.close()
        Lis=[]
        Lis2=[]
        Lis3=[]
        Lis4=[]
        n=0
        f1=codecs.open('MorphTsvTrain2.txt','w', encoding="utf-8")
        for i in range(0,len(Sen),1):
            a=str(i+1)
            for index in Sen[i].split():
                Lis2.append(index)
        for i in range(0,len(Lis2),1):
            if Lis2[i]=='word:' or Lis2[i]=='?word:':
                Lis3.append(Lis2[i+1])
                n=i
                for x in range(n,len(Lis2),1):
                    if Lis2[x]=='?word:'  and Lis2[x+2]=='word:':
                        Lis.append('_NILL_')
                        break
                    if Lis2[x]=='word:' and x!= len(Lis2)-2:
                        if Lis2[x+2]=='word:':
                            Lis.append('_NILL_')
                            break
                        if Lis2[x+2]=='?word:':
                            Lis.append('_NILL_')
                            break
                    if Lis2[x]=='!' or Lis2[x]=='?' or Lis2[x]=='፡፡' or Lis2[x]=='።' or Lis2[x]=='፤' or Lis2[x]=='::':
                        Lis.append('_NILL_')
                        break
                    if Lis2[x]=='stem:' or Lis2[x]=='citation:':
                        Lis.append(Lis2[x+1])
                        break
                for x in range(n,len(Lis2),1):
                    if Lis2[x]=='?word:'  and Lis2[x+2]=='word:':
                        Lis4.append('_NILL_')
                        break
                    if Lis2[x]=='word:' and x!= len(Lis2)-2:
                        if Lis2[x+2]=='word:': 
                            Lis4.append('_NILL_')
                            break
                        if Lis2[x+2]=='?word:':
                            Lis4.append('_NILL_')
                            break
                    if Lis2[x]=='!' or Lis2[x]=='?' or Lis2[x]=='፡፡' or Lis2[x]=='።' or Lis2[x]=='፤' or Lis2[x]=='::':
                        Lis4.append('_NILL_')
                        break
                    if Lis2[x]=='POS:' or Lis2[x]=='?POS:':
                        if Lis2[x+1][len(Lis2[x+1])-1:]==',':
                            Lis4.append(Lis2[x+1][:len(Lis2[x+1])-1])
                            break
                        if Lis2[x+1][len(Lis2[x+1])-1:]!=',':
                            Lis4.append(Lis2[x+1]+" "+Lis2[x+2][:len(Lis2[x+2])-1])
                            break
        Sen1=[]
        s=""
        for x in range(0,len(Lis3),1):
            s=s+Lis3[x]+" "
            if Lis3[x]=='!' or Lis3[x]=='?' or Lis3[x]=='፡፡' or Lis3[x]=='።' or Lis3[x]=='፤' or Lis3[x]=='::':
                Sen1.append(s)
                s=""
                continue
        n=0
        k=0
        for i in range(0,len(Sen1),1):
            a=str(i+1)
            f1.write('\n')
            n=n+len(Sen1[i].split())
            b=0
            for j in range(k,n,1):
                b=b+1
                f1.write(a)
                f1.write('-')
                f1.write(str(b))
                f1.write("\t")
                f1.write(Lis3[j])
                f1.write('\t')
                f1.write(Lis[j])
                f1.write('\t')
                f1.write(Lis4[j])
                f1.write('\n')
            k=k+len(Sen1[i].split())
        f1.close()
        print ("before preprocessing!!!")
        print ("...............................................................................")
        f=codecs.open('MorphoAnaTrainset.txt','r', encoding="utf-8")#opens a raw file to read
        print (" ",f.read()," ")#prints what is found in the file
        f.close()
        print ('=========================================================================')
        print ('=========================================================================')
        print ("after preprocessing)!!!")
        print ("...............................................................................")
        f=codecs.open('MorphTsvTrain2.txt','r', encoding="utf-8")#Opens a preprocessed file to read
        print (" ",f.read()," ")#prints what is found in the file
        f.close()
ob=AMHARIC()
ob.preprocessing("MorphoAnaTrainset.txt")# creation of an object for the class Amharic
