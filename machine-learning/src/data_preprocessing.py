from sklearn.preprocessing import LabelEncoder

def data_preprocessing(df, target_column):
      # drop rows with missing values
      df = df.dropna()

      # take all titles
      titles = df['title']

      # encode values from df that need to be encoded to numbers
      for column in df.columns:
            if df[column].dtype == 'object':
                  encoded_column = LabelEncoder().fit_transform(df[column])
                  df.loc[:, column] = encoded_column

      # take all targets from df 
      targets = df[target_column]

      return df, titles, targets