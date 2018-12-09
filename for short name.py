# BORSADA İŞLEM GÖREN SENETLERE KISA AD OLUŞTURMAK:
isim = input("İsim girin: ")
if len(isim) <= 5:
    print(isim[:5])
else:
    print(isim[:5].upper())
