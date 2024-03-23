from sklearn.tree import DecisionTreeClassifier, plot_tree
from matplotlib import pyplot as plt

def decision_tree_classifier(X_train, X_test, y_train, y_test):
      dtc = DecisionTreeClassifier()
      dtc.fit(X_train, y_train)

      plot_tree(dtc, filled=True, feature_names=X_train.columns) 

      plt.savefig('outputs/dtc_' + y_train.name + '.pdf', format='pdf')
      print('Pdf decision tree classifier saved: outputs/' + 'dtc_' + y_train.name + '.pdf')

      score = round(dtc.score(X_test, y_test) * 100, 2)
      
      return score