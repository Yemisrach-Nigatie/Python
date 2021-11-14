# -*- coding: utf-8 -*-

import os #provides functions for interacting with the operating system
import math #gives access to the underlying C library functions for floating point math
import codecs #using UTF-8 characters of most languages in the world can be used simultaneously in string literals and comments
import sys #Common utility scripts often invoke processing command line arguments
import string

# The program introduces the class at first but all the program starts @ the end when we create an object for the class( ob=AMHARIC() )

class AMHARIC:# this is a class called (Amharic) that have only one function in it called(preprocessing). 
    def preprocessing(self, path):# a preprocessing function that have three sub functions and statements in it 
        test=[]
        f1=codecs.open(path,'r', encoding="utf-8")
        test=f1.readlines()
        f1.close()
        f1=codecs.open('Computation.txt','w', encoding="utf-8")
        tpPN=0
        tpCN=0
        tpC=0
        tpA=0
        tpV=0
        tpAv=0
        tpAN=0
        tpP=0
        tpAd=0
        tpEN=0
        tpPu=0
        tpAb=0
        fpPN=0
        fpCN=0
        fpC=0
        fpA=0
        fpV=0
        fpAv=0
        fpAN=0
        fpP=0
        fpAd=0
        fpEN=0
        fpPu=0
        fpAb=0
        tnPN=0
        tnCN=0
        tnC=0
        tnA=0
        tnV=0
        tnAv=0
        tnAN=0
        tnP=0
        tnAd=0
        tnEN=0
        tnPu=0
        tnAb=0
        fnPN=0
        fnCN=0
        fnC=0
        fnA=0
        fnV=0
        fnAv=0
        fnAN=0
        fnP=0
        fnAd=0
        fnEN=0
        fnPu=0
        fnAb=0
        List1=[]
        List=[]
        for line in test:
            List1.append(line)
        print (len(List1))
        for i in range(0,len(List1),1):
            List2=[]
            for index in List1[i].split():
                List2.append(index)
            for j in range(2,len(List2),2):
                if List2[j+1] == 'ProNou':
                    if List2[j] == List2[j+1]:
                        tpPN=tpPN+1
                    if List2[j] != List2[j+1]:
                        fpPN=fpPN+1
                if List2[j] == "ProNou":
                    fnPN=fnPN+1
                if List2[j+1] == 'ComNou':
                    if List2[j] == List2[j+1]:
                        tpCN=tpCN+1
                    if List2[j] != List2[j+1]:
                        fpCN=fpCN+1
                if List2[j] == "ComNou":
                    fnCN=fnCN+1
                if List2[j+1] == 'Con':
                    if List2[j] == List2[j+1]:
                        tpC=tpC+1
                    if List2[j] != List2[j+1]:
                        fpC=fpC+1
                if List2[j] == "Con":
                    fnC=fnC+1
                if List2[j+1] == 'Adj':
                    if List2[j] == List2[j+1]:
                        tpA=tpA+1
                    if List2[j] != List2[j+1]:
                        fpA=fpA+1
                if List2[j] == "Adj":
                    fnA=fnA+1
                if List2[j+1] == 'Ver':
                    if List2[j] == List2[j+1]:
                        tpV=tpV+1
                    if List2[j] != List2[j+1]:
                        fpV=fpV+1
                if List2[j] == "Ver":
                    fnV=fnV+1
                if List2[j+1] == 'Adv':
                    if List2[j] == List2[j+1]:
                        tpAv=tpAv+1
                    if List2[j] != List2[j+1]:
                        fpAv=fpAv+1
                if List2[j] == "Adv":
                    fnAv=fnAv+1
                if List2[j+1] == 'AraNum':
                    if List2[j] == List2[j+1]:
                        tpAN=tpAN+1
                    if List2[j] != List2[j+1]:
                        fpAN=fpAN+1
                if List2[j] == "AraNum":
                    fnAN=fnAN+1
                if List2[j+1] == 'Pron':
                    if List2[j] == List2[j+1]:
                        tpP=tpP+1
                    if List2[j] != List2[j+1]:
                        fpP=fpP+1
                if List2[j] == "Pron":
                    fnP=fnP+1
                if List2[j+1] == 'Adp':
                    if List2[j] == List2[j+1]:
                        tpAd=tpAd+1
                    if List2[j] != List2[j+1]:
                        fpAd=fpAd+1
                if List2[j] == "Adp":
                    fnAd=fnAd+1
                if List2[j+1] == 'EthNum':
                    if List2[j] == List2[j+1]:
                        tpEN=tpEN+1
                    if List2[j] != List2[j+1]:
                        fpEN=fpEN+1
                if List2[j] == "EthNum":
                    fnEN=fnEN+1
                if List2[j+1] == 'Pun':
                    if List2[j] == List2[j+1]:
                        tpPu=tpPu+1
                    if List2[j] != List2[j+1]:
                        fpPu=fpPu+1
                if List2[j] == "Pun":
                    fnPu=fnPu+1
                if List2[j+1] == 'Abb':
                    if List2[j] == List2[j+1]:
                        tpAb=tpAb+1
                    if List2[j] != List2[j+1]:
                        fpAb=fpAb+1
                if List2[j] == "Abb":
                    fnAb=fnAb+1
        P1=tpPN/(tpPN+fpPN)
        R1=tpPN/(fnPN)
        P2=tpCN/(tpCN+fpCN)
        R2=tpCN/(fnCN)
        P3=tpC/(tpC+fpC)
        R3=tpC/(fnC)
        P4=tpA/(tpA+fpA)
        R4=tpA/(fnA)
        P5=tpV/(tpV+fpV)
        R5=tpV/(fnV)
        P6=tpAv/(tpAv+fpAv)
        R6=tpAv/(fnAv)
        P7=tpAN/(tpAN+fpAN)
        R7=tpAN/(fnAN)
        P8=tpP/(tpP+fpP)
        R8=tpP/(fnP)
        P9=tpAd/(tpAd+fpAd)
        R9=tpAd/(fnAd)
        P10=tpEN/(tpEN+fpEN)
        R10=tpEN/(fnEN)
        P11=tpPu/(tpPu+fpPu)
        R11=tpPu/(fnPu)
        P12=tpAb/(tpAb+fpAb)
        R12=0
        A1 = (tpPN + tnPN)/(tpPN + fpPN + (fnPN-tpPN) + tnPN)
        A2 = (tpCN + tnCN)/ (tpCN + fpCN + (fnCN-tpCN)+ tnCN)
        A3 = (tpC + tnC)/ (tpC + fpC + (fnC-tpC) + tnC)
        A4 = (tpA + tnA)/ (tpA + fpA + (fnA-tpA) + tnA)
        A5 = (tpV + tnV)/ (tpV + fpV + (fnV-tpV) + tnV)
        A6 = (tpAv + tnAv)/ (tpAv + fpAv + (fnAv-tpAv) + tnAv)
        A7 = (tpAN + tnAN)/ (tpAN + fpAN + (fnAN-tpAN) + tnAN)
        A8 = (tpP + tnP)/ (tpP + fpP + (fnP-tpP) + tnP)
        A9 = (tpAd + tnAd)/ (tpAd + fpAd + (fnAd-tpAd) + tnAd)
        A10 = (tpEN + tnEN)/ (tpEN + fpEN + (fnEN-tpEN) + tnEN)
        A11 = (tpPu + tnPu)/ (tpPu + fpPu + (fnPu-tpPu) + tnPu)
        A12 = (tpAb + tnAb)/ (tpAb + fpAb + (fnAb-tpAb) + tnAb)
        F1 = (2*R1*P1)/ (R1+P1)
        F2 = (2*R2*P2)/ (R2+P2)
        F3 = (2*R3*P3)/ (R3+P3)
        F4 = (2*R4*P4)/ (R4+P4)
        F5 = (2*R5*P5)/ (R5+P5)
        F6 = (2*R6*P6)/ (R6+P6)
        F7 = (2*R7*P7)/ (R7+P7)
        F8 = (2*R8*P8)/ (R8+P8)
        F9 = (2*R9*P9)/ (R9+P9)
        F10 = (2*R10*P10)/ (R10+P10)
        F11 = (2*R11*P11)/ (R11+P11)
        F12 = 0
        f1.write('Proper noun')
        f1.write('\n')
        f1.write('True Positive')
        f1.write('\t')
        f1.write(str(tpPN))
        f1.write('\n')
        f1.write('False Positive')
        f1.write('\t')
        f1.write(str(fpPN))
        f1.write('\n')
        f1.write('False Negative')
        f1.write('\t')
        f1.write(str(fnPN))
        f1.write('\n')
        f1.write('Precision')
        f1.write('\t')
        f1.write(str(P1))
        f1.write('\n')
        f1.write('Recall')
        f1.write('\t')
        f1.write(str(R1))
        f1.write('\n')
        f1.write('Accuracy')
        f1.write('\t')
        f1.write(str(A1))
        f1.write('\n')
        f1.write('F-Measure')
        f1.write('\t')
        f1.write(str(F1))
        f1.write('\n''\n')
        f1.write('Common noun')
        f1.write('\n')
        f1.write('True Positive')
        f1.write('\t')
        f1.write(str(tpCN))
        f1.write('\n')
        f1.write('False Positive')
        f1.write('\t')
        f1.write(str(fpCN))
        f1.write('\n')
        f1.write('False Negative')
        f1.write('\t')
        f1.write(str(fnCN))
        f1.write('\n')
        f1.write('Precision')
        f1.write('\t')
        f1.write(str(P2))
        f1.write('\n')
        f1.write('Recall')
        f1.write('\t')
        f1.write(str(R2))
        f1.write('\n')
        f1.write('Accuracy')
        f1.write('\t')
        f1.write(str(A2))
        f1.write('\n')
        f1.write('F-Measure')
        f1.write('\t')
        f1.write(str(F2))
        f1.write('\n''\n')
        f1.write('Conjunction')
        f1.write('\n')
        f1.write('True Positive')
        f1.write('\t')
        f1.write(str(tpC))
        f1.write('\n')
        f1.write('False Positive')
        f1.write('\t')
        f1.write(str(fpC))
        f1.write('\n')
        f1.write('False Negative')
        f1.write('\t')
        f1.write(str(fnC))
        f1.write('\n')
        f1.write('Precision')
        f1.write('\t')
        f1.write(str(P3))
        f1.write('\n')
        f1.write('Recall')
        f1.write('\t')
        f1.write(str(R3))
        f1.write('\n')
        f1.write('Accuracy')
        f1.write('\t')
        f1.write(str(A3))
        f1.write('\n')
        f1.write('F-Measure')
        f1.write('\t')
        f1.write(str(F3))
        f1.write('\n''\n')
        f1.write('Adjective')
        f1.write('\n')
        f1.write('True Positive')
        f1.write('\t')
        f1.write(str(tpA))
        f1.write('\n')
        f1.write('False Positive')
        f1.write('\t')
        f1.write(str(fpA))
        f1.write('\n')
        f1.write('False Negative')
        f1.write('\t')
        f1.write(str(fnA))
        f1.write('\n')
        f1.write('Precision')
        f1.write('\t')
        f1.write(str(P4))
        f1.write('\n')
        f1.write('Recall')
        f1.write('\t')
        f1.write(str(R4))
        f1.write('\n')
        f1.write('Accuracy')
        f1.write('\t')
        f1.write(str(A4))
        f1.write('\n')
        f1.write('F-Measure')
        f1.write('\t')
        f1.write(str(F4))
        f1.write('\n''\n')
        f1.write('Verb')
        f1.write('\n')
        f1.write('True Positive')
        f1.write('\t')
        f1.write(str(tpV))
        f1.write('\n')
        f1.write('False Positive')
        f1.write('\t')
        f1.write(str(fpV))
        f1.write('\n')
        f1.write('False Negative')
        f1.write('\t')
        f1.write(str(fnV))
        f1.write('\n')
        f1.write('Precision')
        f1.write('\t')
        f1.write(str(P5))
        f1.write('\n')
        f1.write('Recall')
        f1.write('\t')
        f1.write(str(R5))
        f1.write('\n')
        f1.write('Accuracy')
        f1.write('\t')
        f1.write(str(A5))
        f1.write('\n')
        f1.write('F-Measure')
        f1.write('\t')
        f1.write(str(F5))
        f1.write('\n''\n')
        f1.write('Adverb')
        f1.write('\n')
        f1.write('True Positive')
        f1.write('\t')
        f1.write(str(tpAv))
        f1.write('\n')
        f1.write('False Positive')
        f1.write('\t')
        f1.write(str(fpAv))
        f1.write('\n')
        f1.write('False Negative')
        f1.write('\t')
        f1.write(str(fnAv))
        f1.write('\n')
        f1.write('Precision')
        f1.write('\t')
        f1.write(str(P6))
        f1.write('\n')
        f1.write('Recall')
        f1.write('\t')
        f1.write(str(R6))
        f1.write('\n')
        f1.write('Accuracy')
        f1.write('\t')
        f1.write(str(A6))
        f1.write('\n')
        f1.write('F-Measure')
        f1.write('\t')
        f1.write(str(F6))
        f1.write('\n''\n')
        f1.write('Arabic Numeral')
        f1.write('\n')
        f1.write('True Positive')
        f1.write('\t')
        f1.write(str(tpAN))
        f1.write('\n')
        f1.write('False Positive')
        f1.write('\t')
        f1.write(str(fpAN))
        f1.write('\n')
        f1.write('False Negative')
        f1.write('\t')
        f1.write(str(fnAN))
        f1.write('\n')
        f1.write('Precision')
        f1.write('\t')
        f1.write(str(P7))
        f1.write('\n')
        f1.write('Recall')
        f1.write('\t')
        f1.write(str(R7))
        f1.write('\n')
        f1.write('Accuracy')
        f1.write('\t')
        f1.write(str(A7))
        f1.write('\n')
        f1.write('F-Measure')
        f1.write('\t')
        f1.write(str(F7))
        f1.write('\n''\n')
        f1.write('Pronoun')
        f1.write('\n')
        f1.write('True Positive')
        f1.write('\t')
        f1.write(str(tpP))
        f1.write('\n')
        f1.write('False Positive')
        f1.write('\t')
        f1.write(str(fpP))
        f1.write('\n')
        f1.write('False Negative')
        f1.write('\t')
        f1.write(str(fnP))
        f1.write('\n')
        f1.write('Precision')
        f1.write('\t')
        f1.write(str(P8))
        f1.write('\n')
        f1.write('Recall')
        f1.write('\t')
        f1.write(str(R8))
        f1.write('\n')
        f1.write('Accuracy')
        f1.write('\t')
        f1.write(str(A8))
        f1.write('\n')
        f1.write('F-Measure')
        f1.write('\t')
        f1.write(str(F8))
        f1.write('\n''\n')
        f1.write('Ad Position')
        f1.write('\n')
        f1.write('True Positive')
        f1.write('\t')
        f1.write(str(tpAd))
        f1.write('\n')
        f1.write('False Positive')
        f1.write('\t')
        f1.write(str(fpAd))
        f1.write('\n')
        f1.write('False Negative')
        f1.write('\t')
        f1.write(str(fnAd))
        f1.write('\n')
        f1.write('Precision')
        f1.write('\t')
        f1.write(str(P9))
        f1.write('\n')
        f1.write('Recall')
        f1.write('\t')
        f1.write(str(R9))
        f1.write('\n')
        f1.write('Accuracy')
        f1.write('\t')
        f1.write(str(A9))
        f1.write('\n')
        f1.write('F-Measure')
        f1.write('\t')
        f1.write(str(F9))
        f1.write('\n''\n')
        f1.write('Ethiopian Numeral')
        f1.write('\n')
        f1.write('True Positive')
        f1.write('\t')
        f1.write(str(tpEN))
        f1.write('\n')
        f1.write('False Positive')
        f1.write('\t')
        f1.write(str(fpEN))
        f1.write('\n')
        f1.write('False Negative')
        f1.write('\t')
        f1.write(str(fnEN))
        f1.write('\n')
        f1.write('Precision')
        f1.write('\t')
        f1.write(str(P10))
        f1.write('\n')
        f1.write('Recall')
        f1.write('\t')
        f1.write(str(R10))
        f1.write('\n')
        f1.write('Accuracy')
        f1.write('\t')
        f1.write(str(A10))
        f1.write('\n')
        f1.write('F-Measure')
        f1.write('\t')
        f1.write(str(F10))
        f1.write('\n''\n')
        f1.write('Punctuation')
        f1.write('\n')
        f1.write('True Positive')
        f1.write('\t')
        f1.write(str(tpPu))
        f1.write('\n')
        f1.write('False Positive')
        f1.write('\t')
        f1.write(str(fpPu))
        f1.write('\n')
        f1.write('False Negative')
        f1.write('\t')
        f1.write(str(fnPu))
        f1.write('\n')
        f1.write('Precision')
        f1.write('\t')
        f1.write(str(P11))
        f1.write('\n')
        f1.write('Recall')
        f1.write('\t')
        f1.write(str(R11))
        f1.write('\n')
        f1.write('Accuracy')
        f1.write('\t')
        f1.write(str(A11))
        f1.write('\n')
        f1.write('F-Measure')
        f1.write('\t')
        f1.write(str(F11))
        f1.write('\n''\n')
        f1.write('Abbrivation')
        f1.write('\n')
        f1.write('True Positive')
        f1.write('\t')
        f1.write(str(tpAb))
        f1.write('\n')
        f1.write('False Positive')
        f1.write('\t')
        f1.write(str(fpAb))
        f1.write('\n')
        f1.write('False Negative')
        f1.write('\t')
        f1.write(str(fnAb))
        f1.write('\n')
        f1.write('Precision')
        f1.write('\t')
        f1.write(str(P12))
        f1.write('\n')
        f1.write('Recall')
        f1.write('\t')
        f1.write(str(R12))
        f1.write('\n')
        f1.write('Accuracy')
        f1.write('\t')
        f1.write(str(A12))
        f1.write('\n')
        f1.write('F-Measure')
        f1.write('\t')
        f1.write(str(F12))
        f1.close()
        print ("before preprocessing!!!")
        print ("...............................................................................")
        f=codecs.open('ForUnsuposOnlyORIG.FINE.txt','r', encoding="utf-8")#opens a raw file to read
        print (" ",f.read()," ")#prints what is found in the file
        f.close()
        print ('=========================================================================')
        print ('=========================================================================')
        print ("after preprocessing)!!!")
        print ("...............................................................................")
        f=codecs.open('Computation.txt','r', encoding="utf-8")#Opens a preprocessed file to read
        print (" ",f.read()," ")#prints what is found in the file
        f.close()
ob=AMHARIC()
ob.preprocessing("ForUnsuposOnlyORIG.FINE.txt")# creation of an object for the class Amharic
