# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 12:19:56 2019

@author: CEC
"""

#Condicionales

aclNum=int(input("What is teh IPv4 ACL number? "))

if aclNum>=1 and aclNum <=99:
    print("this is a standard IPv4 ACL.")
elif aclNum>=100 and aclNum<=199:
    print("this is a extended IPv4 ACL.")
else:
    print("this is not a standard or extended IPv4 ACL.")