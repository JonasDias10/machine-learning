from sklearn import tree

def decision_tree(X_train, X_test, y_train, y_test):
      clf = tree.DecisionTreeClassifier()
      clf = clf.fit(X_train, y_train)
      return clf.predict(X_test)
