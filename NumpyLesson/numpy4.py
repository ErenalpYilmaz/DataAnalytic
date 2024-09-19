import numpy as np

#NUMPY dizi methodlari

myNumpyDizi = np.arange(30)

print(myNumpyDizi)
print("====================")
#Dizi eleman sayisi onemli 6 x 5 = 30 dan bu sonuca varabiliyoruz.
print(myNumpyDizi.reshape(5,6))

print("====================#Dizideki max sayiyi gosterir")
#Dizideki max sayiyi gosterir
print(myNumpyDizi.max())

print("====================#Dizidekli min sayiyi gosterir.")
#Dizidekli min sayiyi gosterir.
print(myNumpyDizi.min())

print("====================#En buyuk sayi kacinci indexte onu gosterir.")
#En buyuk sayi kacinci indexte onu gosterir.
print(myNumpyDizi.argmax())
print("====================#En kucuk sayi kacinci indexte gosterir")
#En kucuk sayi kacinci indexte gosterir
print(myNumpyDizi.argmin())

print("====================")

print(myNumpyDizi.shape)
reshapeDizim = myNumpyDizi.reshape(5,6)
print(reshapeDizim)

print("==================== Shape komutu ile dizinin durumundan haberdar olabiliyoruz")
print(reshapeDizim.shape)