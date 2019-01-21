nama = (input("Nama Anda : "))
bulan = int(input("Berapa lama anda bekerja [bulan] : "))

if bulan >= 48:
    print(nama, "Anda adalah pegawai tetap")
    print("Gaji : Rp 6.000.000")
    print("tunjangan : \n - BPJS kelas I, \n - Keluarga, \n - Hari Raya")
elif bulan >= 36:
    print(nama, "Anda bukan pegawai tetap")
    print("Gaji : Rp 5.500.000")
    print("tunjangan : \n - BPJS kelas II, \n - Keluarga")
elif bulan >= 12:
    print(nama, "Anda bukan pegawai tetap")
    print("Gaji : Rp 4.000.000")
    print("tunjangan : - ")
elif bulan < 12:
    print(nama, "Anda bukan pegawai tetap")
    print("Gaji : RP 3.000.000")
    print("Tunjangan : -")
