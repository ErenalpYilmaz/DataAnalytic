import pandas as pd
import numpy as np

## DATAFRAME ##


data = np.random.randn(4,3)
print(data)
print("\n======================================\n")

dataFrame = pd.DataFrame(data)
print(dataFrame[0])


print("\n======================================\n")
#Manuel DataFrame olusturma
newDataFrame = pd.DataFrame(data,index = ["Alp","Zeynep","atlas","Cumali"],columns=["Maas","Yas","CalismaSaati"])
print(newDataFrame)
print(newDataFrame[["Maas"]])
print("\n======================================\n")
#DataFramede ki maas ve yas kolonlarini ve indexlerinin tumunu getirir.
print(newDataFrame[["Maas","Yas"]])
print("\n======================================\n")
# DataFrame olusturma
# Icine Dictionary olusturduk
df = pd.DataFrame(
    {
        "Name" : [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age" : [22,35,45],
        "Sex": ["male", "male", "female"]
    }
)
print(df)
print(df[["Name","Sex"]])

print("\n======================================\n")
#Belirli bir veriye gore arama yapma 
print("Alp in maas , yas ve calisma saati bilgileri gelmistir\n")
print(newDataFrame.loc["Alp"])

print("\n======================================\n")

print("INDEX E GORE maas , yas ve calisma saati bilgileri gelmistir\n")
print(newDataFrame.iloc[1])
