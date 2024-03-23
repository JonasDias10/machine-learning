from sklearn.linear_model import LinearRegression 

def linear_regression(X_train, X_test, y_train, y_test):
      lr = LinearRegression()
      lr = lr.fit(X_train, y_train)

      return round(lr.score(X_test, y_test) * 100, 2)
