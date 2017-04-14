import requests

from bs4 import BeautifulSoup

sections = ['http://www.collegiatetimes.com/news/',
         'http://www.collegiatetimes.com/sports/',
         'http://www.collegiatetimes.com/lifestyles/',
         'http://www.collegiatetimes.com/opinion/']

for section in sections:
    section_name = section.split('/')[-2]
    section_fn = 'output/01-section-{}.txt'.format(section_name)
    r  = requests.get(section)
    data = r.text
    with open(section_fn, 'w') as f:
        f.write(data)
    print('{} created'.format(section_fn))
