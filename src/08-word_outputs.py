import pandas as pd

df = pd.read_csv('output/word_sentiments.csv')

print(pd.crosstab(df.swn_pos, df.pos_neg, margins=True))

# write out 2x2 table values
# pos_n pos_v neg_n neg_v
df.ix[(df.pos_neg == 'neg') & (df.swn_pos == 'n'), 'word'].to_csv('output/words_neg_n.csv', index=False)
df.ix[(df.pos_neg == 'neg') & (df.swn_pos == 'v'), 'word'].to_csv('output/words_neg_v.csv', index=False)
df.ix[(df.pos_neg == 'pos') & (df.swn_pos == 'n'), 'word'].to_csv('output/words_pos_n.csv', index=False)
df.ix[(df.pos_neg == 'pos') & (df.swn_pos == 'v'), 'word'].to_csv('output/words_pos_v.csv', index=False)

# all nouns
df.ix[df.swn_pos == 'n', 'word'].drop_duplicates().to_csv('output/words_all_n.csv', index=False)

# all verbs
df.ix[df.swn_pos == 'v', 'word'].drop_duplicates().to_csv('output/words_all_n.csv', index=False)

all_words = pd.read_csv('all_word_counts.csv', header=None, names=['word', 'count'])
nv_words = pd.read_csv('noun_verbs.csv').drop_duplicates()

word_counts = all_words.merge(nv_words, on='word')
combined = df.merge(word_counts, on='word')

counts = combined[['word', 'swn_pos', 'pos_neg', 'count']].drop_duplicates()

counts.to_csv('output/word_counts_pos_sent.csv')
