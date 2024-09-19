#Numpy in kendi random kutuphanesi
import numpy as np

# Rastgele sayilarla matrix olusturur.
print(np.random.randn(3,3))

# Tek bir deger dondurmek icin --> randint 1 doner 10 donmez
print("==============")
print(np.random.randint(1,10))
print("==============")

# Rastgele bir sekilde 1 ile 100 arasinda 6 adet sayi dondurur
print(np.random.randint(1,100,6))

# Degiskene atama islemlerim
myNumpyDizim = np.arange(30)
print(myNumpyDizim)

 