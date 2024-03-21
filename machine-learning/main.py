import pandas as pd
from sklearn.model_selection import train_test_split
from src import data_preprocessing, decision_tree

df = pd.read_csv('data/NintendoGames.csv')

df, platform_mapping, genres_mapping = data_preprocessing.data_preprocessing(df)

features = df.drop('title', axis=1)
targets = df['title']

X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.33, random_state=5)
