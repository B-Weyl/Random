from venv import create
import requests
from bs4 import BeautifulSoup
from prettytable.colortable import ColorTable, Themes
from prettytable import PrettyTable
import html
import rich

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
    # subarticles on crime page
    for link in soup.find_all('a', {'class': 'gnt_m_flm_a'}):
        if link.get('href') != None:
            post_urls.append(BASE_URL + link.get('href'))
    headlines = soup.find_all('a', {'class': 'gnt_m_flm_a'})
    dates = soup.find_all('div', {'class': 'gnt_m_flm_sbt'})

    # the main headline on the crime page
    main_headline = ""
    for main_article in soup.find_all('a', {'class': 'gnt_m_he'}):
        # print(main_article.text)
        if main_article.text != None:
            main_headline = main_article.text
    
    main_date = soup.find_all('div', {'class:' 'gnt_sbt'})
    main_url = ""
    for main_link in soup.find_all('a', {'class': 'gnt_m_he'}):
        if main_link.get('href') != None:
            main_url = BASE_URL + main_link.get('href')
    


    for date in dates:
        post_ages.append(' '.join(date.text.split()))
    for headline in headlines:
        if headline.text != "" and headline.text not in post_titles:
            post_titles.append(headline.text)
    post_titles.insert(0, main_headline)
    post_ages.insert(0, main_date)
    post_urls.insert(0, main_url)
    return zip(post_titles, post_urls, post_ages)


def print_nice(data):
    for title, url, age in data:
        print(f"{title}" + f" {age}", '\n' + f"{url}")

def link(uri, label=None):
    if label is None: 
        label = uri
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)

def create_table(data):
    x = ColorTable(theme=Themes.DEFAULT)
    # headers = ("Headline", "URL")
    # t = PrettyTable(headers)
    x.field_names = ["Headline", "URL" ]
    for title, url, _age in data:
        # x.add_row([title, "[link=" + url + "]Link Here[/link]!"])
        x.add_row([title, link(url, 'Link for Story')])
    x.align = "c"
    return x

def main():
    site = get_content('https://www.delawareonline.com/news/crime')
    data = parse_data(site)
    t = create_table(data)
    print(t)


if __name__ == '__main__':
    main()


