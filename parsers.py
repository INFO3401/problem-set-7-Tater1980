import csv
import string
from collections import Counter
from os import listdir
import os
import glob
import json
import sqlite3

# I helped my table with this problem set (Brandon, Nathan, Michael) quite a bit, 
# especially Nathan since he and I are partners for the semester project. I also read a lot
# from stackoverflow, reddit and notes from 2201.  It literally took me all weekend but I
# learned a TON.

# Problem 1

def countWordsUnstructured(filename):

	wordCounts = {}
	datafile = open(filename).read()
	data = datafile.split()
	
	for word in data:
		for mark in string.punctuation:
			word = word.replace(mark, "")
		if word in wordCounts:
			wordCounts[word] = wordCounts[word] +1
		else: wordCounts[word] = 1
	return wordCounts
	
bush1989 = countWordsUnstructured("./state-of-the-union-corpus-1989-2017/Bush_1989.txt")
print (bush1989)

# Problem 2

def generateSimpleCSV(targetfile, wordCounts):
	
	with open('1989.csv', 'w') as my_file:	
		
		writer = csv.writer(my_file)
		writer.writerow(['Word', 'Count'])
		for key, value in bush1989.items():			
			writer.writerow([key,value])	

generateSimpleCSV('1989.csv', bush1989)

# Problem 3

def countWordsMany(directory):
	dictionary = {}
	files = glob.glob(os.path.join(directory, '*.txt'))
	for fle in files:
		dictionary[fle] = countWordsUnstructured(fle)
	return (dictionary)

directoryCount = countWordsMany("./state-of-the-union-corpus-1989-2017")

# Problem #4

def generateDirectoryCSV(wordCounts, targetfile):
	with open ('targetfile.csv', 'w') as new_file:
	
		writer = csv.writer(new_file)
		writer.writerow(['Filename', 'Word', 'Count'])
		for k, v in directoryCount.items():
			for key,value in v.items():
				writer.writerow([k,key, value])

generateDirectoryCSV(directoryCount, 'targetfile.csv')

# Problem #5

def generateJSONFile(wordCounts, targetfile):
	with open('targetfile.json', 'w') as fp:
		json.dump(directoryCount, fp)

generateJSONFile(directoryCount, 'targetfile.json')
				
	
	
# Problem #6

def searchCSV(csvfile, word):
	
	maximum = 0
	with open(csvfile, 'rt') as inputfile:
		reader = csv.reader(inputfile , delimiter=',')
		for row in reader:
			if word ==row[1]:
				if maximum < int(row[2]):
					maximum = int(row[2])
					result = row[0]
		return result
		
print(searchCSV('targetfile.csv', 'President'))


def searchJSON(JSONfile, word):
	maximum = 0
	with open(JSONfile) as json_data:
		jdata = json.loads(json_data.read())
		for key in jdata:
			value = jdata[key]
			for v in value:
				if word == v:
					if maximum < int(value[v]):
						maximum = int(value[v])
						result = key
		return result
		
		
print(searchJSON('targetfile.json', 'President'))

#Database


conn = sqlite3.connect('Presidents.db')
c = conn.cursor()

def create_table():
	c.execute('''CREATE TABLE US_Presidents(Number real, Start date, End date, President varchar(50), Prior varchar(150))''')
	c.execute('''CREATE TABLE Speeches(File_name text, Word text, Word_Count real)''')
	
	conn.commit()
	conn.close()
	
create_table()

	
		






