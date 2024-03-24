from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix

def k_neighbors(df, targets):
      X_train, X_test, y_train, y_test = train_test_split(df, targets, test_size=0.2, random_state=42)

      knn = KNeighborsClassifier(n_neighbors=2)
      knn.fit(X_train, y_train)

      y_pred = knn.predict(X_test)

      accuracy = accuracy_score(y_test, y_pred) * 100
      precision = precision_score(y_test, y_pred) * 100
      recall = recall_score(y_test, y_pred) * 100
      
      # save txt with the results
      with open('outputs/k_neighbors_results.txt', 'w') as f:
            f.write('K-Nearest Neighbors Results\n\n')
            f.write('Accuracy: {:.2f}%\n'.format(accuracy))
            f.write('Precision: {:.2f}%\n'.format(precision))
            f.write('Recall: {:.2f}%\n'.format(recall))
            