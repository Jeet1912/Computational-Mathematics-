import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

first = int(input("Enter the first year \n"))
last  = int(input("Enter the last year \n"))

# if class interval != 1, pass it's value using step in range
time_line = []
for i in range(first,last+1):
    time_line.append(i)

l = len(time_line)
values = []
for i in range(0,l):
    values.append(float(input("Enter "+str(i)+"th value \n")))
dictionary = {"Year" : time_line, "givenReading" : values}
dataSet = pd.DataFrame(dictionary)
#print(dataSet)

if( l % 2 != 0):
    u = time_line[int(l/2)]
    dataSet["Ui"] = dataSet['Year'] - u
    dataSet["UiYi"]= dataSet["Ui"] * dataSet["givenReading"]
    dataSet["Ui^2"]= dataSet["Ui"] * dataSet["Ui"]
    sigUi2 = dataSet["Ui^2"].sum()
    sigUiYi = dataSet["UiYi"].sum()
    sigYi = dataSet["givenReading"].sum()
    a = sigYi / l
    b = sigUiYi / sigUi2
    dataSet["Trend"] = a + b * dataSet["Ui"]
    dataSet["Additive Model"] = dataSet["givenReading"] - dataSet["Trend"]
    dataSet["Multiplicative Model"] = dataSet["givenReading"]/dataSet["Trend"]
    print(dataSet)
    plt.plot(dataSet['Year'],dataSet["givenReading"],label = "givenValues")
    plt.plot(dataSet['Year'],dataSet["Trend"],label = "Trend")
    plt.legend(loc = 2)
    plt.show()
  
else:
    class_interval = dataSet.loc[1,"Year"] - dataSet.loc[0,"Year"]
    u = 0.5 * (time_line[int(l/2)-1] + time_line[int(l/2)])
    dataSet["Ui"] = (dataSet["Year"] - u) / (0.5 * class_interval)
    dataSet["UiYi"]= dataSet["Ui"] * dataSet["givenReading"]
    dataSet["Ui^2"]= dataSet["Ui"] * dataSet["Ui"]
    sigUi2 = dataSet["Ui^2"].sum()
    sigUiYi = dataSet["UiYi"].sum()
    sigYi = dataSet["givenReading"].sum()
    a = sigYi / l
    b = sigUiYi / sigUi2
    dataSet["Trend"] = a + b * dataSet["Ui"]
    print(dataSet)
    dataSet["Additive Model"] = dataSet["givenReading"] - dataSet["Trend"]
    dataSet["Multiplicative Model"] = dataSet["givenReading"]/dataSet["Trend"]
    plt.plot(dataSet['Year'],dataSet["givenReading"],label = "givenValues")
    plt.plot(dataSet['Year'],dataSet["Trend"],label = "Trend")
    plt.legend(loc = 2)
    plt.show()
 
