print("""*****************************************
Hesap Makinesi Programı

1.Toplama İşlemi
2.Çıkarma İşlemi
3.Çarpma İşlemi
4.Bölme İşlemi


********************************************
""")
sayi1=float(input("1.Sayıyı Girin:"))
sayi2=float(input("2.Sayıyı Girin:"))
islem=int(input("İşlemi Girin:"))
if islem==1:
    print("{} ile {}' nin toplamı {} ' dir.".format(sayi1,sayi2,sayi1+sayi2))
elif islem==2:

    if sayi1-sayi2<0:
        print("{} ile {} farkı {}'dir.".format(sayi1,sayi2,sayi2-sayi1))

    else:
        print("{} ile {} 'nin farkı {}'dir.".format(sayi1,sayi2,sayi1-sayi2))
elif islem==3:
    print("{} ile {}'nin çarpımı {}'dir.".format(sayi1,sayi2,sayi1*sayi2))
elif islem==4:
    print("{} ile {}'nin bölümü {}'dir.".format(sayi1,sayi2,sayi1//sayi2))
else:
    print("Geçersiz İşlem")
