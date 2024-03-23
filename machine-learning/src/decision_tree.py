from sklearn.tree import DecisionTreeRegressor, plot_tree
from matplotlib import pyplot as plt

def decision_tree_regressor(X_train, X_test, y_train, y_test):
      dtr = DecisionTreeRegressor()
      dtr.fit(X_train, y_train)

      plot_tree(dtr, filled=True, feature_names=X_train.columns) 

      plt.savefig('outputs/dtr_' + y_train.name + '.pdf', format='pdf')
      print('Pdf decision tree regressor saved: outputs/' + 'dtr_' + y_train.name + '.pdf')

      score = round(dtr.score(X_test, y_test) * 100, 2)
      
      return score