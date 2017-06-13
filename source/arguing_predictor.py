
import csv
import os
from datetime import datetime
from nltk import tokenize
from arglex import Classifier #ignore

# Inicializa o arglex
arglex = Classifier()

# show categories names
categories= ["page_id","page_title","contributor","timestamp", 'topic']
categories.extend([arglex.list_categories_names()])
categories.append('sentence')

opinions_file = '/Users/john/projects/source/dataset/enwiki-discussions/rafael_correa_opinions.csv'
sent_file = os.path.splitext(opinions_file)[0] + '_arguing.csv'

with open(sent_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(categories)

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
            stats = arglex.analyse(sentence)
            output = [page_id, page_title, contributor, timestamp, topic]
            output.extend(stats)
            output.append(sentence.encode('utf-8'))
            output_rows.append(output)
            #message = ','.join(stats)
            #print(message)

        with open(sent_file, 'a') as f:
            writer = csv.writer(f,quoting=csv.QUOTE_ALL)
            writer.writerows(output_rows)


