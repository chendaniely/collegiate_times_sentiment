import pandas as pd
from numpy import NaN

from nltk.corpus import sentiwordnet as swn

def recode_pos(x):
    if x == 'NN':
        return('n')
    elif x == 'VB':
        return('v')
    else:
        return(NaN)

def score_word(row):
    word = row['word']
    pos = row['swn_pos']
    sent_str = '.'.join([word, pos, '01'])
    try:
        sent = swn.senti_synset(sent_str)
    except:
        return(NaN)
    return([sent.pos_score(), sent.neg_score(), sent.obj_score()])

def assign_pos_neg(score):
    if score > 0:
        return('pos')
    elif score < 0:
        return('neg')
    else:
        return('neu')

wn = pd.read_csv('noun_verbs.csv')

wn['swn_pos'] = wn.pos.apply(recode_pos)

sentiments = wn.apply(score_word, axis=1).apply(lambda x: pd.Series(x, index=['pos_s', 'neg_s', 'obj_s']))

# if score is pos, then the word is positive
# if score is negative, then word is negative
sentiments['score'] = sentiments.pos_s - sentiments.neg_s

sentiments['pos_neg'] = sentiments['score'].apply(assign_pos_neg)
sentiments.pos_neg.value_counts()

df = pd.concat([wn, sentiments], axis=1)
complete = df.dropna()

print(complete.pos_neg.value_counts())

print(pd.crosstab(complete.swn_pos, complete.pos_neg, margins=True))

complete.to_csv('output/word_sentiments.csv')
