import numpy as np
import pandas as pd

dictionary1 = {
    "isim" : ["Ahmet","Mehmet","Zeynep","Atil"],
    "Spor" : ["Kosu","Yuzme","Kosu","Basketbol"],
    "Kalori" : [100,200,300,400]
}

dictionary2 = {
    "isim" : ["Alp","Veli","Osman","Ayse"],
    "Spor" : ["Kosu","Yuzme","Kosu","Basketbol"],
    "Kalori" : [100,200,300,400]
}
dictionary3 = {
    "isim" : ["Ayse","Mahmut","Duygu","Nur"],
    "Spor" : ["Basketbol","Yuzme","Kosu","Yuzme"],
    "Kalori" : [150,300,300,400]
}

df1 = pd.DataFrame(data = dictionary1,index = [0,1,2,3])
df2 = pd.DataFrame(data = dictionary2,index = [4,5,6,7])
df3 = pd.DataFrame(data = dictionary3,index = [8,9,10,11])
print(df1)
print(df2)
print(df3)

print("===============================")

# concatenation (Birlestirme Islemi)

new = pd.concat([df1,df2,df3],axis = 0)
print(new)