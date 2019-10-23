# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:44:30 2019

@author: tanuj
"""
from random import randint
k = randint(1,50) #cipher key
pt='' #plain text to decrypt
plainT = input('Enter your message : ')
cipherT = '' #cipher text to encrypt

#function e(x) = (x+k) (mod 26) for encryption
for x in plainT:
    if ord(x)<97 and ord(x)>64:
        cipherT += chr((((ord(x)+k)-65)%26)+65)  #lower chars
    elif ord(x)>96 and ord(x)<123:
        cipherT += chr((((ord(x)+k)-97)%26)+97)  #upper chars
    else:
        cipherT += x
print('Cipher Text : ',cipherT)

#function e(x) = (x-k) (mod 26) for decryption
for x in cipherT:
    if ord(x)<97 and ord(x)>64:
        pt += chr((((ord(x)-k)-65)%26)+65)  #lower chars
    elif ord(x)>96 and ord(x)<123:
        pt += chr((((ord(x)-k)-97)%26)+97)  #upper chars
    else:
        pt += x
print('Plain Text : ',pt)