import cProfile

profiler = cProfile.Profile()
profiler.disable()

import bs4
import shared_funcs

url = 'https://www.nytimes.com/section/technology/personaltech'


def scrape(site):
    header_list = []
    soup = bs4.BeautifulSoup(site.text, 'lxml')
    html_header_list = soup.select('.headline')
    for html_header in html_header_list:
        header_list.append(html_header.getText())
    return list(set(header_list))


def main():
    profiler.enable()
    site = shared_funcs._pull_site(url)
    headers = scrape(site)
    with open('itdict.txt') as file_dict:
        it_dict = file_dict.read().strip().lower().split()
        profiler.disable()
        for header in headers:
            for header_word in header.lower().split():
                if header_word in it_dict:
                    print(header.strip())
                    break
    return None


if __name__ == '__main__':
    main()
    profiler.print_stats(sort='cumtime')
