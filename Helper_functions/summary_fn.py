import numpy as np
import pandas as pd


def summary(df):
    """
    input: The function takes in a data frame
    output: It counts total number of records and unique records present in each column
    """

    print("Total number of records: ",len(df))
    for i in df.columns:
        print('Distinct {} in train: {}'.format(i,len(np.unique(df[i].astype('str')))))


def count_na(df):
    """
    input: The function takes in a data frame
    output: It counts number of NA values in each column and % of NA values 
    """
    new=pd.DataFrame(df.isnull().astype('int').sum(axis=0),columns=["NA_count"])
    new['Percentage']=df.isnull().astype('int').sum(axis=0)*100/len(df)
    return new
