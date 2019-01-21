nilai = int(input("Masukkan nilai anda : "))

if nilai >= 80:
    ket = "A"
elif nilai >= 75:
    ket = "B"
elif nilai >= 70:
    ket = "C"
elif nilai >= 65:
    ket = "D"
else:
    ket = "E"

print("Nilai anda", nilai , "Keterangan", ket )