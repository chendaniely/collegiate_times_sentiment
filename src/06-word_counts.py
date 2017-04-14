import operator
from collections import Counter

import pandas as pd
from numpy import NaN

from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords

def word_count(tokens):
    counts = {}

    for w in tokens:
        if counts.get(w) is None:
            counts[w] = 1
        else:
            counts[w] += 1

    return(counts)

def clean_text(text):
    text = str(text)
    text = text.replace("\n", ' ')
    word_list = text.split(' ')
    return([word for word in word_list if word not in stopwords.words('english')])

data = pd.read_csv('./output/scraped_article_info.tsv', sep='\t').text
data['clean_words'] = data.text.apply(clean_text)
data['word_counts'] = data.clean_words.apply(word_count)