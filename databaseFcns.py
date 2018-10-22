import sqlite3
import parsers
import pandas as pd
import numpy as np


def populateDatabase(databaseName):
	
	conn = sqlite3.connect('./Presidents.db')
	c = conn.cursor()
	df = pd.read_csv('us_presidents.csv', encoding='latin1')
	
	for i in range(len(df)):
		data = df.iloc[i]
		c.execute('''INSERT INTO US_Presidents (Idx, Number, Start, End, President, Prior, Party, Vice) 
					Values (?, ?, ?, ?, ?, ?, ?, ?) ''', np.array(data, dtype=str))
					
		conn.commit()
	df_wordcounts = pd.read_csv('targetfile.csv')
	
	for i in range(len(df_wordcounts)):
	
		data = df_wordcounts.iloc[i]
		print (data)
		c.execute('''INSERT INTO Speeches (File_name, Word, Word_Count)
					VALUES (?, ?, ?) ''', np.array(data, dtype=str))
		
		conn.commit()
		
populateDatabase('Presidents.db')


# Part 2

def searchDatabase(databaseName, word):

	conn = sqlite3.connect('./Presidents.db')
	
	# This code read all the columns and rows from my db
	df_wordcounts = pd.read_sql('SELECT * FROM Speeches', conn)
	
	#
	president_counts = df_wordcounts.loc[df_wordcounts['Word'] == word]
	
	idx_max_wordCount = np.argmax(president_counts['Word_Count'])
	president_name = president_counts.loc[idx_max_wordCount]
	
	return president_name['File_name']

president_name = searchDatabase('./Presidents.db', 'the')
print (president_name)

def computeLengthByParty(databaseName):

	conn = sqlite3.connect('./Presidents.db')
	
	df_presidents = pd.read_sql('SELECT * FROM US_Presidents', conn)
	
	presidents_parties = df_presidents.loc[df_presidents['Party'] == 'Democratic' ]
	presidents_parties = df_presidents.loc[df_presidents['Party'] == 'Republican' ]
	
computeLengthByParty('./Presidents.db')
	 
   


	
	
	
	

