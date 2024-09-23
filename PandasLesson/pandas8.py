import numpy as np
import pandas as pd

##  GROUPBY-----------GRUPLAMA


df = pd.DataFrame(
    data = {
        "Departman" : [
            "Yazilim Departmani",
            "Yazilim Departmani",
            "Pazarlama Departmani",
            "Pazarlama Departmani",
            "Hukuk Departmani",
            "Hukuk Departmani"],

        "CalisanIsmi" : [
            "Ahmet",
            "Mehmet",
            "Atil",
            "Burak",
            "Alp",
            "Fatma"
        ],

        "Maas" : [
            1900,
            2000,
            2100,
            2200,
            2300,
            2400
        ]

    }
)
print(df)
print("\n=======================\n")
groupObjects = df.groupby("Departman")

#Hangi departmanda kac kisi calisiyor gormek icin
print(groupObjects.count())
print("\n============================\n")

#Departmandaki kisilerin ortalama maaslarini gormek icin
print(groupObjects.mean('Maas'))
print("\n============================\n")

#Gruptakilerin minimumlari al
print(groupObjects.min())
print("\n============================\n")

#Gruptakilerin maximumlarini al
print(groupObjects.max())
print("\n============================\n")

# Ekstra ozellikleri hesapliyor. Detayli hesaplama std : standart sapma  
print(groupObjects.describe())