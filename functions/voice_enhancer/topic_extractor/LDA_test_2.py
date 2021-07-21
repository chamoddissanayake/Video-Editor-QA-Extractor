# pip install pyldavis spacy seaborn

import pandas as pd
import numpy as np
import re
import string

import spacy

from gensim import corpora

# libraries for visualization
import pyLDAvis
import pyLDAvis.gensim_models as gm
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline


# get data from the transcription source
# review_data = pd.read_csv("spt2.txt", sep=" ")
f = open("spt2.txt", "r+")
review_data = f.read().split(' ')
# print(f'review_data::::::::: \n {review_data}')
# exit()


# print('Unique Products')
# print(len(review_data.groupby('ProductId')))
# print('Unique Users')
# print(len(review_data.groupby('UserId')))

# a method to clean the text in the transcription
def clean_text(text):
    delete_dict = {sp_character: '' for sp_character in string.punctuation}
    delete_dict[' '] = ' '
    table = str.maketrans(delete_dict)
    # text1 = text.translate(table)
    # print('cleaned:'+text1)
    textArr = text.split()
    text2 = ' '.join([w for w in textArr if (not w.isdigit() and (not w.isdigit() and len(w) > 3))])
    return text2.lower()



import nltk

nltk.download('stopwords')  # run this one time

# review_data.dropna(axis=0, how='any', inplace=True)
# review_data['Text'] = review_data['Text'].apply(clean_text)
# review_data = clean_text(review_data)
# print(review_data)

review_data['Num_words_text'] = review_data['Text'].apply(lambda x: len(str(x).split()))

print('-------Dataset --------')
print(review_data['Score'].value_counts())
print(len(review_data))
print('-------------------------')
max_review_data_sentence_length = review_data['Num_words_text'].max()

mask = (review_data['Num_words_text'] < 100) & (review_data['Num_words_text'] >= 20)
df_short_reviews = review_data[mask]
df_sampled = df_short_reviews.groupby('Score').apply(lambda x: x.sample(n=20000)).reset_index(drop=True)

print('No of Short reviews')
print(len(df_short_reviews))

# all_sentences = train_data['text'].tolist() + test_data['text'].tolist()

from nltk.corpus import stopwords

stop_words = stopwords.words('english')


# function to remove stopwords
def remove_stopwords(text):
    textArr = text.split(' ')
    rem_text = " ".join([i for i in textArr if i not in stop_words])
    return rem_text


# remove stopwords from the text
df_sampled['Text'] = df_sampled['Text'].apply(remove_stopwords)

nlp = spacy.load('en_core_web_md', disable=['parser', 'ner'])


def lemmatization(texts, allowed_postags=['NOUN', 'ADJ']):
    output = []
    for sent in texts:
        doc = nlp(sent)
        output.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return output


text_list = df_sampled['Text'].tolist()
print(text_list[1])
tokenized_reviews = lemmatization(text_list)
print(tokenized_reviews[1])

dictionary = corpora.Dictionary(tokenized_reviews)
doc_term_matrix = [dictionary.doc2bow(rev) for rev in tokenized_reviews]

# Creating the object for LDA model using gensim library
LDA = gm.models.ldamodel.LdaModel

# Build LDA model
lda_model = LDA(corpus=doc_term_matrix, id2word=dictionary, num_topics=10, random_state=100,
                chunksize=1000, passes=50, iterations=100)

lda_model.print_topics()

# Visualize the topics
# https://github.com/bmabey/pyLDAvis
# https://speakerdeck.com/bmabey/visualizing-topic-models
pyLDAvis.enable_notebook()
vis = pyLDAvis.gensim.prepare(lda_model, doc_term_matrix, dictionary)
vis

print('\nPerplexity: ', lda_model.log_perplexity(doc_term_matrix,
                                                 total_docs=10000))  # a measure of how good the model is. lower the better.

# Compute Coherence Score
from gensim.models.coherencemodel import CoherenceModel

coherence_model_lda = CoherenceModel(model=lda_model, texts=tokenized_reviews, dictionary=dictionary, coherence='c_v')
coherence_lda = coherence_model_lda.get_coherence()
print('\nCoherence Score: ', coherence_lda)


def compute_coherence_values(dictionary, corpus, texts, limit, start=2, step=3):
    """
    Compute c_v coherence for various number of topics

    Parameters:
    ----------
    dictionary : Gensim dictionary
    corpus : Gensim corpus
    texts : List of input texts
    limit : Max num of topics

    Returns:
    -------
    model_list : List of LDA topic models
    coherence_values : Coherence values corresponding to the LDA model with respective number of topics
    """
    coherence_values = []
    model_list = []
    for num_topics in range(start, limit, step):
        model = gensim.models.ldamodel.LdaModel(corpus=corpus, num_topics=num_topics, id2word=dictionary)
        model_list.append(model)
        coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherencemodel.get_coherence())

    return model_list, coherence_values


model_list, coherence_values = compute_coherence_values(dictionary=dictionary, corpus=doc_term_matrix,
                                                        texts=tokenized_reviews, start=2, limit=50, step=1)

# Show graph
limit = 50;
start = 2;
step = 1;
x = range(start, limit, step)
plt.plot(x, coherence_values)
plt.xlabel("Num Topics")
plt.ylabel("Coherence score")
plt.legend(("coherence_values"), loc='best')
plt.show()  # Print the coherence scores

# Print the coherence scores
for m, cv in zip(x, coherence_values):
    print("Num Topics =", m, " has Coherence Value of", round(cv, 4))

# Select the model and print the topics
optimal_model = model_list[7]
model_topics = optimal_model.show_topics(formatted=False)
optimal_model.print_topics(num_words=10)

# Visualize the topics
pyLDAvis.enable_notebook()
vis = pyLDAvis.gensim.prepare(optimal_model, doc_term_matrix, dictionary)
vis
