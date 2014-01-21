
import re
word=""

while True:
    addw = raw_input("Enter a word (. ! or ? to end): ")
    word += addw   
    if re.search("\.$",addw) is not None:
        break
    else:
        pass

print "Your word is "+word