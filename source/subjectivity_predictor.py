
import csv
import os
from datetime import datetime
from nltk import tokenize
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *


opinions_file = '/Users/john/projects/source/dataset/enwiki-discussions/rafael_correa_opinions.csv'
sent_file = os.path.splitext(opinions_file)[0] + '_subjectivity.csv'

with open(sent_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["page_id","page_title","contributor","timestamp", 'topic', 'subjectivity',  'sentence'])

n_instances =100
subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]

n_train_instances = 80
train_subj_docs = subj_docs[:n_train_instances]
test_subj_docs = subj_docs[n_train_instances:n_instances]
train_obj_docs = obj_docs[:n_train_instances]
test_obj_docs = obj_docs[n_train_instances:n_instances]
training_docs = train_subj_docs+train_obj_docs
testing_docs = test_subj_docs+test_obj_docs

sentim_analyzer = SentimentAnalyzer()
all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])

unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)
training_set = sentim_analyzer.apply_features(training_docs)
test_set = sentim_analyzer.apply_features(testing_docs)
trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)

#for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
#    print('{0}: {1}'.format(key, value))


with open(opinions_file, 'r') as f:
    csvreader = csv.reader(f)
    csvreader.next()

    for row in csvreader:
        page_id = row[0]
        page_title = row[1]
        contributor = row[2]
        timestamp = datetime.fromtimestamp(float(row[3]))
        comment = row[4]
        topic = row[5]
        opinion = row[6].decode('utf-8')
        sentences = tokenize.sent_tokenize(opinion)
        output_rows = []

        for sentence in sentences:
            ss = sentim_analyzer.classify(sentence)
            output = [page_id, page_title, contributor, timestamp, topic, ss, sentence.encode('utf-8')]
            output_rows.append(output)
            #message = ','.join(stats)
            #print(message)

        with open(sent_file, 'a') as f:
            writer = csv.writer(f,quoting=csv.QUOTE_ALL)
            writer.writerows(output_rows)
