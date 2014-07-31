#!/usr/bin/python
import sys
import enchant
import re

d = enchant.Dict("en_US")

def CalcPerms(partialword):
	#if "".join(partialword) == "".join(partialword).lower():
	#	return []
	x = -1
	t = 0
	for t in range(0,len(partialword)):
		if partialword[t] == " ":
			continue
		if partialword[t] == partialword[t].upper():
			x = t
			break

	if x == -1:
		return []

	partialword = list(partialword)
	wordlist = []

	for val in range(97,123):
		if "".join(partialword).find(chr(val)) != -1:
			continue

		if partialword[x] == partialword[x].upper():
			y = []
			y = [m.start() for m in re.finditer(partialword[x], "".join(partialword))]
			
		for t in range(0, len(y)):
			partialword[y[t]] = chr(val)
		
		checkWord = "".join(partialword)
		z = []
		z = [m.start() for m in re.finditer(" ", checkWord)]

		#print len(z)
		if len(z) == 0:
			if d.check("".join(partialword)):
				print "".join(partialword)
				wordlist.append("".join(partialword))
		else:
			addWord = True
			# print "===PREP==="
			# print checkWord
			# print z
			# print len(z)
			#print "===Checking Words==="
			for t in range(0, len(z)):
				#print "loop"
				if t == 0:
					if not (d.check(checkWord[0:z[0]])):
						#print checkWord[0:z[0]]
					 	addWord = False

					if not (d.check(checkWord[z[len(z)-1]+1:])):
						#print checkWord[z[len(z)-1]+1:]
						addWord = False

				# elif t == len(z)-1:
				# 	print "HERE"
				# 	if not (d.check(checkWord[z[t-1]+1:])):
				# 		print checkWord[z[t]+1:]
				# 		addWord = False
				else:
					if not (d.check(checkWord[z[t-1]+1:z[t]])):
						#print checkWord[z[t-1]+1:z[t]]
						addWord = False

				if not addWord:
					break

			if addWord:
				if "".join(partialword) == "".join(partialword).lower():
					wordlist.append("".join(partialword))

		wordlist.extend(CalcPerms(partialword))

	
	return wordlist

if len(sys.argv) == 1:
	print "Usage: ./CalcPerms.py 'w_ord'"
	exit()

print CalcPerms(sys.argv[1])