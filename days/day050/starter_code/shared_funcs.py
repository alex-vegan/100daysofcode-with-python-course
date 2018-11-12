import requests


def _pull_site(url):
    raw_site_page = requests.get(url)
    raw_site_page.raise_for_status()
    return raw_site_page
