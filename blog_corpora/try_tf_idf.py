import nltk
from nltk.tokenize import *
from nltk.corpus import stopwords
from nltk import bigrams
from nltk.probability import FreqDist

import string
import glob


#1. Import Files
print "Import Files"
liberal_files=[]
for file in glob.glob("cb/*"):
	liberal_files.append(file)
for file in glob.glob("dk/*"):
	liberal_files.append(file)

conservative_files=[]
for file in glob.glob("rs/*"):
	conservative_files.append(file)
for file in glob.glob("rwn/*"):
	conservative_files.append(file)

print "Number of Liberal Files: ", len(liberal_files)
print "Number of Conservative Files: ", len(conservative_files)


#2. Per document: calculate frequency of stopwords
def calc_freq(file):
	stopwords = nltk.corpus.stopwords.words('english')
	stopwords.extend(["metaenddot", "metanumberref", "metaendquestion, metanumberrefs"])

	f = open(file,'r')
	raw = nltk.clean_html(f.read())
	raw = ''.join(ch for ch in raw if ch not in set(string.punctuation))
	tokens = [token.lower() for token in raw.split() if token not in stopwords] #generates a list of tokens
	
	fdist=FreqDist(tokens)


#3. Create a table where you a row for each file, and words for each column
for file in liberal_files:
	freq_dist = calc_freq(file)
	top_words = freq_dist.keys()[:50]
	for top_word in top_words:
		frequency = freq_dist(top_word)
	















