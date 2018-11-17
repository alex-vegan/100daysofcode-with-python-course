#!python3

import requests
import feedparser
from pprint import pprint as pp
import click

url_list = ['http://feeds.reuters.com/reuters/technologyNews',
            'http://rss.cnn.com/rss/edition_technology.rss',
            'http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml']

xml_file_list = ['rss_reuters.xml', 'rss_cnn.xml', 'rss_nytimes.xml']


def make_xml_file(url, filename):
    resp = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(resp.content)
    return None


def parse_xml_file(filename, top=5, url=False):
    feed = feedparser.parse(filename)
    for e in feed.entries[:top]:
        if url:
            print(f'{e.published:33} - {e.title}\n{e.link}')
        else:
            print(f'{e.published:33} - {e.title}')
    return None


@click.command()
@click.argument('filenames', default='all', type=click.Choice(xml_file_list + ['all']))
@click.option('--top', '-t', default=5, show_default=True, type=int, help='print number of lines')
@click.option('--url/--no-url', '-u', default=False, show_default=True, help='show or hide url')
def do_magic(filenames, top, url):
    """simple programm for feedparsing of some rss-channels"""
    if filenames == 'all':
        filenames = xml_file_list
    if isinstance(filenames, str):
        filenames = [filenames]
    for filename in filenames:
        parse_xml_file(filename, top, url)
    return None


if __name__ == "__main__":
    for idx, url in enumerate(url_list):
        make_xml_file(url, xml_file_list[idx])
    do_magic()
