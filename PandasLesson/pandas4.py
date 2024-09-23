import numpy as np
import pandas as pd

data = np.random.randn(4,3)
newDataFrame = pd.DataFrame(data,
                         index = [
                             "Atil",
                             "Alp",
                             "Zeynep",
                             "Osman"
                                  ],
                        columns = ["Maas","Yas","Calisma Saati"]
                         )

print(newDataFrame[["Maas"]])
print("\n=============================\n")
newDataFrame["Emeklilik yasi"] = newDataFrame["Yas"] + newDataFrame["Yas"]
print(newDataFrame)
print("\n=============================\n")
#Emeklilik yasi Column unu siler
print(newDataFrame.drop("Emeklilik yasi",axis = 1))

print("\n=============================\n")

#Row u silme axis = 0 diyebilirsin .

print(newDataFrame.drop("Osman",axis=0))

#inplace True dedigin zaman ana newDataFrame in icinden de siler.
#Silme islemi kalici olmus olur
#inplace degerinin default u false olarak ayarlidir.

print(newDataFrame.drop("Osman",axis=0,inplace=False))

print("\n=============================\n")
#Eger direkt verinin kendisine ulasmak istiyorsak bu sekilde yazmaliyiz.
print(newDataFrame.loc["Atil","Yas"])

print("\n=============================\n")
#Bunu dataframe olarak veriyor.
print(newDataFrame.loc[["Atil"],["Yas"]])

#Tabloda maaslari 0 den kucuk olanlari True / False olarak yazdir.
print( newDataFrame[["Maas"]] < 0 )

print("\n=============================\n")
booleanFrame = newDataFrame["Maas"] < 0
print(newDataFrame[booleanFrame])


print("\n=============================\n")

#Yas degeri 0 dan buyuk olanlari gosterir
print(newDataFrame[newDataFrame['Yas'] > 0 ])