def remove_outliers(df,column):

    q1=df[column].quantile(0.25)
    q3=df[column].quantile(0.75)

    iqr=q3-q1

    lower=q1-1.5*iqr
    upper=q3+1.5*iqr

    return df[(df[column]>=lower)&(df[column]<=upper)]