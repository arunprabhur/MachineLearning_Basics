from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

#creating dataset
Year = [[2000],[2001],[2002],[2003],[2000],[2001],[2002],[2003],[2000],[2001],[2002],[2003]]
Price = [10000,12000,13000,14000,10500,12500,13005,14000,10040,12050,13500,14500]

#Display mapping
for row in zip(Year,Price):
    print(row[0][0], "-->", row[1])

#plotting graph for dataset using matplotlib
plt.scatter(Year,Price,color="red")
plt.xlabel("Year")
plt.ylabel("Price")

#creating model using scikit-learn
r=linear_model.LinearRegression()
r.fit(Year,Price)

#Get co-eff and intercept for y = mx + b
m=r.coef_[0]
b=r.intercept_
print("slope=",m, "intercept=",b)

#Predict Values and draw graph
predicted_values = [r.coef_ * i + r.intercept_ for i in Year]
print(predicted_values)
plt.plot(Year,predicted_values,'b')
plt.savefig('graph.png')

#Prediction for Future 
FuturePrediction = r.coef_[0] * 2003 + r.intercept_
print("Prediction of 2003 is", FuturePrediction)

#Accuracy findings
print("Prediction function from scikit-learn",r.predict([[2003]]))
y_true = Year
y_pred = predicted_values

print("Mean squred error is" , mean_squared_error(y_true, y_pred))
print("R2 Score Function" , r2_score(y_true, y_pred))
