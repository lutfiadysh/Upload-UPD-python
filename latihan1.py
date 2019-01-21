nilai = int(input("Masukkan Nilai Anda: "))

if nilai <= 45 and nilai >= 0:
    print("D")
elif nilai <= 50 and nilai >= 0:
    print("D+")
elif nilai <= 55 and nilai >= 0:
    print("C-")
elif nilai <= 60 and nilai >= 0:
    print("C")
elif nilai <= 65 and nilai >= 0:
    print("C+")
elif nilai <= 70 and nilai >= 0:
    print("B-")
elif nilai <= 75 and nilai >= 0:
    print("B")
elif nilai <= 80 and nilai >= 0:
    print("B+")
elif nilai <= 85 and nilai >= 0:
    print("A-")
elif nilai <= 100 and nilai >= 0:
    print("A")
elif nilai <= 0:
    print("Nilai Salah")
else:
    print("Nilai Salah")