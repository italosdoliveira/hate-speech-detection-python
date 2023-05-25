from sklearn.feature_extraction.text import CountVectorizer

def get_vector(instagram_comments):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(instagram_comments)
    
    return X