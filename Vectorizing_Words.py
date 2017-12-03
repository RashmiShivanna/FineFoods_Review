
# extracting review text from the dataset into a text file
import os
import csv
import nltk
from collections import OrderedDict
f = open('finefoods.txt')
lines = f.readlines()
out = open("Reviews.txt","w+")
for line in lines:
    text = []
    text = line.split(':')
    if text[0]=='review/text':
        words = str(text[1:])
        out.write(words)
out.close()
f.close()


f = open('reviews.txt')
reviews = f.read()
print "length of original reviews file"
print len(reviews)
f.close()

#tokenize the text
print "tokenizing"
import nltk
tokens = nltk.word_tokenize(reviews)
print "tokenizing finished"
print "Length of tokens is"
print len(tokens)

#Convert text into lower case
reviews_lower = [w.lower() for w in tokens]

#Remove non-alpha numeric characters
import re
pattern = re.compile('^[^a-z]+$')
def alpha_filter(w):
  # pattern to match word of non-alphabetical characters
  pattern = re.compile('^[^A-Za-z]+$')
  if (pattern.match(w)):
    return True
  else:
    return False

print "removing alpha"
reviews_alpha = [w for w in reviews_lower if not alpha_filter(w)]
print "removed alpha"
print "length of reviews after removing non-alpha characters is"
print len(reviews_alpha)


#removing stop words
print "Removing stop words"
f = open('StopWords.txt')
stopwords = f.read()
f.close()
reviews_stopped = [w for w in reviews_alpha if not w in stopwords]
print "removed stop words"
print "length of reviews after removing stopped words is"
print len(reviews_stopped)


#getting unique words from the review text
print "getting unique words"
L = {}
i = 0
for word in reviews_stopped:
    L[word] = i
    i = i+1
print "Unique words count is"
print len(L)

output =  open("Unique.csv", "w+")
writer = csv.writer(output, lineterminator='\n')
for word in L:
    writer.writerow([word])


#Counting the occurrences of each unique word in the review text
print "Counting occurrences"
count = {}
for word in reviews_stopped:
    if word in L:
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1
writer.writerow(count.values())


#Get the top 500 words
print "Getting top 500 words"
import operator
sorted_count = sorted(count.iteritems(), key=lambda (k,v): (v,k), reverse=True)
top_500 = []
output =  open("top500.csv", "w+")
writer = csv.writer(output, lineterminator='\n')
for word, count in sorted_count[:500]:
    top_500.append(word.strip())
    writer.writerow([word.strip(),count])

print top_500
top_500= sorted(top_500)
print top_500
#vectorizing the data using the top 500 words founf
print "Vectorizing the data"
i= 1
output =  open("vectors.csv", "w+")
writer = csv.writer(output, lineterminator='\n')
writer.writerow(top_500)

print "size of lines"
print len(lines)
for line in lines:
    text = []
    text = line.split(':')
    count = {}
    print "processing line "+str(i)
    if text[0]=='review/text':
        reviews = []
        reviews = nltk.word_tokenize(str(text[1:]))
        for word in top_500:
            if word in reviews and word in count:
                count[word] = count[word]+ 1
            elif word in reviews and word not in count:
                count[word] = 1
            else:
                count[word] = 0
        sorted_count = []
        for word, count in sorted(count.items()):
            sorted_count.append(count)
        writer.writerow(sorted_count)
    i = i+1
output.close()
