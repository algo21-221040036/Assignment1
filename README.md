# 一.Article Summary

​	The title of the paper is "A Labeling Method for Financial Time Series Prediction Based on Trends", and the web link is https://www.mdpi.com/1099-4300/22/10/1162.

​	This paper first proposes a dimension expansion of the daily closing price, and then uses a new method to standardize it. The benefit of normalizing with this new method is that it prevents future information from being used. Then use a new method to mark future ups and downs. Previously, the price of the next day and the price of the current day were directly used for comparison. The problem with this is that it is very sensitive to the noise of small fluctuations, so it should be directly judged whether the point is in a on rising or falling bands. Finally, machine learning is used to train the labeled data.

# 二.Reproduce method

## 1.Prepare

numpy : 1.20.3

pandas : 1.3.4

sklearn : 0.24.2

Select the closing price of CSI 500etf from 2014 to 2021, and the data comes from Mikuang.

## 2.Result

In this article, the entire data set is divided into a training set and a test set. I use the daily one-year review cycle data for training and then predict the current day. Using random forest, KNN, SVM and logistic regression for testing, random forest has the best effect, and logistic regression has the worst effect, indicating that the training set may not be linearly separable.





