import pandas as pd
from sklearn.model_selection import train_test_split
from src import data_preprocessing, decision_tree as dt, save_score_histograms as ssh

df = pd.read_csv('data/NintendoGames.csv')

# save score histograms
ssh.save_score_histograms(df)
