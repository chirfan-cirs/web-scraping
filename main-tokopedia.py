import requests
from bs4 import BeautifulSoup

"""
Scraping Data from Tokopedia.com
"""

url = 'https://www.tokopedia.com/search?st=product&q=bangku%20gaming'
params = {
    'st': 'product',
    'q': 'bangku gaming',
}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/118.0.0.0 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'en-US,en;q=0.9',
           'Referer': 'https://www.tokopedia.com/search?',
           'Upgrade-Insecure-Requests': '1',
           'TE': 'Trailers',}

respons = requests.get(url, headers=headers)

if respons.status_code == 200:
    print(respons.status_code)
else:
    print("Request Failed : ", respons.status_code)

soup = BeautifulSoup(respons.content, 'html.parser')
items = soup.findAll('div', 'css-1asz3by')


# BeautifulSoup
def get_items():
    i = 0
    for item in items:
        name = item.find('div', 'prd_link-product-name')
        print(name.text)


def get_price():
    # soup = BeautifulSoup(respons.content, 'html.parser')
    # items = soup.findAll('div', 'css-llwpbs')
    # items = soup.findAll("div", attrs={"data-testid": "divSRPContentProducts"})
    i = 0
    for item in items:
        price = item.find('div', 'prd_link-product-price')
        print(price.text)


if __name__ == '__main__':
    get_items()
    get_price()

