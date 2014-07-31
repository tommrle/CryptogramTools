#!/usr/bin/python
from LetterPerms import CalcPerms

def FrequencyMeasurep1(phrase):
	letterFreq = []
	letterFreq = [0] * 26

	for char in phrase.lower():
		if( (ord(char) - 97) >= 0 & (ord(char) - 97) <= 25):
			letterFreq[ord(char)-97] += 1

	sortLetterFreq = sorted(letterFreq, reverse=True)
	englishFreq = ('e', 't', 'a', 'o', 'i', 'n', 'r', 'h', 'd', 'l', 'u', 'c', 'm', 'f', 'y', 'w', 'g', 'p', 'b', 'v', 'k', 'x', 'q', 'j', 'z')

	for z in range(0,25):
		letterf = sortLetterFreq.pop(0)
		q = letterFreq.index(letterf)
		letterFreq[q] = englishFreq[z]

	return letterFreq


def theFinder(phrase):
	words = phrase.split(" ")
	wordlist = []
	freq = []

	freq = FrequencyMeasurep1(phrase)

	for word in words:
		if len(word) == 3 or len(word) == 4:
			wordlist.append(word)

			

	return wordlist


phrase = "QOWKAUWXG YWPOYW DH JZKD TPFFWXUWU XKN WFQBPCWWK NK PR UWKWOG KGPOF RPO GDW MWC KAYAXG KZQQPOG GDWC QOPLAUWU"

print theFinder(phrase)