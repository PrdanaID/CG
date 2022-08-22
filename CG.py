import os
os.system("clear")
U = True

while (U==True) :
    os.system("clear")

    # Head
    print(30*"=")
    print("=  KALKULATOR GEAR SEDERHANA =")
    print(30*"=")
    print("            Spur Gear")
    print("")
    print("Pilih Opsi :")
    print("|1| Menghitung Diameter Tusuk")
    print("|2| Menghitung Modul")
    print("|3| Perancangan roda gigi lurus")
    print("|4| Rangkaian rumus")
    print("|5| Nama bagian roda gigi")
    print("")
    a = int(input("Masukkan pilihan opsi : "))

    # Opsi 1
    if a==1:
        os.system("clear")
        print("*MENGHITUNG DIAMETER TUSUK*")
        A1= int(input("Masukkan Z : "))
        A2= int(input("Masukkan M : "))

        H = A1 * A2
        print("Maka diameter tusuk nya =",H)

    # Opsi 2
    if a==2:
        os.system("clear")
        
        A3= int(input("Masukkan diameter luar : "))
        A4= int(input("Masukkan jumlah gigi   : "))

        H = A3 / (A4+2)
        print("Maka (M)Modul nya =",H)
    
    # Opsi 3
    if a==3:
        os.system("clear")
        print ("*PERENCANAAN PEMBUATAN RODA GIGI LURUS*")
        print("")
        A5= int(input("Pisau modul : "))
        A6= int(input("Jumlah gigi : "))
        print("")
        print("Perencanaan:")

        A = A6*A5
        print("|Dt|",A,"mm")

        B = 1*A5
        print("|ha|",B,"mm")

        C = 1.2*A5
        print("|hf|",C,"mm")

        D = B+C
        print("|h |",D,"mm")

        E = A-(2*C)
        print("|Df|",E,"mm")

        F = A+(2*B)
        print("|Dk|",F,"mm")

        G = 10*A5
        print("|b |",G,"mm")

        H = 40/A6
        print("|Nc|",H,"mm")
        print("Jadi, kepala pembagi diputar",H,"x putaran untuk memindah dari gigi 1 ke gigi lainnya")
        
    # Opsi 4 (BUTUH KROSCEK)
    if a==4:
        os.system("clear")
        print("* RUMUS-RUMUS *")
        print("|Dt| Z.M")
        print("|ha| 1.M")
        print("|hf| 1,2.M")
        print("|Df| Dt-2hf")
        print("|Dk| Dt+2ha")
        print("|b | -untuk otomotif (6 s/d 8).M")
        print("     -untuk pemesinan (9 s/d 12).M")
        print("|h | ha+hf")
        print("|Nc| 40:Z")
        print("|M | D:Z")
        print("|Z | D:M")
        print("|D | Z.M")
        print("|T | 3,14.M")

    # Opsi 5
    if a==5:
        os.system("clear")
        print("* Nama bagian roda gigi *")
        print("")
        print("|Dk| Diameter kepala")
        print("|Dt| Diameter Tusuk")
        print("|Df| Diameter kaki")
        print("|ha| Tinggi kepala gigi")
        print("|hf| Tinggi kaki gigi")
        print("|b | Tebal gigi")
        print("|m | Modul")
        print("|T | Jarak pitch")
        print("|D | Diameter")
        print("|h | Tinggi kaki")

    #PENGULANGAN
    print (" ")
    l = input('Lagi? (Y/n) : ')
    if (l=='n'):
        U = False
        print("Program dalam proses pengembangan,Jika ada kritik dan saran dipersilakan")
        print("Thanks!")
        print(" ")