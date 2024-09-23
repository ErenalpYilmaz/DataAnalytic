import numpy as np 
import pandas as pd

data = np.random.randn(4,3)

df = pd.DataFrame( data ,
                  index = [
                      "Ali","Osman","Mehmet","Ali"
                  ],
                  columns=[
                      "Maas","Yas","Calisma Saati"
                  ]
)
print(df)

#Indexleri sifirlar inplace=True eklersek ana dataframe e de eklenir
print(df.reset_index())

print("\n========================================\n")

#DataFrame in indexlerini degistirir.
#Eger gecerli kalmasini istiyorsan inplace = True komutunu eklemelisin.
newIndexList = ["Ati","Zeyn","Atl","Meh"]
df["New Index"] = newIndexList
print(df.set_index("New Index"))

print("\n========================================\n")

#Yeni Column Ekleme Islemleri
newColumnList = ["05421828167","05465421123","05548658585","05641233232"]
df["Tel"] = newColumnList
print(df)

#Girilen sayi adeti kadar veriyi gosterir.
print(df.head(3))