import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.kompas.com/')

if url.status_code == 200:
    soup = BeautifulSoup(url.content, 'html.parser')

    result = soup.find('div', {'class': 'mostWrap'})
    titles = result.find_all('h2', 'mostTitle')

    for title in titles:
        print(title.text.strip())

else:
    print("Can't Scrape")
