# collegiate_times_sentiment


- Data on Friday Apr 14
- Took the articles from the front page of the following pages: new, sports, lifestyles, opinion
- tokenized and part of speach tagged words using NLTK in Python
- Filtered words based on "NN" (Noun) and "VB" (Verb)
- Performed word counts on subsetted noun/verb words
    - Need to check these counts
    - the counts were done without grouping by noun/verb
- Used SentiWordNet in nltk.corpus.reader to tag the sentiment of each word.
    - used the `01` sentiment of the word
    - collected the positive, negative, and objective score
- Calculated score based on the positive score - negative score
- Recoded pos/neg/neu word based on difference of pos and neg score
    - > 0 = positive
    - < 0 = negative
    - == 0 = neutral
