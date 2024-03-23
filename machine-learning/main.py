import pandas as pd
from sklearn.model_selection import train_test_split
from src import data_preprocessing, decision_tree as dtr, linear_regression as lr

df = pd.read_csv('data/NintendoGames.csv')

# preprocessing data with meta_score
df, titles, targets = data_preprocessing.data_preprocessing(df, target_column='meta_score')

# train test split with 33% test size and meta_score as target
X_train, X_test, y_train, y_test = train_test_split(df, targets, test_size=0.33, random_state=5)

dtr_score = dtr.decision_tree_regressor(X_train, X_test, y_train, y_test)
lr_score = lr.linear_regression(X_train, X_test, y_train, y_test)

print('Decision tree score with meta_score: ' + str(dtr_score) + '%')
print('Linear regression score with meta_score: ' + str(lr_score) + '%')

# preprocessing data with user_score
df, titles, targets = data_preprocessing.data_preprocessing(df, target_column='user_score')

# train test split with 33% test size and user_score as target
X_train, X_test, y_train, y_test = train_test_split(df, targets, test_size=0.33, random_state=5)

dtr_score = dtr.decision_tree_regressor(X_train, X_test, y_train, y_test)
lr_score = lr.linear_regression(X_train, X_test, y_train, y_test)

print('Decision tree score with user_score: ' + str(dtr_score) + '%')
print('Linear regression score with user_score: ' + str(lr_score) + '%')