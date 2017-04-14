import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.corpus import sentiwordnet as swn

import pandas as pd

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

data = pd.read_csv('./output/scraped_article_info.tsv', sep='\t').text.astype(str)
all_text = '\n\n\n\n'.join(data)

all_text_tokens = wordpunct_tokenize(all_text)
pos = nltk.pos_tag(all_text_tokens)

nv = filter(lambda x: x[1] == "NN" or x[1] == "VB", pos)
nv_df = pd.DataFrame(list(nv), columns=['word', 'pos'])

word_counts = nv_df.word.value_counts()
word_counts.to_csv('all_word_counts.csv')

words_df = nv_df.drop_duplicates()
words_df.to_csv('noun_verbs.csv')
