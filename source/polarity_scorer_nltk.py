
import csv
import os
from datetime import datetime
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize


def analyze_sentiment(opinions_file):

    sid = SentimentIntensityAnalyzer()

    sent_file = os.path.splitext(opinions_file)[0] + '_sentiment.csv'

    with open(sent_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["page_id","page_title","contributor","timestamp", 'topic', 'compound', 'neg','neu','pos', 'sentence'])

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
                ss = sid.polarity_scores(sentence)
                stats = ['{0}'.format(ss[k]) for k in sorted(ss)]
                output = [page_id, page_title, contributor, timestamp, topic]
                output.extend(stats)
                output.append(sentence.encode('utf-8'))
                output_rows.append(output)
                #message = ','.join(stats)
                #print(message)

            with open(sent_file, 'a') as f:
                writer = csv.writer(f,quoting=csv.QUOTE_ALL)
                writer.writerows(output_rows)

if __name__ == '__main__':
    opinions_file = '/Users/john/projects/source/dataset/enwiki-discussions/rafael_correa_opinions.csv'
    analyze_sentiment(opinions_file)