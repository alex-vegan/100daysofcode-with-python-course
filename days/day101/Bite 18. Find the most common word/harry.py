import os
import urllib.request
from collections import Counter
import re

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)

#stopwords_file = 'stopwords.txt'
#harry_text = 'harry.txt'

def get_harry_most_common_word():
    with open(stopwords_file) as sw_f, open(harry_text) as ht_f:
        stopwords_list = sw_f.read().strip().split('\n')
        c = Counter()
        words = re.findall(r"[\w|']+", ht_f.read().lower())
        for word in words:
            if not word in stopwords_list:
                c[word] += 1
    return c.most_common(1)[0]