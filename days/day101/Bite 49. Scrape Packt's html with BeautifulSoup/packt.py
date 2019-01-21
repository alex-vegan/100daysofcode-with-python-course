from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

CONTENT = requests.get('http://bit.ly/2EN2Ntv').text
#CONTENT = 'pcc_packt-free.txt'

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')
    title = soup.find('div', class_="dotd-title").h2.text.strip()
    description = soup.find('div', class_="dotd-main-book-summary float-left").find_all('div')[2].text.strip()
    image = soup.find('div', class_="dotd-main-book-image float-left").a.\
            noscript.find('img', class_="bookimage imagecache imagecache-dotd_main_image")['src']
    link = soup.find('div', class_="dotd-main-book-image float-left").find('a')['href']
    return Book(title=title, description=description, image=image, link=link)


if __name__ == "__main__":
    print(get_book())
