from flask import Flask, render_template, request, jsonify
from math import sqrt
import requests
import hashlib
import os

#Api funtions
def fact(n):
	
