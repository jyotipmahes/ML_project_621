import numpy as np
import pandas as pd
from collections import Counter


def summary(df):
    """
    input: The function takes in a data frame
    output: It counts total number of records and unique records present in each column
    """

    print("Total number of records: ",len(df))
    for i in df.columns:
        print('Distinct {} in dataframe: {}'.format(i,len(np.unique(df[i].astype('str')))))


def count_na(df):
    """
    input: The function takes in a data frame
    output: It counts number of NA values in each column and % of NA values 
    """
    new=pd.DataFrame(df.isnull().astype('int').sum(axis=0),columns=["NA_count"])
    new['Percentage']=df.isnull().astype('int').sum(axis=0)*100/len(df)
    return new


def data_category_counter(df):
    counters = dict()
    for col in df.columns:
        counters[col] = Counter(df[col])
    return counters


def test_train_diff(train, test):
    count = dict()
    columns = set(train.columns).intersection(test.columns)
    for col in columns:
        set1 = set(train[col])
        set2 = set(test[col])
        new_item = len(set2-set1)
        count[col] = new_item
    return count


def genres_separate(genre_ids):
    """
    Each genre represented by a three-digit number, and there are songs 
    have more than one genres. We want to separate them. 
    Input: column"genre_ids" of song.csv file.
    Output: devided all possible categories existed for each of the song.
            return a dictionary where key=distinguish genre_id,
            value=number of songs belongs to that specific genre_id.
    """
    genre_dictionary = {}
    for genre_id in genre_ids:
        if type(genre_id) != str:
            continue
        genre_list = genre_id.split('|')
        for genre in genre_list:
            if genre not in genre_dictionary:
                genre_dictionary[genre] = 1
            else:
                genre_dictionary[genre] += 1
    
    return genre_dictionary  


def song_play_times(song_ids): 
    """
    We also want to know the frequencies of each song.
    input: distinct song info(ie song id).
    output: a dictionary with key=song_id, value=number of times it's played.
    or 
    We can also use a similar function for frequencies of languages.
    input: distinct language(each language represented by a different number).
    output: a dictionary with key=language, value=number of songs in this specific language.
    """
    song_play_dict = {}

    for song_id in song_ids:
        if song_id not in song_play_dict:
            song_play_dict[song_id] = 1
        else:
            song_play_dict[song_id] += 1
    
    return song_play_dict



