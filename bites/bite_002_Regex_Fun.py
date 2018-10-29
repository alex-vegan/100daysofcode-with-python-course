import re

def extract_course_times():
    """Write a regular expression that returns a list of timestamps:
        ['01:47', '32:03', '41:51', '27:48', '05:02']"""
    flask_course = ('Introduction 1 Lecture 01:47'
                    'The Basics 4 Lectures 32:03'
                    'Getting Technical!  4 Lectures 41:51'
                    'Challenge 2 Lectures 27:48'
                    'Afterword 1 Lecture 05:02')
    return re.findall('Lectures? (\d\d:\d\d)', flask_course) 


def get_all_hashtags_and_links():
    """Write a regular expression that returns this list:
       ['http://pybit.es/requests-cache.html', '#python', '#APIs']"""
    tweet = ('New PyBites article: Module of the Week - Requests-cache '
             'for Repeated API Calls - http://pybit.es/requests-cache.html '
             '#python #APIs')
    regex = ('http://(?P<link>\S+)'
             '|#(?P<hashtag>\S+)')
    result = []
    match_iter = re.finditer(regex, tweet)
    for match in match_iter:
        if match.lastgroup == 'link':
            result.append('http://' + match.group(match.lastgroup))
        if match.lastgroup == 'hashtag':
            result.append('#' + match.group(match.lastgroup))
    return result
             

def match_first_paragraph():
    """Write a regular expression that returns  'pybites != greedy' """
    html = ('<p>pybites != greedy</p>'
            '<p>not the same can be said REgarding ...</p>')
    match = re.search('<p>(.*?)</p>', html)
    return match.group(1)