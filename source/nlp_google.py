import sys
import pandas as pd
import numpy as np
from google.cloud import language



def print_result(annotations):
    score = annotations.sentiment.score
    magnitude = annotations.sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))

    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0

    print('Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0


def analyze():
    """Run a sentiment analysis request on text within a passed filename."""
    language_client = language.Client()
    #filename = '../dataset/wiki/aawd_annotated_sent.csv'
    filename = '../dataset/wiki/opinions_annotated_sent.csv'
    ds = pd.read_csv(filename)

    #ds['sentence'] = ds.text.apply(lambda t: t.replace('.', ' ').replace('\n', ' ').replace('\t', ' '))
    #dat = ds[0:100].text.str.cat(sep='. ')

    if 'sent_score' not in ds.columns:
        ds['sent_score'] =  np.nan
        ds['sent_magnitude'] = np.nan

    counter = 0



    for i, row in ds.iterrows():
        try:
            if not np.isnan(row['sent_score']):
                continue

            if row['lang'] == 'es':
                continue

            # Instantiates a plain text document.
            dat = row['text']
            document = language_client.document_from_text(dat)

            # Detects sentiment in the document.
            annotations = document.annotate_text(include_sentiment=True,
                                                 include_syntax=False,
                                                 include_entities=False)

            ds.loc[i, 'sent_score'] = annotations.sentiment.score
            ds.loc[i, 'sent_magnitude'] = annotations.sentiment.magnitude
            counter += 1

            print(f"sentence {i} score:{annotations.sentiment.score}")

            if counter > 1000:
                break
        except:
            print("Unexpected error:", sys.exc_info()[0])


    ds.to_csv(filename, index=False)

        # Print the results
        # print_result(annotations)



if __name__ == '__main__':
    analyze()
