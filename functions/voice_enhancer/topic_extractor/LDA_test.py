
import re
from wordcloud import WordCloud
import gensim
from gensim.utils import simple_preprocess
import nltk
import gensim.corpora as corpora
from pprint import pprint

import pyLDAvis.gensim_models
import pickle
import pyLDAvis
import os
import webbrowser
from utils import  constants
from random import randint

nltk.download('stopwords')
from nltk.corpus import stopwords


# get data from the transcription source
# Loading data
def load_data(path):
    # review_data = pd.read_csv("spt2.txt", sep=" ")
    print("ppath: "+path)
    f = open(path, "r+")
    transcribed_data = f.read()
    # print(f'transcribed_data::: \n {transcribed_data}')

    print(f'length of transcribed_data {len(transcribed_data)}')
    return transcribed_data


'''first analyze using a wordcloud'''


def analyze_text(data):
    data = data.split(' ')
    # Data cleaning
    data = list(map(lambda x: re.sub('[,\.!?]', '', x), data))
    data = list(map(lambda x: x.lower(), data))
    # print(f'preprocessed::: \n {transcribed_data}')

    transcribed_data_as_string = ''
    for word in data:
        transcribed_data_as_string += word + ','

    wordcloud = WordCloud(background_color="white", max_words=10000, contour_width=3, contour_color='steelblue')
    wordcloud.generate(transcribed_data_as_string)
    wordcloud.scale = 3
    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


# Exploratory analysis
# analyze_text(transcribed_data)

# Preparing data for LDA analysis
def prepare_data_for_lda_analysis(transcribed_data):
    stop_words = stopwords.words('english')

    def sent_to_words(sentences):
        for sentence in sentences:
            # deacc=True removes punctuations
            yield (gensim.utils.simple_preprocess(str(sentence), deacc=True))

    def remove_stopwords(texts):
        return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

    # make sentences form transcribed data
    transcribed_data_as_sentences = re.split('([.?\s!]\s)|^(\b\w)', transcribed_data)
    transcribed_data_as_sentences = list(
        filter(lambda x: x != '. ' and x != '? ' and x != '! ' and x != None, transcribed_data_as_sentences))
    for sentence in transcribed_data_as_sentences:
        print(f'sentence: {sentence}')

    data_words = list(sent_to_words(transcribed_data_as_sentences))

    # remove stop words
    data_words = remove_stopwords(data_words)
    return data_words


# LDA model training ##################
def train_lda_model(corpus, lda_model):
    print("corpus:" + str(len(corpus)))
    # View
    # print(corpus)
    # print(corpus[:1][0][:100])

    print(f'lda_model.num_topics = {lda_model.num_topics}')
    # Print the Keyword in the 10 topics
    pprint(lda_model.print_topics())
    doc_lda = lda_model[corpus]
    print(doc_lda)
    return doc_lda


# Analyzing LDA model results ##################
def analyze_lda_model_results(lda_model, corpus, id2word, num_topics):
    rand=str(randint(0, 10000))
    # Visualize the topics
    # pyLDAvis.enable_notebook()
    current_dir = os.path.abspath(os.curdir)
    LDAvis_data_filepath = current_dir + '/tempStorage/voiceEnhancerTranscriptions/html/ldavis_prepared_'+rand+'_' + str(num_topics)
    print(f'LDAvis_data_filepath: {LDAvis_data_filepath}')
    print(f'os.path: {os.path}')
    # # this is a bit time consuming - make the if statement True
    # # if you want to execute visualization prep yourself
    if 1 == 1:
        LDAvis_prepared = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word)
        with open(LDAvis_data_filepath, 'wb') as f:
            pickle.dump(LDAvis_prepared, f)
    # load the pre-prepared pyLDAvis data from disk
    with open(LDAvis_data_filepath, 'rb') as f:
        LDAvis_prepared = pickle.load(f)
    print(f' str(num_topics) "{ str(num_topics) }')
    pyLDAvis.save_html(LDAvis_prepared, current_dir + '/tempStorage/voiceEnhancerTranscriptions/html/ldavis_prepared_'  + rand+'_' + str(num_topics) + '.html')
    LDAvis_prepared
    print('Done!. analyze_lda_model_results saved in ./results ')
    webbrowser.open(current_dir + '/tempStorage/voiceEnhancerTranscriptions/html/ldavis_prepared_' +rand+'_' + str(num_topics) + '.html', new=1)


def run_lda_topic_extraction(path):
    preprocessed_data_words = prepare_data_for_lda_analysis(
        load_data(
            path
        )
    )
    print(preprocessed_data_words)

    # Create Dictionary
    id2word = corpora.Dictionary(preprocessed_data_words)
    lda_model = ''
    # Create Corpus
    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in preprocessed_data_words]

    # number of topics
    num_topics = 30

    # Build LDA model
    lda_model = gensim.models.LdaModel(corpus=corpus,
                                       id2word=id2word,
                                       num_topics=num_topics)

    doc_lda = train_lda_model(corpus, lda_model)

    import time
    time.sleep(1)

    analyze_lda_model_results(lda_model, corpus, id2word, num_topics)

# run_lda_topic_extraction()
