import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.detik.com/terpopuler')

# Beautifulsoup
bs = BeautifulSoup(url.text, 'html.parser')
result = bs.find('div', 'list-content')


def get_links():
    links = result.findAll('div', 'media__text')
    for link in links:
        print(link.find('a').get('href'))


def get_item():
    titles = result.findAll('div', 'media__text')
    for title in titles:
        print(title.find('a').text)


if __name__ == '__main__':
    get_item()
    get_links()
