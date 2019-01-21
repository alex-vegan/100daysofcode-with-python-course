import os
import urllib.request

#LOG = os.path.join('/tmp', 'safari.logs')
PY_BOOK, OTHER_BOOK = '+', '.'
#urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)

LOG = 'safari.logs'

def create_chart():
    super_date = ''
    with open(LOG) as f:
        while True:
            first_line = f.readline()
            if not first_line:
                break
            second_line = f.readline()
            if 'sending to slack channel' in second_line:
                date = first_line[:6]
                if date != super_date:
                    print('')
                    super_date = date
                    print(date, end='')
                if 'Python' in first_line:
                    print(PY_BOOK, end='')
                else:
                    print(OTHER_BOOK, end='')
                    


                
                