import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/NintendoGames.csv')

print(df.head())

features = df.drop('title', axis=1)
targets = df['title']

X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.33, random_state=5)
