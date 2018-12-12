import os
import re
from collections import Counter
import urllib.request

# prep
TAG_HTML = re.compile(r'<category>([^<]+)</category>')

tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)

#tempfile = 'tempfile.xml'

with open(tempfile) as f:
    content = f.read().lower()
    #print(content)

# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    match = TAG_HTML.findall(content)
    c = Counter(match)
    return c.most_common(n)