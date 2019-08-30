from django.shortcuts import render
from sklearn import linear_model
import matplotlib.pyplot as plt

def lr(request):
    #creating dataset
    Year = [[2000],[2001],[2002],[2003]]
    Price = [10000,12000,13000,14000]

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
    FuturePrediction = r.coef_ * 2005 + r.intercept_
    print("Prediction of 10 is", FuturePrediction)
        return render(request, 'LR/LinearRegression.html')
