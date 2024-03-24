import pandas as pd
from sklearn.model_selection import train_test_split
from src import data_preprocessing, save_score_histograms as ssh

df = pd.read_csv('data/NintendoGames.csv')

# preprocess data
df, targets = data_preprocessing.data_preprocessing(df, 'best_game')

# save score histograms
ssh.save_score_histograms(df)
