import glob

import pandas as pd
import requests


def save_article_soup(df_row):
    url = df_row['url']
    url_hash = df_row['url_hash']

    print('Scraping: {}'.format(url))
    r  = requests.get(url)
    data = r.text
    fn = 'output/articles/{}'.format(url_hash)
    with open(fn, 'w') as f:
        f.write(data)
    return(True)


articles_df = pd.read_csv('output/all_article_links.txt', header=None, names=['url'])
articles_df.url.astype(str)
articles_df['url_hash'] = articles_df.apply(lambda x: hash(str(x)), axis=1)
articles_df.to_csv('article_hashes.csv')

# get list of already saved articles
# so you don't end up double scraping later
fetched_articles = glob.glob('output/articles/*')

article_hash = pd.DataFrame(fetched_articles, columns=['file_hash'])
article_hash['parsed_hash'] = article_hash.file_hash.str.split('/').str[-1]

articles_df_new = articles_df.merge(article_hash, left_on='url_hash', right_on='file_hash', how='left')

to_parse = articles_df_new.ix[pd.isnull(articles_df_new['file_hash']), :]
to_parse['file_soup'] = to_parse.apply(save_article_soup, axis=1)

print('Articles not scraped:')
print(to_parse.ix[to_parse.file_soup == False, :])
