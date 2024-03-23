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
