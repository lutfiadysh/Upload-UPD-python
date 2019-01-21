def menu():
    def lingkaran():
        print("Menghitung Luas Lingkaran\n")
        l = int(input("Masukan Jari - jari Lingkaran : "))
        hitung = 3.14*l*l
        print("Hasilnya adalah",hitung)

        t = input("Ingin memakai aplikasi lagi? (y/n) : ")
        if(t=="y") or (t=="Y") or (t=="yes") or (t =="Yes"):
            menu()
        else:
            exit()


    def persegi():
        print("Menghitung Luas Persegi\n")
        p = int(input("Masukan Sisi Persegi : "))
        hitung = p*p
        print("Hasilnya adalah",hitung)

        t = input("Ingin memakai aplikasi lagi? (y/n) : ")
        if (t == "y") or (t == "Y") or (t == "yes") or (t == "Yes"):
            menu()
        else:
            exit()


    def segitiga():
        print("Menghitung Luas Segitiga\n")
        sa = int(input("Masukan Alas Segitiga : "))
        sm = int(input("Masukan Tinggi Segitiga : "))
        hitung = 0.5*sa*sm
        print("Hasilnya adalah",hitung)

        t = input("Ingin memakai aplikasi lagi? (y/n) : ")
        if (t == "y") or (t == "Y") or (t == "yes") or (t == "Yes"):
            menu()
        else:
            exit()


    def fibonacci():
        string = ""

        x = int(input("Masukkan angka :"))
        bar = x
        no = 0

        while bar >= 0:

            kol = bar
            while kol > 0:
                string = string + "   "
                kol = kol - 1

            kiri = 1
            while kiri < (x - (bar - 1)):
                string = string + " " + str(no) + " "
                kiri = kiri + 1

            kanan = 1
            while kanan < kiri - 1:
                string = string + " " + str(no) + " "
                kanan = kanan + 1

            string = string + "\n\n"
            bar = bar - 1
            no = no + 1
        print(string)

        t = input("Ingin memakai aplikasi lagi? (y/n) : ")
        if (t == "y") or (t == "Y") or (t == "yes") or (t == "Yes"):
            menu()
        else:
            exit()


    def siku():
        string = ""
        bar = 1

        x = int(input("Masukkan angka :"))
        no = 1

        while bar <= x:
            kol = bar

            while kol > 0:
                string = string + " " + str(no) + " "
                kol = kol - 1

            string = string + "\n"
            bar = bar + 1
            no = no + 1
        print(string)

        t = input("Ingin memakai aplikasi lagi? (y/n) : ")
        if (t == "y") or (t == "Y") or (t == "yes") or (t == "Yes"):
            menu()
        else:
            exit()



    print("Pilih Program :")
    print("1. Menghitung Luas Lingkaran")
    print("2. Menghitung Luas Persegi")
    print("3. Menghitung Luas Segitiga")
    print("4. Membuat Segitiga Fibonacci")
    print("5. Membuat Segitiga Siku-Siku")
    print("6. Exit")
    r = input("Masukan pilihan (1-6) : ")
    if(r =="1"):
        lingkaran()
    elif(r=="2"):
        persegi()
    elif(r=="3"):
        segitiga()
    elif(r=="4"):
        fibonacci()
    elif(r=="5"):
        siku()
    elif(r=="6"):
        exit()
    else:
        print("Masukan Pilihan diantara 1-6")

q = input("ingin menggunakan Kalkulator? (y/n) : ")
if (q == "y") or (q == "Y") or (q == "yes") or (q == "Yes"):
    menu()
else:
    exit()
