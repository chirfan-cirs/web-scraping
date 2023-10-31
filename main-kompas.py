import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.kompas.com/')

if url.status_code == 200:
    soup = BeautifulSoup(url.content, 'html.parser')

    result = soup.find('div', {'class': 'mostWrap'})
    titles = result.find_all('h2', 'mostTitle')
    links = result.find_all('div', 'mostItem')

    for title in titles:
        print(title.text.strip())
    for link in links:
        try:  # Using Try Except to get the link, because not all of them have the 'a' tag and for
            # anticipation if there is a missing some tag ('a' for example)
            print(link.find('a').get('href'))
        except Exception:
            pass

else:
    print("Can't Scrape")
