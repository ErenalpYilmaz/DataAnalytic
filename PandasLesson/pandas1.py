import numpy as np
import pandas as pd

# Series / Seriler

myDic = {"Atil":    50 ,
         "Zeynep":  40 ,
         "Mehmet":  30  }
#Veri tipini gosterir ve excel gibi yazdirir.
print(pd.Series(myDic))

print("====================================")

myAges = [50,40,30]
myNames = ["alp","Neo","Toprak"]

#Bu iki kullanim da dogrudur.
#print(pd.Series(myAges,myNames))
print(pd.Series(index = myNames, data = myAges))

print("====================================")
#Datalari numpy dan aldik indexleri ise myNames dizisinden aldik.
numpyArray = np.array([50, 40, 30])
print(pd.Series(numpyArray , myNames))