import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
res = requests.get(url, params=params, headers=headers)

# BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')
soup = soup.find('nav', 'css-jbuxu0 ecydgvn0')
pages = soup.find_all('a')
for page in pages:
    print(page.text)
