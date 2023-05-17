import buffer
from sklearn.feature_extraction.text import CountVectorizer

def get_ngrams_vector():
    instagram_comments = buffer.list_comments()

    vectorizer = CountVectorizer()