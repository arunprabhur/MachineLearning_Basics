from sklearn import linear_model
import matplotlib.pyplot as plt
X = [[1],[2],[3],[4]]
Y = [2,4,6,8]
print("X Y")
for row in zip(X,Y):
    print(row[0][0], "-->", row[0])
plt.scatter(X,Y,color="red")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
r=linear_model.LinearRegression()
r.fit(X,Y)
m=r.coef_[0]
b=r.intercept_
print("slope=",m, "intercept=",b)
predicted_values = [r.coef_ * i + r.intercept_ for i in X]
print(predicted_values)
plt.plot(X,predicted_values,'b')
FuturePrediction = r.coef_ * 10 + r.intercept_
print("Prediction of 10 is", FuturePrediction)
