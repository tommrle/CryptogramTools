#!/usr/bin/python

#export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages

import sys
import enchant

d=enchant.Dict("en_US")

def SimpleCaesar(phrase):
	print "Caesar Cipher Cracker"
	print "Input: " + phrase
	string = ""
	wordCheck = []

	for index in range(1, 26):
		for char in phrase.lower():
			if char == ' ':
				string += ' '
				continue
			val = ord(char)
			val += index
			if val > 122:
				val -= 26
			string += chr(val)
		wordCheck = string.split(' ')
		sum = 0
		for word in wordCheck:
			if d.check(word):
				sum += 1

		#print sum
		if sum > 0:
			print sum
		print string
		string = ""

def SimpleCaesarKey(phrase, cipherChar, plainChar):
	print "Caesar Cipher Cracker"
	print "Input: " + phrase
	adjust = slideCaesar(cipherChar, plainChar)
	print adjust
	string = ""
	wordCheck = []

	t = 0
	for char in phrase.lower():
		if char == ' ':
			string += " "
			continue
		if (ord(char) + adjust) > 122:
			t = -26
		else:
			t = 0
		string += chr(ord(char) + adjust + t)

	print string

def FrequencyMeasure():
	print "========"
	print "Letter Frequency Crack"

	letterFreq = []
	letterFreq = [0] * 26

	print "Letter Freq: "
	print letterFreq

	phrase = sys.argv[2]

	for char in phrase.lower():
			if( (ord(char) - 97) >= 0 & (ord(char) - 97) <= 25):
				letterFreq[ord(char)-97] += 1

	print letterFreq

	sortLetterFreq = sorted(letterFreq, reverse=True)
	print sortLetterFreq

	englishFreq = ('e', 't', 'a', 'o', 'i', 'n', 'r', 'h', 'd', 'l', 'u', 'c', 'm', 'f', 'y', 'w', 'g', 'p', 'b', 'v', 'k', 'x', 'q', 'j', 'z')

	for z in range(0,25):
		letterf = sortLetterFreq.pop(0)
		q = letterFreq.index(letterf)
		letterFreq[q] = englishFreq[z]

	print letterFreq

	for t in range(0,26):
		string = ""
		string += chr(97+t)
		string += " "
		string += str(letterFreq[t])
		print string

	string = ""
	for char in phrase.lower():
		if( (ord(char) - 97) >= 0 & (ord(char) - 97) <= 25):
			string += letterFreq[ord(char)-97]
		else:
			string += char

	print "======"
	print string

# function FrequencyCrack. 
# Take in the phrase repeated sub in different characters, 
# evaluting for english language accuracy.
def FrequencyCrack(phrase):
	letterFreq = []
	letterFreq = [0] * 26




# function isEnglish:
# Take in a phrase and look to see if there are english words
# within it.
def isEnglish(phrase):
	#first remove spaces

	sum = 0
	x = 0
	while x < len(phrase):
		if d.check(phrase[x:]):
			sum += 1
		x+=1

	return sum


def singleReplace(searchChar, replaceChar):
	print "========"
	print "Single Replace"

	phrase = sys.argv[2]
	string = ""

	for char in phrase.lower():
		if( char == searchChar):
			string += replaceChar
		else:
			string += char

	print string



def asciitable():
	for val in range(0, 26):
		print chr(val + 97) + " " + str(val)

def slideCaesar(cipherChar, plainChar):
	cipherChar = cipherChar.lower()
	plainChar = plainChar.lower()
	adjust = ord(plainChar) - ord(cipherChar)

	print "Simple Caesar Slide"
	t = 0
	for val in range(0, 26):
		if (val + 97 + adjust) > 122:
			t = -26
		else:
			t = 0
		print chr(val + 97) + " " + chr(val + 97 + adjust + t)

	return adjust



#TEST CODE
# print "Test isEnglish()"
# print isEnglish("afternoon")
# exit()
#END TEST CODE

if(len(sys.argv) == 1):
	print "Invalid Arugments."
	print "CaesarCrack arg (-a -f -c -s -h) <input>"
	exit()

opts = sys.argv[1]
if(opts == "-h"):
	print "== HELP =="
	print "-a   ASCII TABLE. Print the lower case alphabet ascii table"
	print "-f 'text'   Frequency Measure. Takes a phrase and attempts to crack by measuring the frequency of the letters and comparing to english alphabet"
	print "-s  'text' 'searchChar' 'replaceChar'	Single Replace. Takes text and replaces all letters of one value with another"
	print "-c 'text'	Simple Caesar crack. Evaluates all possible simple caesar possibilities"
	print "-t 'cipherChar' 'plainChar'	Simple caesar translation"

if opts == "-t":
	slideCaesar(sys.argv[2], sys.argv[3])

if(opts == "-a"):
	asciitable()

if(opts == "-f"):
	FrequencyMeasure()

if(opts == "-c"):
	if len(sys.argv) == 3:
		SimpleCaesar(sys.argv[2])
	elif len(sys.argv) == 5:
		SimpleCaesarKey(sys.argv[2], sys.argv[3], sys.argv[4])

if(opts == "-s"):
	if(len(sys.argv) != 5):
		print "Error: Invalid Arguments"
		print "Format: -s 'text' 'searchChar' 'replaceChar'"
		exit()

	singleReplace(sys.argv[3], sys.argv[4])
