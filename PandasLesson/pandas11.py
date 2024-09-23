import numpy as np
import pandas as pd


maasDic = {
    "Isim" : ["Alp","Eren","Yilmaz","Mehmet"],
    "Departman" : ["Yazilim","Satis","Pazarlama","Yazilim"],
    "Maas" : [200,300,400,500]
}

df = pd.DataFrame(data = maasDic)

#! unique komutu burada sadece tek bir kere olanlari getirmeye yarar.
#! Tekrar eden verileri ele almaz
print(df["Departman"].unique())

#! Kac adet departman var ? 
#! Burada number of unique Tekrar etmeyen veri adetini simgeler.
print(f"Departman Sayisi = {df["Departman"].nunique()}")

print("===============================")
#! Hangi veriden kac adet oldugunu gosterir
print(f"Hangi departmandan kac adet var ?\n {df['Departman'].value_counts()}")


print("===============================")
#! Ornegin brut maastan net maas a gitmeye calisiyoruz.
#! orani 0.66 verdigimiz senaryoda
def bruttenNete(maas):
    return maas * 0.66

print("Maas hesaplama")

print(df["Maas"].apply(bruttenNete))

#Null deger olup olmadigini gosterir.
print(df.isnull())


#Maas sutununda null deger var mi kontrol eder.
print(df["Maas"].isnull())


print("============================")
newData = {
    "Karakter Sinifi" : ["South Park","South Park","Simpson","Simpson","Simpson"],
    "Karakter Ismi" : ["Cartman","Kenny","Homer","Bart","Bart"],
    "Yas" :[9,10,50,20,20]
}

#Pivot Table
#? orn simpson Bart tan 1 tane daha olsaydi ve yasi da 10 olsaydi
#! Bize bunu toplayarak ortalamasini aldirir.tek bir veri gibi getirirdi.
newdf = pd.DataFrame(data = newData)

print(newdf)
print("============================")
karakterDF1 = newdf.pivot_table(values = "Yas",index = ["Karakter Sinifi","Karakter Ismi"])

print(karakterDF1)
print("============================")
#? Normalde ayni verileri toplayip bu verilerin ortalamasini aldirir.
#! Eger sonuna aggfunc = np.sum yazarsak bu sefer ayni verileri sadece toplar
#! Su anki surum python : 3.12.4 pandas : 2.2.3 bu surumlerde calisiyor. Ileriki surumlerde kaldirilabilir.
karakterDF2 = newdf.pivot_table(values = "Yas",index = ["Karakter Sinifi","Karakter Ismi"],aggfunc=np.sum)

print(karakterDF2)

