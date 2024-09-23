import numpy as np
import pandas as pd


#EXCELLE NASIL CALISILIR.

dataFrame = pd.read_excel("dosyaYolu")

print(dataFrame)

#Bos verisi olanlari atar . 
dolu_degerler_dataframe = dataFrame.dropna()


#Degistirilen tabloyu excel e kaydetme islemleri
#Bunu yeni bir excel dosyasi olusturarak yapar.
dolu_degerler_dataframe.to_excel("yenimaas.xlsx")

## eger veriler csv seklinde gelirse read_csv ile cagirmak gerekiyor
## Yazmak icin ise to_csv seklinde kullanilir. (excel yerine)