from sklearn.preprocessing import LabelEncoder

def data_preprocessing(df, target_column):
      # drop rows with missing values
      df = df.dropna()

      # define best game as having a user score >= 7 and a meta score >= 70
      df.loc[:,['best_game']] =((df['user_score'] >= 7.0) & (df['meta_score'] >= 70)).astype(int)

      # take all targets from df 
      targets = df[target_column].copy()

      encoder = LabelEncoder()
      for column in df.columns:
            if df[column].dtype == 'object':
                  encoded_column = encoder.fit_transform(df[column])
                  df.loc[:, column] = encoded_column
                  if column == 'title':
                        df.loc[:, ['decoded_titles']] = encoder.inverse_transform(encoded_column)
      return df, targets