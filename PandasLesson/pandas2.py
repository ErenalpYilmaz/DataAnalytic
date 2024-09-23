import numpy as np
import pandas as pd


#Elle tanimlama
print(pd.Series(["Alp","Atlas","Osman"]))
print("==========================================")

print(pd.Series(["Alp","Atlas","Osman"],[1,2,3]))
print("==========================================")

#Bir degiskene atayarak tanimlama
result1 = pd.Series([10,5,1],["Atlas","Alp","Osman"])
print(result1)
print("==========================================")

result2 = pd.Series([20,10,8],["Atlas","Alp","Osman"])
print(result2)
print("==========================================")
#pandas result1 ve result2 de ayni index'lere bakip datalarini toplayabilir . Matematiksel islemlerin hepsi icin gecerli
resultLast = result1 + result2
print(resultLast)
print("==========================================")

#Farkli tanimlamalar yapildi
diffSeries = pd.Series([20, 30, 40, 50],['a','b','c','d'])
diffSeries1 = pd.Series([10, 5, 3, 1],['a','c','f','e'])
#Ortak olmayanlar null verir. Ortak olanlar ise toplanir. 
print(diffSeries+diffSeries1)