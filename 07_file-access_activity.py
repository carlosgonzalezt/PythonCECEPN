# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:43:01 2019

@author: CEC
"""

file=open("devices.txt","a")

while True:
    newitem=input("Ingrese un nuevo item: ")
    
    if newitem=="exit":
        print("All done!")
        break
    else:
        file.write(newitem+"\n")

file.close()        