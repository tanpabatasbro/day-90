print("""
      ========= WELCOME TO ========
      <===>>> KC BOOK STORE <<<===>
      
      _____________________
      | Kode | Jenis Buku |
      |-------------------|
      |__K___|_Komik______|
      |__N___|_Novel______|
      |______|____________|
      """)

nama = input("Nama: ")
alamat = input("Alamat : ")
kontak = int(input("No Handphone :"))
kodeBuku = input("Kode Buku : ")

if kodeBuku == "K":
    print("""
          Komik                  | Harga
          1. Komik Naruto        | RP. 90.000,00
          2. Komik Black Clover  | RP. 85.000,00
          3. Komik Boboiboy      | RP. 80.000,00
          """)
    pilih = int(input("Mau Komik NO Berapa? : "))
    jumlah  = int(input("Mau Beli Berapa? : "))
    if pilih == 1:
        jenisBuku = "Komik Naruto"
        hargaKNaruto = 90_000
        totalHarga = hargaKNaruto * jumlah
    elif pilih  == 2:
        jenisBuku = "Komik Black Clover"
        hargaKBlackClover = 85_000
        totalHarga = hargaKBlackClover * jumlah
    elif pilih == 3:
        jenisBuku = "Komik Boboiboy"
        hargaKBoboiboy = 80_000
        totalHarga =  hargaKBoboiboy * jumlah
    else:
        print("KOMIK NOT  FOUND")
        
    print(f"\nNama : {nama}")
    print(f"Alamat : {alamat}")
    print(f"No Handphone : {kontak}")
    print(f"Jenis Buku : {jenisBuku}")
    print(f"jumlah Buku : {jumlah}")
    print(f"Harga : RP.{totalHarga},00")
                
elif kodeBuku == "N":
    print("""
          Novel                     | Harga
          1. Dilan 1990             | RP. 65.000,00
          2. Layangan Putus         | RP. 75.000,00
          3. Ronggeng Dukuh Paruk   | RP. 70.000,00
          """)
    pilih = int(input("Mau Novel NO Berapa? : "))
    jumlah = int(input("Mau Beli Berapa? : "))
    
    if pilih == 1:
        jenisBuku = "Novel Dilan 1990"
        hargaNDilan = 65_000
        totalHarga = hargaNDilan * jumlah  
    elif pilih == 2:
        jenisBuku = "Novel Layangan Putus"
        hargaNLayanganPutus = 75_000
        totalHarga = hargaNLayanganPutus * jumlah
    elif pilih == 3:
        jenisBuku = "Novel Dukuh Paruk"
        hargaNDukuhParuk = 70_000
        totalHarga = hargaNDukuhParuk * jumlah
    else:
        print("NOVEL NOT FOUND")
        
    print(f"\nNama : {nama}")
    print(f"Alamat : {alamat}")
    print(f"No Handphone : {kontak}")
    print(f"Jenis Buku : {jenisBuku}")
    print(f"jumlah Buku : {jumlah}")
    print(f"Harga : RP.{totalHarga},00")
