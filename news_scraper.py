import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.delawareonline.com'
response = requests.get("https://www.delawareonline.com/news/crime")
if response.status_code == 200:
    data = response.text
soup = BeautifulSoup(data, 'html.parser')
the_urls = []
post_titles = []
post_ages = []
for link in soup.find_all('a', {'class': 'js-asset-link'}):
    the_urls.append(BASE_URL + link.get('href'))
the_headlines = soup.find_all('span', {'class': 'js-asset-headline'})
the_dates = soup.find_all('p', {'class': 'flm-time-since-update'})
for date in the_dates:
    post_ages.append(' '.join(date.text.split()))
for headline in the_headlines:
    if headline.text not in post_titles:
        post_titles.append(headline.text)
# the_urls = the_urls[3:]
# very hackish because of picking up the three news stories from the top
# section need to adjust scraping the headlines to match with that..
# but for now this will have to do
titles_and_urls_and_ages = zip(post_titles, the_urls, post_ages)
for title, url, age in titles_and_urls_and_ages:
    print(f"{title} " + f" {age}" + '\n' + f"{url}")
