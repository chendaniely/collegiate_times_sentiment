#
# This file does not ping the server
#

import glob

from bs4 import BeautifulSoup

sections = glob.glob('output/01-*.txt')

for section in sections:
    print('Parsing: {}'.format(section))
    section_name = section.split('-')[2].split('.')[0]
    section_link_fn = 'output/02-{}_links.txt'.format(section_name)
    f = open(section_link_fn, 'w')
    f.close()

    with open(section, 'r') as f:
        data = f.read()

    soup = BeautifulSoup(data, 'lxml')
    card_panels = soup.find_all('div', class_='card-panel panel')

    for article in card_panels:
        rel_link = article.find('a')['href']
        full_link = 'http://www.collegiatetimes.com' + rel_link + '\n'
        with open(section_link_fn, 'a') as f:
            f.write(full_link)
