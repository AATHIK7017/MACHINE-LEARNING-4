y_pred=knn.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print(accuracy)
knn.predict([[123,45]])
