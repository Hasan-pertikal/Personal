def opFilter(opLen): #untuk memfilter apakah sebuah operasi ada dalam input user
    varO = 0
    for i in opLen:
        if i != 0:
            opLen[varO] = True 
        else:
            opLen[varO] = False
        varO += 1
    
def main():
    print("********Calculator Total********")
    angka = []
    operasi = []

    while True: #looping untuk input user
        try: #ngecek apakah user input ada error
            usernum_input: float = float(input("Masukkan angka: "))
            angka.append(usernum_input)

            userOp_input: str = input("Masukkan Operasi: ").lower() #input operasi hitung dan me-lowercase semua kata

            if userOp_input in ["+", "add", "tambahkan", "tambah", "ditambah", #filter operasi hitung
                                "-", "minus", "kurangi", "kurang", "dikurang", 
                                "x", "*", "times", "kali", "dikali", 
                                "/", "divided by", "dibagi", "bagi"]:    
                operasi.append(userOp_input)
            elif userOp_input in ["=", "equal", "sama", "sama dengan"]: #meghentikan looping
                break
            else:
                print("Masukkan Operasi yang Valid!")

                userOp_input: str = input("Masukkan Operasi: ").lower()

                if userOp_input in ["+", "add", "tambahkan", "tambah", "ditambah", #filter operasi hitung
                                    "-", "minus", "kurangi", "kurang", "dikurang", 
                                    "x", "*", "times", "kali", "dikali", 
                                    "/", "divided by", "dibagi", "bagi"]:    
                    operasi.append(userOp_input) #memasukkan operasi hitung dalam list
        except ValueError: #jika ada error
            print("!#### Masukkan angka dalam tipe integer (..., -2, -1 , 1, 2,...) atau Float (..., -2.1, -1.2 , 1.3, 2.4,... ) ####!")
            pass

    tambah, kurang, kali, bagi = [], [], [], [] #membuat list untuk setiap tipe operasi
    
    x = 0
    for i in operasi: #memfilter operasi
        if i in ["+", "add", "tambahkan", "tambah", "ditambah"]:
            tambah.append(x)
        elif i in ["-", "minus", "kurangi", "kurang", "dikurang"]:
            kurang.append(x)
        elif i in ["x", "*", "times", "kali", "dikali"]:
            kali.append(x)
        elif i in ["/", "divided by", "dibagi", "bagi"]:
            bagi.append(x)
        else:
            break
        x += 1
    opLen = [len(tambah), len(kurang), len(kali), len(bagi)]

    opFilter(opLen) 
    angka_range = len(angka)
    if opLen[2] == True or opLen[3] == True: #ngecek ada kali atau bagi
        tress = 0
        for i in range(angka_range):
            try:
                if i in kali and i == 0:
                    hasil_1 = angka[0] * angka[1]
                    angka[0] = hasil_1
                    angka.pop(1) #menghilangkan angka di index 1
                    tress -= 1
                elif i in bagi and i == 0:
                    hasil_1 = angka[0] / angka[1]
                    angka[0] = hasil_1 
                    angka.pop(1) #menghilangkan angka di index 1
                    tress -= 1
                elif i in kali:
                    hasil_1 = angka[tress] * angka[tress + 1]
                    angka[tress] = hasil_1
                    angka.pop(tress + 1) #menghilangkan angka pada index i + 1    
                    tress -= 1
                elif i in bagi: 
                    hasil_1 = angka[tress] / angka[tress + 1]
                    angka[tress] = hasil_1
                    angka.pop(tress + 1) #menghilangkan angka di index i + 1
                    tress -= 1
                
            except IndexError: #mengcek apakah ada error pada angka[i]
                if i in kali:
                    hasil_1 = angka[tress - 1] * angka[tress]
                    angka[tress - 1] = hasil_1
                    angka.pop(tress)
                    tress -= 1
                elif i in bagi:
                    hasil_1 = angka[tress - 1] / angka[tress]
                    angka[tress - 1] = hasil_1
                    angka.pop(tress)
                    tress -= 1
            tress += 1   
            print(angka)
    
    if opLen[0] == True or opLen[1] == True: #ngecek ada + atau -
        for i in range(angka_range):
            if i in tambah and i == 0:
                hasil_2 = angka[0] + angka[1]
                angka[0] = hasil_2
                angka.pop(1) #menghilangkan angka di index 1
            elif i in kurang and i == 0:
                hasil_2 = angka[0] - angka[1]
                angka[0] = hasil_2
                angka.pop(1) #menghilangkan angka di index 1
            elif i in tambah:
                hasil_2 = angka[0] + angka[1]
                angka[0] = hasil_2
                angka.pop(1) #menghilangkan angka di index 1
            elif i in kurang:
                hasil_2 = angka[0] - angka[1]
                angka[0] = hasil_2
                angka.pop(1) #menghilangkan angka di index 1

            print(angka)

    print(f"= {angka[0]}") #print hasil  
      
if __name__ == "__main__": #untuk melaksanakan program utama
    main()