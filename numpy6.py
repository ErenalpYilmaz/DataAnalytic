import numpy as np
### MATRIX ###

myList = [[10,20,30],[20,30,40],[40,50,60]]

myMatrix = np.array(myList)

print(myMatrix)

#Iki kullanimda aynidir.
print(myMatrix[1][2])
print(myMatrix[1,2])

#1. indexten itibaren her dizinin 2. indexini getirir.
#Ilk i dizinin kactan itibaren alinacagini belirtir.
#Ikincisi ise Dizi icindeki kacinci indexin alinicahi
print(myMatrix[1:,2:])

myListe = [[1, 2, 3, 4, 101], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]

myMatrixx = np.array(myListe)
print("-----------------------------")
#Dizi icinde dizi de aranabiliyor.
#0 , 2 ve 4. index numarali dizileri ekrana getirir.
print(myMatrixx[[0,2,4]])