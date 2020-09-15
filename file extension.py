#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:28:05 2020

@author: meera
"""

a=input("Input the filename: ")
s=a.split('.')
if(s[1]=="py"):
    print("The extension of the file is: " + "'Python'")
elif(s[1]=="java"):
    print("The extension of the file is: " + "'Java'")
elif(s[1]=="js"):
    print("The extension of the file is: " + "'Java Script'")
elif(s[1]=="mat"):
    print("The extension of the file is: " + "'Matlab'")
elif(s[1]=="txt"):
    print("The extension of the file is: " + "'Text'")
else:
    print("The extension of the file is: " + "'Other files'")
  