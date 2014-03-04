import nltk
from nltk.corpus import stopwords

import glob


#1. Import Files
print "Import Files"
liberal_files=[]
test = glob.glob("cb/*")
print type(glob.glob("cb/*"))
print file for file for file in glob.glob("cb/*")
#liberal_files.append((file for file in (glob.glob("cb/*"))))
#liberal_files.append(glob.glob("dk/*"))

conservative_files=[]
conservative_files.append(glob.glob("rs/*"))
conservative_files.append(glob.glob("rwn/*"))

print "Number in Test: ", len(test)
print "Number of Liberal Files: ", len(liberal_files)
print "Number of Conservative Files: ", len(conservative_files)
