import math as mt
# Membuat Program Menghitung
def main_menu():
    # Membuat daftar Menu pada program
    print ('=' * 10,"Pilih Program Bangunan Datar", '=' * 10)
    print ("1. Program Persegi Panjang")
    print ("2. Program Segitiga")
    print ("3. Program Lingkaran")
    print ("4. Program Belah Ketupat")
    print ("5. Exit Program")
    print ('=' * 35)
    # Pilihan input
    pilihan = input("Pilih Menu : ")
    # Pilihan Menu
    if pilihan == '1':
        persegi_panjang()
    elif pilihan == '2':
        segitiga()
    elif pilihan == '3':
        lingkaran()
    elif pilihan == '4':
        belah_ketupat()
    else:
        print ('=' * 35)
        print ("Program Keluar")
        print ('=' * 35)
        exit()
# Program Persegi Panjang
def persegi_panjang():
    print ('=' * 35 )
    print ("Pilih Menu : ")
    print ("1. Luas Persegi Panjang")
    print ("2. Keliling Persegi Panjang")
    print ("3. Kembali Menu awal")
    print ('=' * 35)
    pilihan = input("Pilih Menu : ")
    if pilihan == '1':
        luas_persegi_panjang()
    elif pilihan == '2':
        keliling_persegi_panjang()
    elif pilihan == '3':
        main_menu()
    else:
        exit()
# Menghitung luas Persegi Panjang
def luas_persegi_panjang():
    print ('=' * 35)
    print ("Luas Persegi Panjang")
    print ("Luas = Pajang x Lebar")
    print ('=' * 35)
    p = int(input("Masukan Panjang Persegi Panjang : "))
    l = int(input("Masukan Lebar Persegi Panjang : "))
    print ('=' * 35)
    luas = p * l
    print (f"Luas Persegi Panjang adalah : {luas}")
    return persegi_panjang()
# Menghitung Keliling Persgi Panjang
def keliling_persegi_panjang():
    print ('=' * 35)
    print ("Keliling Persgi Panjang")
    print ("Keliling = 2 x (Panjang + Lebar)")
    p = int(input("Masukan Panjang Persegi Panjang : "))
    l = int(input("Masukan Lebar Persegi Panjang : "))
    print ('=' * 35)
    keliling = 2 * (p + l)
    print (f"Keliling Persegi Panjang adalah : {keliling}")
    return persegi_panjang()
# Program Segitiga
def segitiga():
    print ('=' * 35)
    print ("Luas Segitiga")
    print ("1/2 x alas x tinggi")
    a = int(input("Masukan alas Segitiga :  "))
    t = int(input("Masukan tinggi Segitiga : "))
    print ('=' * 35)
    luas = 0.5 * a * t
    print (f"Luas Segitiga adalah : {luas}")
    print ('=' * 35)
    return main_menu()
# Program Lingkaran
def lingkaran():
    print ('=' * 35)
    print ("Pilih Menu : ")
    print ("1. Luas Lingkaran")
    print ("2. Keliling Lingkaran")
    print ("3. Kembali Menu awal")
    print ('=' * 35)
    tanya = input("Pilih Menu : ")
    if tanya == '1':
        luas_lingkaran()
    elif tanya == '2':
        keliling_lingkaran()
    else:
        main_menu()
# Program Luas Lingkaran
def luas_lingkaran():
    print ('=' * 35)
    print ("Luas Lingkaran")
    print ("Luas = pi x (r x r)")
    jari = int(input("Masukan Nilai Jari - Jari Lingkaran : "))
    print ('=' * 35)
    luas = mt.pi * (jari * jari)
    print (f"Luas lingkaran adalah : {luas}")
    print ('=' * 35)
    return lingkaran()
# Program Keliling Lingkaran
def keliling_lingkaran():
    print ('=' * 35)
    print ("Keliling Lingkaran")
    print ("Keliling = 2 x pi x r")
    jari = int(input("Masukan Nilai Jari - Jari Lingkaran : "))
    print ('=' * 35)
    keliling = 2 * mt.pi * jari
    print (f"Keliling Lingkaran adalah : {keliling}")
    print ('=' * 35)
    return lingkaran()
# Program Belah Ketupat
def belah_ketupat():
    print ('=' * 35)
    print ("Luas Belah Ketupat")
    print ("Luas = 1/2 x d1 x d2")
    d1 = int(input("Masukan Diagonal 1 : "))
    d2 = int(input("Masukan Diagonal 2 : "))
    print ('=' * 35)
    luas = (d1 * d2) / 2
    print (f"Luas Belah Ketupat adalah : {luas}")
    print ('=' * 35)
    return main_menu()
# Main menu
if __name__ == "__main__":
    main_menu()