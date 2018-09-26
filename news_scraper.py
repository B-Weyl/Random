import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.delawareonline.com'
response = requests.get("https://www.delawareonline.com/news/crime")
if response.status_code == 200:
    data = response.text
soup = BeautifulSoup(data, 'html.parser')
the_urls = []
post_titles = []
for link in soup.find_all('a', {'class': 'js-asset-link'}):
    the_urls.append(BASE_URL + link.get('href'))
the_headlines = soup.find_all('h1', {'class': 'flm-hed'})
for headline in the_headlines:
    if headline.text not in post_titles:
        post_titles.append(headline.text)
titles_and_urls = zip(post_titles, the_urls)
for title, url in titles_and_urls:
    print(f"{title}" + '\n' + f"{url}")
