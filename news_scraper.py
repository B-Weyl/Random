import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.delawareonline.com'

# code rewritten to utilize functions and main instead of just running as a
# block of code



def get_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
    return data


def parse_data(data):
    soup = BeautifulSoup(data, 'html.parser')
    post_urls, post_titles, post_ages = [], [], []
    for link in soup.find_all('a', {'class': 'gnt_m_flm_a'}):
        post_urls.append(BASE_URL + link.get('href'))
    headlines = soup.find_all('a', {'class': 'gnt_m_flm_a'})
    dates = soup.find_all('div', {'class': 'gnt_m_flm_sbt'})
    for date in dates:
        post_ages.append(' '.join(date.text.split()))
    for headline in headlines:
        if headline.text not in post_titles:
            post_titles.append(headline.text)
    return zip(post_titles, post_urls, post_ages)


def print_nice(data):
    for title, url, age in data:
        print(f"{title}" + f" {age}", '\n' + f"{url}")


def main():
    site = get_content('https://www.delawareonline.com/news/crime')
    data = parse_data(site)
    print_nice(data)


if __name__ == '__main__':
    main()


