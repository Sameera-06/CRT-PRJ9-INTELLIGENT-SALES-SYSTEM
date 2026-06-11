import pandas as pd

def clean_data(df):

    df.drop_duplicates(inplace=True)

    df.fillna(method='ffill', inplace=True)

    return df