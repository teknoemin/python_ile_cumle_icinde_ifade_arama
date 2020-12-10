ana_metin = "USAK emin"
aranacak_obek = "ver"
arama_komutu = ana_metin.find(aranacak_obek)
if (arama_komutu > 0):
	onceki = ana_metin[arama_komutu - 1]
	sonraki = ana_metin[arama_komutu + len(aranacak_obek)]
	print(onceki + aranacak_obek + sonraki)
else:
	print("Aranan değer bulunamadı!")