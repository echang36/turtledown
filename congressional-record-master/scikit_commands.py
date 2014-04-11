from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report


#Load files
categories=['liberal','conservative']
train_files=load_files('./congress_data_even/Train/', categories=categories, charset='latin-1')
test_files=load_files('./congress_data_even/Test/', categories=categories, charset='latin-1')

# Turn the text documents into vectors of word frequencies
vectorizer = TfidfVectorizer(min_df=2, ngram_range=(1, 3), token_pattern=ur'(?u)\b[\w-]+\b')
X_train = vectorizer.fit_transform(train_files.data)
y_train = train_files.target

# Fit a classifier on the training set
classifier = MultinomialNB(alpha=1)
classifier.fit(X_train, y_train)
print("Training score: {0:.1f}%".format(
    classifier.score(X_train, y_train) * 100))

# Evaluate the classifier on the testing set
X_test = vectorizer.transform(test_files.data)
y_test = test_files.target
print("Testing score: {0:.1f}%".format(
    classifier.score(X_test, y_test) * 100))
#print classifier.score(X_train, y_train)


################################################################################################################

import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

pipeline = Pipeline((
    ('vec', TfidfVectorizer(min_df=1, max_df=0.8, use_idf=True)),
    ('clf', MultinomialNB(alpha=.001)),
))


predicted=classifier.predict(X_test)
actual=test_files.target
print predicted

print(classification_report(actual, predicted,
                            target_names=test_files.target_names))


################################################################################################################

from sklearn.grid_search import GridSearchCV

parameters = {
    'vec__min_df': [0.5, 0.75, 1.0],
    'vec__max_df': [0.8, 1.0],
    'tfidf__use_idf':(True, False),
    'vec__ngram_range': [(1, 1), (1, 2)],
    'vec__use_idf': [True, False],
}

gs = GridSearchCV(pipeline, parameters, verbose=2, refit=False)
_ = gs.fit(train_files.data, train_files.target)

print gs.best_score_
print gs.best_params_

_ = pipeline.fit(train_files.data, train_files.target)


vec_name, vec = pipeline.steps[0]
clf_name, clf = pipeline.steps[1]

feature_names = vec.get_feature_names()
target_names = train_files.target_names

feature_weights = clf.coef_

feature_weights.shape

def display_important_features(feature_names, target_names, weights, n_top=30):
    for i, target_name in enumerate(target_names):
        print("Class: " + target_name)
        print("")
        
        sorted_features_indices = weights[i].argsort()[::-1]
        
        most_important = sorted_features_indices[:n_top]
        print(", ".join("{0}: {1:.4f}".format(feature_names[j], weights[i, j])
                        for j in most_important))
        print("...")
        
        least_important = sorted_features_indices[-n_top:]
        print(", ".join("{0}: {1:.4f}".format(feature_names[j], weights[i, j])
                        for j in least_important))
        print("")
        
display_important_features(feature_names, target_names, feature_weights)