import httpx
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""It seems that indeed.com can't be scraped anymore and needs a custom API or they have a new policy about their 
API, so I'll forget about it for now"""

# Selenium
driver = webdriver.Chrome()
driver.get('https://id.indeed.com/jobs?q=python&l=Jakarta&from=mobRdr&utm_source=%2Fm%2F&utm_medium=redir'
           '&utm_campaign=dt&vjk=ee57d86c9b488ae8')
page_source = driver.page_source

# Requests
url = 'https://id.indeed.com/jobs?'
params = {
    'q': 'python',
    'l': 'Jakarta',
    'vjk': 'ee57d86c9b488ae8'
}
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, '
                         'like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36'}
res = requests.get(url)
print(res.status_code)

# BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')
soup = soup.find('div', 'mosaic-jobResults')
pages = soup.find_all('a')
print(soup.prettify())

def get_item():
    bsoup = BeautifulSoup(page_source, 'html.parser')
    bsoup = bsoup.find('div', 'mosaic-zone')
    items = bsoup.find_all('a')
    for item in items:
        print(item.text)


if __name__ == '__main__':
    try:
        get_item()
    except:
        pass
