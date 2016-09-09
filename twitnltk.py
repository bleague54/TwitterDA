
from pprint import pprint
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
import json
from nltk.corpus import stopwords
import string


file = "AtlantaDream052916.out"
tknzr = TweetTokenizer()
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['RT', 'rt', 'via', 'VIA']
linecnt = 0

with open(file, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        if linecnt < 1:
            print("TWEET TEXT FOR TWEET NUMBER: ", linecnt)
            #print(json.dumps(tweet, indent=4))
            pprint(tweet['text'])
        terms_all = [term for term in tknzr.tokenize(tweet['text']) if term not in stop]
        count_all.update(terms_all)
        linecnt += 1
    print('MOST COMMON WORDS in FILE: ', file)
    print(count_all.most_common(5))


# TEST TWEET
#tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'

#print(word_tokenize(tweet))

#print(punctuation)
#print(stop)