import re

def generate_affiliation_link(url):
    regex = re.compile(r'\/dp\/(\w+)')
    match = regex.search(url)
    return 'http://www.amazon.com/dp/{}/?tag=pyb0f-20'.format(match.groups()[0])
    