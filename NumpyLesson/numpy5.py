import numpy as np
myArray = np.arange(0,20)
print(myArray)

#Index e gore gosterme
print("====================")

print(myArray[3:6])

print("====================")
#Belirli index arasindaki verileri -5 yaptik
myArray[3:8] = -5
print(myArray)


anotherArray = np.arange(0,24)

print(anotherArray)
print("====================")

slicingArray = anotherArray[4:9]
print(slicingArray)

print("=============== -->slicingArray Dizi icindeki verileri baska bir veriye esitleme")
slicingArray[:] = 700
print(slicingArray)

print("=============== --> Another Dizisi de degisti.")
print(anotherArray)

print("======================")
#Slicing isleminde veri degistiginde ana array degismesin istiyorsan bunu yap
ornekArray = np.arange(0,24)
print(ornekArray)

print("====================== --> OrnekdiziKopyasindayiz")
ornekArrayCopy = ornekArray.copy()
print(ornekArrayCopy)
print("======================")
ornekArrayCopySlicing = ornekArrayCopy[3:6]
ornekArrayCopySlicing[:] = 800
print(ornekArrayCopySlicing)
print("====================== Slicing isleminden sonra kopyasinda da degisti ama ana verilere bir sey olmadi.")
print(ornekArrayCopy)
print("======================")
print("======================")
