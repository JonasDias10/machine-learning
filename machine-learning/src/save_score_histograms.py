import matplotlib.pyplot as plt

def save_score_histograms(df):
      plt.figure(figsize=(12, 6))
      plt.title('Histogram of meta score from Nintendo games')
      plt.xlabel('Meta Score')
      plt.ylabel('Frequency of games')
      df['meta_score'].hist()
      plt.savefig('outputs/histogram_meta_score.png')

      plt.figure(figsize=(12, 6))
      plt.title('Histogram of user score from Nintendo games')
      plt.xlabel('User Score')
      plt.ylabel('Frequency of games')
      df['user_score'].hist()
      plt.savefig('outputs/histogram_user_score.png')

      # Save the list of good games with titles, meta scores, and user scores
      good_games_data = df[df['best_game'] == 1].sort_values(by='meta_score', ascending=False)[['decoded_titles', 'meta_score', 'user_score']]
      with open('outputs/good_games.txt', 'w') as file:
            file.write(f"{'Title':85} | Meta Score | User Score\n")
            for index, row in good_games_data.iterrows():
                  file.write(f"{row['decoded_titles']:85} | {row['meta_score']:10} | {row['user_score']:10}\n")

      # Save the list of bad games with titles, meta scores, and user scores 
      bad_games_data = df[df['best_game'] == 0].sort_values(by='meta_score', ascending=False)[['decoded_titles', 'meta_score', 'user_score']]
      with open('outputs/bad_games.txt', 'w') as file:
            file.write(f"{'Title':85} | Meta Score | User Score\n")
            for index, row in bad_games_data.iterrows():
                  file.write(f"{row['decoded_titles']:85} | {row['meta_score']:10} | {row['user_score']:10}\n")