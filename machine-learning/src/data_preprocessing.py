from sklearn.preprocessing import LabelEncoder

def data_preprocessing(df):
      # drop rows with missing values
      df = df.dropna()

      # drop columns that are not needed
      df = df.drop(['date', 'link', 'esrb_rating', 'developers'], axis=1)

      # encode platform
      label_encoder = LabelEncoder()

      df['platform'] = label_encoder.fit_transform(df['platform'])

      # platform mapping 
      platform_mapping = dict(zip(range(len(label_encoder.classes_)), label_encoder.classes_))

      # encode genres
      df['genres'] = label_encoder.fit_transform(df['genres'])

      # genre mapping
      genres_mapping = dict(zip(range(len(label_encoder.classes_)), label_encoder.classes_))

      return df, platform_mapping, genres_mapping