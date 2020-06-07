from bs4 import BeautifulSoup
import requests
from pprint import pprint


def request_diff_pages(pages):
    res_list = []
    for pgnum in range(1, pages+1):
        res = requests.get(f'https://news.ycombinator.com/news?p={pgnum}')
        res_list.append(res)
    return res_list


def megalink(res_list):
    megalink = []
    links = soup.select('.storylink')
    for res in res_list:
        megalink.append(res)
    return megalinkㄨㄨ


def megasubtext(res_list):
    megalink = []
    for res in res_list:
        megalink.append(res)
    return megalink


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')  # '.' stands for class
subtext = soup.select('.subtext')
pprint(create_custom_hn(links, subtext))
