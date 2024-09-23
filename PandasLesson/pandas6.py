import numpy as np
import pandas as pd

firstIndex = ["Simpson","Simpson","Simpson","South Park","South Park","South Park"]
icIndex = ["Homer","Bart","Marge","Cartman","Kenny","Kyle"]
#Bu iki diziyi birbirleri ile esledik.
birlesikIndex = list(zip(firstIndex,icIndex))

#Datalari tuples in icine koyuyor.
birlesikIndex = pd.MultiIndex.from_tuples(birlesikIndex)
print(birlesikIndex)

print("\n==========================\n")
myCartoonList = [[40,"A"],[10,"B"],[30,"C"],[9,"D"],[10,"E"],[11,"F"]]
cartoonNumpyArray = np.array(myCartoonList)
print(f'cartoonlist = {myCartoonList} ve\n cartoonNumpyArray = {cartoonNumpyArray}')

print("\n==========================\n")
df = pd.DataFrame(
    data = cartoonNumpyArray,
    index = birlesikIndex,
    columns=["Yas","Meslek"],
)
print(df)
print("\n==========================\n")
print("Homer in bilgileri")
print(df.loc["Simpson"].loc["Homer"])
print("\n==========================\n")

#--> DataFrame de indexlere isim verme islemi

df.index.names = ["Film Ad","Isim"]
print(df)