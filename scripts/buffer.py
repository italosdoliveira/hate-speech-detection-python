import pandas as pd
import io
from sklearn.feature_extraction.text import CountVectorizer

#return pandas dataframe
def get_dataframe():
    df = pd.read_csv('../../dataset/HateBR.csv')
    return df

#return all items from column instagram_comments in dataframe
def get_x():
    df = get_dataframe()
    instagram_comments = df['instagram_comments']

    return instagram_comments

def get_y():
    pass
