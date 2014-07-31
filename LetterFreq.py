#!/usr/bin/python
import sys

print "Letter Frequency Generator"
print "Input: " + sys.argv[1]

index = 0
freq = []

while index < 26:
	freq.insert(index, 0)
	index += 1

word = sys.argv[1]

for char in word.lower():
	print ord(char) - 97
	freq[(ord(char) - 97)] += 1

print freq

