import pandas as pd
from sklearn.model_selection import train_test_split
from src import data_preprocessing, decision_tree as dtr

df = pd.read_csv('data/NintendoGames.csv')

df, titles, targets = data_preprocessing.data_preprocessing(df, target_column='meta_score')

X_train, X_test, y_train, y_test = train_test_split(df, targets, test_size=0.33, random_state=5)

dtr.decision_tree_regressor(X_train, X_test, y_train, y_test, file_name='dtr_meta_score.pdf')
