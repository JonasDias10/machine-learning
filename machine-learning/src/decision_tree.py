from sklearn.tree import DecisionTreeRegressor, plot_tree
from matplotlib import pyplot as plt

def decision_tree_regressor(X_train, X_test, y_train, y_test, file_name):
      dtr = DecisionTreeRegressor()
      dtr.fit(X_train, y_train)

      plot_tree(dtr, filled=True, feature_names=X_train.columns) 

      plt.savefig('outputs/' + file_name, format='pdf')
      print('Pdf decision tree regressor saved: outputs/' + file_name)

      print('Decision tree regressor score: ', round(dtr.score(X_test, y_test) * 100, 2), '%')