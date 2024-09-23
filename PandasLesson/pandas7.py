import numpy as np
import pandas as pd

#!!!! Eksik veri oldugunda ne yapmaliyiz !!!!

#!!! --> np.nan nan bir deger olusturur.

df = pd.DataFrame(
    data={
        "Istanbul" : ["30",29,np.nan],
        "Ankara" : [20,np.nan,24],
        "Izmir" : [40,35,34]
    },
    index = ["Pazartesi","Sali","Carsamba"]
)
print(df)

#! veri olmayanlari siler
#?  Bir row da birden fazla deger varsa hepsini siler.
# df.dropna()

# 0 olursa nan olmayan kolonlari alir.
# 1 olursa nan olmayan satirlari alir.
# df.dropna(axis = 0)

df2 = pd.DataFrame(
    data={
        "Istanbul" : ["30",29,np.nan],
        "Ankara" : [20,np.nan,24],
        "Izmir" : [40,35,34],
        "Antalya" : [45,np.nan,np.nan]
    },
    index = ["Pazartesi","Sali","Carsamba"]
)
print(df2)

#! thresh degeri kaca kadar anlamini tasir.
#? 2 ve uzeri nan degeri varsa dropla anlami tasir burada.
#  inplace = true bir veriye atanmadan direkt kayit edilmesini saglar.
df2.dropna(axis=1,thresh=2,inplace=True)
print(df2)

# nan olanlara otomatik olarak 20 koyar
df2.fillna(20,inplace=True)
print(df2)