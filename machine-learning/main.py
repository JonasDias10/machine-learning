import pandas as pd
from src import data_preprocessing as dp, save_score_histograms as save_score
from src import k_neighbors as kn, naive_bayes as nb, neural_network as neural_n
from src import save_comparison as comp

df = pd.read_csv('data/NintendoGames.csv')

# preprocess data
df, targets = dp.data_preprocessing(df, 'best_game')

# save score histograms 
save_score.save_score_histograms(df)

# Drop the decoded_titles column from the DataFrame
df = df.drop(columns=['decoded_titles'], axis=1) 

# run k-nearest neighbors algorithm
kn.k_neighbors(df, targets)

# run naive bayes algorithm
nb.naive_bayes(df, targets)

# run neural network algorithm
neural_n.neural_network(df, targets)

comp.save_algorithms_comparison('k_neighbors_results.txt', 'naive_bayes_results.txt', 'neural_network_results.txt')