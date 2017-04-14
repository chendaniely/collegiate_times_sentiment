import glob

from bs4 import BeautifulSoup
import pandas as pd
from numpy import NaN

from tqdm import tqdm

def get_section(soup):
    section = soup.\
        find('div', class_='heading card').\
        find('div', class_='block-title-inner').\
        find('a').text.strip().lower()
    return(section)

def get_title(soup):
    title = soup.\
        find('h1', {'itemprop': 'headline'}).text.strip().lower()
    return(title)

def get_text(soup):
    try:
        text_p = soup.find('div', {'itemprop': 'articleBody'}).\
            find_all('p')
        text = [p.text for p in text_p]
        
        text = '\n\n'.join(text)
    except AttributeError:
        return(NaN)
    return(text)

articles = glob.glob('output/articles/*')
print('Number of articles: {}'.format(len(articles)))

data = pd.DataFrame(columns=['section', 'title', 'text'])

for i, page in tqdm(enumerate(articles), total=len(articles)):
    # print(page)
    with open(page, 'r') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
    section = get_section(soup)
    title = get_title(soup)
    text = get_text(soup)
    article_df = pd.DataFrame({'section': section, 'title': title, 'text': text}, index = [i])
    data = pd.concat([data, article_df], axis=0)

data.to_csv('output/scraped_article_info.tsv', sep='\t')
