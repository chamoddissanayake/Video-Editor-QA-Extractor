from gensim import corpora, models, similarities, downloader, utils
import pprint
import regex as re

def topic_extractor(transcription):

    # read all content of text file
    # with open('spt1.txt') as f:
    #     lines = f.read()
    
    # preprocess each line and make a single string
    lines = ' '.join(utils.simple_preprocess(transcription))
    print(lines)
    # spt_sentences = lines.split(".")
    spt_sentences = re.compile('.').split(lines)
    print(spt_sentences)
   
    # Create a set of frequent words
    stoplist = set('so we you for a of the and to in or is'.split(' '))
    # Lowercase each document, split it by white space and filter out stopwords
    texts = [[word for word in document.split() if word not in stoplist]
            for document in spt_sentences]

    # Count word frequencies
    from collections import defaultdict
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1

    # Only keep words that appear more than once
    processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]

    dictionary = corpora.Dictionary(processed_corpus)
    corpus = [dictionary.doc2bow(text) for text in texts]
    print(corpus)

    tfidf = models.TfidfModel(corpus)

    from gensim.corpora import Dictionary
    from gensim.corpora import MmCorpus
    from gensim.models.ldamodel import LdaModel

    document = "This is some document..."
    # load id->word mapping (the dictionary)
    id2word = Dictionary.load_from_text('wiki_en_wordids.txt')
    # load corpus iterator
    mm = MmCorpus('wiki_en_tfidf.mm')
    # extract 100 LDA topics, updating once every 10,000
    lda = LdaModel(corpus=mm, id2word=id2word, num_topics=100, update_every=1, chunksize=10000, passes=1)
    # use LDA model: transform new doc to bag-of-words, then apply lda
    doc_bow = Dictionary.doc2bow(document.split())
    doc_lda = lda[doc_bow]
    # doc_lda is vector of length num_topics representing weighted presence of each topic in the doc