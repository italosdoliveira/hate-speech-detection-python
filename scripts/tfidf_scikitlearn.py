from sklearn.feature_extraction.text import TfidfVectorizer

def get_vector(instagram_comments):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(instagram_comments)

    return X