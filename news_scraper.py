import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://www.delawareonline.com'
response = requests.get("http://www.delawareonline.com/news/crime")
if response.status_code == 200:
    data = response.text

soup = BeautifulSoup(data, 'html.parser')
the_urls = []
the_headlines = []
for link in soup.find_all('a', itemprop='url'):
    the_urls.append(BASE_URL + link.get('href'))
headlines = soup.find_all(itemprop='headline')
for _ in range(len(headlines)):
    if headlines[_].text not in the_headlines:
        the_headlines.append(headlines[_].text)
titles_and_urls = zip(the_headlines, the_urls)
for title, url in titles_and_urls:
    print(title + '\n' + url)