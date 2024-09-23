import numpy as np
import pandas as pd

## MERGE ##

dictionary1 = {
    "isim" : ["Ahmet","Mehmet","Zeynep","Atil"],
    "Spor" : ["Kosu","Yuzme","Kosu","Basketbol"],
}

dictionary2 = {
    "isim" : ["Ahmet","Mehmet","Zeynep","Atil"],
    "Kalori" : [100,200,300,400]
}

df = pd.DataFrame(data = dictionary1)
df2 = pd.DataFrame(data = dictionary2)

print(f"dataframe1 = {df}")
print(f"dataframe2 = {df2}")

print("=======================")

#Hangi kolon uzerinden merge edilicekse on = "name"
#seklinde kullanilir. isim e gore merge ler.
#Ortak bir data belirlenir ve ortak dataya gore islemleri yapiyor.
mergedf = pd.merge(df,df2,on="isim")
print(mergedf)