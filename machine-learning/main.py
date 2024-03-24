import pandas as pd
from src import data_preprocessing, save_score_histograms as ssh, k_neighbors as kn

df = pd.read_csv('data/NintendoGames.csv')

# preprocess data
df, targets = data_preprocessing.data_preprocessing(df, 'best_game')

# save score histograms
ssh.save_score_histograms(df)

# run k-nearest neighbors
kn.k_neighbors(df, targets)
