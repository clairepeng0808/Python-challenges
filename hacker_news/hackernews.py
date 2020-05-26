from bs4 import BeautifulSoup
import requests
from pprint import pprint


res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.find_all('a'))
# print(soup.find('a'))  # find the first occurrence of <a>
# print(soup.title)
# print(soup.find(id="score_23254587"))


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


links = soup.select('.storylink')  # '.' stands for class
subtext = soup.select('.subtext')
# print(links[0].get('href'))

pprint(create_custom_hn(links, subtext))
