from flask import Flask, render_template, request, jsonify
from math import sqrt
import requests
import hashlib
import os

#Api funtions
def fact(n):
	
#I don't know what to put for the def
#this is for checking prime numbers
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")
