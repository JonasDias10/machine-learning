from sklearn.naive_bayes import GaussianNB

def naive_bayes(X_train, X_test, y_train, y_test):
      clf = GaussianNB()
      clf = clf.fit(X_train, y_train)
      return clf.predict(X_test)
