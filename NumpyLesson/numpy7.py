import numpy as np
## OPERASYONLAR --> Filtreleme Islemleri

#Icinde rastgele sayilar olan bir dizi olusturduk
createArray = np.random.randint(1,100,20)

print(createArray)
#Bu rastgele sayilardan 25 ten buyuk olanlari true kucuk olanlari false seklinde
#resultarray e yazdirdik
resultArray = createArray > 25

print(resultArray)

#createArray dizisinde true deger verenleri newarray e aktardik yani
#dizi icindeki verilerde 25 ten buyuk sayilari newarray in icine aktardik
newArray = createArray[resultArray]
print(newArray)

#-->
print("-------------------------------------")
lastArray = np.arange(0,24)

#Diziler kendi indexlerine karsilik gelen sayilari birbirleri ile toplayabilir , cikarabilir , carpabilir ve bolebiliriz.
#Kisaca matematiksel islemler yapabiliriz.
print(lastArray+lastArray)

print(np.sqrt(lastArray))