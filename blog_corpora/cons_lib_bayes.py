import nltk
from nltk.classify.util import apply_features
import string
import glob
import random
from nltk.corpus import stopwords
#from textblob import TextBlob


print "Importing files...."
#Import liberal data sources
cb_files=glob.glob("cb/*")
dk_files=glob.glob("dk/*")
my_files=glob.glob("my/*")

#Import conservative data sources
rs_files=glob.glob("rs/*")
rwn_files=glob.glob("rwn/*")



#For folding, create a dataset that has:
#List 1-5, each of which contains a list of tuples
#Tuples contain the text of a file and whether it is liberal or conservative
print "Adding files into dataset, bucketing for folding"
random.seed(36)
overall_data_set={1:[], 2:[], 3:[], 4:[], 5:[]}

liberal_count=0
conservative_count=0

for file in cb_files:
	f=open(file,'r')
	data_point=((f.read(),"Liberal"))
	(overall_data_set[random.randint(1,5)]).append(data_point)
	liberal_count+=1
	f.close()

for file in dk_files:
	f=open(file,'r')
	data_point=((f.read(),"Liberal"))
	(overall_data_set[random.randint(1,5)]).append(data_point)
	liberal_count+=1
	f.close()

for file in my_files:
	f=open(file,'r')
	data_point=((f.read(),"Liberal"))
	(overall_data_set[random.randint(1,5)]).append(data_point)
	liberal_count+=1
	f.close()

for file in rs_files:
	f=open(file,'r')
	data_point=((f.read(),"Conservative"))
	(overall_data_set[random.randint(1,5)]).append(data_point)
	conservative_count+=1
	f.close()

for file in rwn_files:
	f=open(file,'r')
	data_point=((f.read(),"Conservative"))
	(overall_data_set[random.randint(1,5)]).append(data_point)
	conservative_count+=1
	f.close()


print "Liberal Count", liberal_count
print "Conservative Count", conservative_count

#Create training and test data points, based on which fold we are on
print "Creating train and test data sets...."
fold_num = 5
train_data_points=[]
test_data_points=[]
test_data_points = overall_data_set[fold_num]
gen = (i for i in overall_data_set if i != fold_num)
for i in gen:
    for item in overall_data_set[i]:
        train_data_points.append(item)


def feature_extracting_function(data_point):
	features={}

	data_point = nltk.clean_html(data_point)
	#data_point = ''.join(ch for ch in data_point if ch not in set(string.punctuation)) #Strip punctuation
	
	#sentence = data_point.sentiment.polarity


	#nouns = data_point.noun_phrases


	#words = data_point.split()
	#words = [word.lower() for word in words] #convert all words to lowercase

	#word_tuples= nltk.bigrams(words)

	#word_pairs=[]
	#for word_tuple in word_tuples:
	#	if word_tuple[0] not in nltk.corpus.stopwords.words('english') and word_tuple[1] not in nltk.corpus.stopwords.words('english'):
	#		word_pair = word_tuple[0] + " " + word_tuple[1]
	#		word_pairs.append(word_pair)

	#gen = (word for word in words if word not in nltk.corpus.stopwords.words('english'))
	#for word in gen:
	#	features["contains_unigrams_(%s)" %(word)] = True

	#for word_pair in word_pairs:
	#	features["contains_bigrams_(%s)" % (word_pair)] = True

	return features



#Create proper test and training sets based on features 
print "Applying features to Training Set..."
train_set = apply_features(feature_extracting_function, train_data_points)
print "Applying features to Testing Set..."
test_set = apply_features(feature_extracting_function, test_data_points)


#Run the NLTK Naive Bayes Classifier on the training set 
print "Doing Naive Bayes...."
nb = nltk.NaiveBayesClassifier.train(train_set)

#NLTK Accuracy: Run trained model on the test set 
print "Accuracy: "+str(nltk.classify.accuracy(nb, test_set))

print "\n"+str(nb.show_most_informative_features(20))











