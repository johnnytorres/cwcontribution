from preprocessing.opinions_extractor import extract_opinions
from preprocessing.revisions_extractor import extract_revisions

from polarity_scorer_nltk import analyze_sentiment

if __name__ == '__main__':

    wiki_file = '../dataset/enwiki-discussions/rafael_correa.xml'

    revisions_file = extract_revisions(wiki_file)
    opinions_file = extract_opinions(revisions_file)
    analyze_sentiment(opinions_file)
