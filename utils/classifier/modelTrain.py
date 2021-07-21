import os
import pickle

import nltk
from xml.dom import minidom


def fileCheckExistSavedData():
    status_lecturer_student_classifier_1 = os.path.isfile(
        os.path.abspath(os.curdir) + "/tempStorage/trainedData/lecturer_student_classifier_1.pickle")
    status_lecturer_student_classifier_2 = os.path.isfile(
        os.path.abspath(os.curdir) + "/tempStorage/trainedData/lecturer_student_classifier_2.pickle")

    status_domain_related_or_not_classifier_1 = os.path.isfile(
        os.path.abspath(os.curdir) + "/tempStorage/trainedData/domain_related_or_not_classifier_1.pickle")
    status_domain_related_or_not_classifier_2 = os.path.isfile(
        os.path.abspath(os.curdir) + "/tempStorage/trainedData/domain_related_or_not_classifier_2.pickle")

    status_answer_give_or_not_classifier_1 = os.path.isfile(
        os.path.abspath(os.curdir) + "/tempStorage/trainedData/answer_give_or_not_classifier_1.pickle")
    status_answer_give_or_not_classifier_2 = os.path.isfile(
        os.path.abspath(os.curdir) + "/tempStorage/trainedData/answer_give_or_not_classifier_2.pickle")

    if status_lecturer_student_classifier_1 == False or status_lecturer_student_classifier_2 == False:
        train_lecturer_student_classifier(status_lecturer_student_classifier_1,status_lecturer_student_classifier_2 )


    if status_domain_related_or_not_classifier_1 == False or status_domain_related_or_not_classifier_2 == False:
        train_domain_related_or_not_classifier(status_domain_related_or_not_classifier_1,status_domain_related_or_not_classifier_2 )


    if status_answer_give_or_not_classifier_1 == False or status_answer_give_or_not_classifier_2 == False:
        train_answer_give_or_not_classifier(status_answer_give_or_not_classifier_1,status_answer_give_or_not_classifier_2 )


def train_lecturer_student_classifier(status_lecturer_student_classifier_1,status_lecturer_student_classifier_2):

    mydoc = minidom.parse('utils/data/custom-lecturer-student.xml')

    lecturerposts = mydoc.getElementsByTagName('Post');
    posts = nltk.corpus.nps_chat.xml_posts()[:10000]

    def dialogue_act_features(post):
        features = {}
        for word in nltk.word_tokenize(post):
            features['contains({})'.format(word.lower())] = True
        return features

    featuresets = [(dialogue_act_features(post.text), post.get('class')) for post in posts]
    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    if status_lecturer_student_classifier_1==False:
        f = open('tempStorage/trainedData/lecturer_student_classifier_1.pickle', 'wb')
        pickle.dump(classifier, f)
        f.close()


    featuresets2 = [(dialogue_act_features(dp.firstChild.data), dp.attributes['class'].value) for dp in lecturerposts]
    size2 = int(len(featuresets2) * 0.1)
    train_set2, test_set2 = featuresets2[size2:], featuresets2[:size2]
    classifier2 = nltk.NaiveBayesClassifier.train(train_set2)

    if status_lecturer_student_classifier_2==False:
        f = open('tempStorage/trainedData/lecturer_student_classifier_2.pickle', 'wb')
        pickle.dump(classifier2, f)
        f.close()


def train_domain_related_or_not_classifier(status_domain_related_or_not_classifier_1,status_domain_related_or_not_classifier_2 ):
    mydoc = minidom.parse('utils/data/question-classification.xml')

    domainposts = mydoc.getElementsByTagName('Post');
    posts = nltk.corpus.nps_chat.xml_posts()[:10000]

    def dialogue_act_features(post):
        features = {}
        for word in nltk.word_tokenize(post):
            features['contains({})'.format(word.lower())] = True
        return features

    featuresets = [(dialogue_act_features(post.text), post.get('class')) for post in posts]
    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    if status_domain_related_or_not_classifier_1==False:
        f = open('tempStorage/trainedData/domain_related_or_not_classifier_1.pickle', 'wb')
        pickle.dump(classifier, f)
        f.close()


    featuresets2 = [(dialogue_act_features(dp.firstChild.data), dp.attributes['class'].value) for dp in domainposts]
    size2 = int(len(featuresets2) * 0.1)
    train_set2, test_set2 = featuresets2[size2:], featuresets2[:size2]
    classifier2 = nltk.NaiveBayesClassifier.train(train_set2)

    if status_domain_related_or_not_classifier_2==False:
        f = open('tempStorage/trainedData/domain_related_or_not_classifier_2.pickle', 'wb')
        pickle.dump(classifier2, f)
        f.close()


def train_answer_give_or_not_classifier(status_answer_give_or_not_classifier_1,status_answer_give_or_not_classifier_2 ):
    mydoc = minidom.parse('utils/data/answer-give-or-not.xml')

    hasAnswerposts = mydoc.getElementsByTagName('Post');
    posts = nltk.corpus.nps_chat.xml_posts()[:10000]

    def dialogue_act_features(post):
        features = {}
        for word in nltk.word_tokenize(post):
            features['contains({})'.format(word.lower())] = True
        return features

    featuresets = [(dialogue_act_features(post.text), post.get('class')) for post in posts]
    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    if status_answer_give_or_not_classifier_1==False:
        f = open('tempStorage/trainedData/answer_give_or_not_classifier_1.pickle', 'wb')
        pickle.dump(classifier, f)
        f.close()

    featuresets2 = [(dialogue_act_features(dp.firstChild.data), dp.attributes['class'].value) for dp in hasAnswerposts]
    size2 = int(len(featuresets2) * 0.1)
    train_set2, test_set2 = featuresets2[size2:], featuresets2[:size2]
    classifier2 = nltk.NaiveBayesClassifier.train(train_set2)

    if status_answer_give_or_not_classifier_2==False:
        f = open('tempStorage/trainedData/answer_give_or_not_classifier_2.pickle', 'wb')
        pickle.dump(classifier2, f)
        f.close()

