def opFilter(opLen):
    varO = 0
    for i in opLen:
        if i != 0:
            opLen[varO] = True
        else:
            opLen[varO] = False
        varO += 1
    
def main():
    print("********Calculator********")
    angka = []
    operasi = []

    while True:
        try:
            usernum_input: float = float(input("Masukkan angka: "))
            angka.append(usernum_input)

            userOp_input: str = input("Masukkan Operasi: ").lower()

            if userOp_input in ["+", "add", "tambahkan", "tambah", 
                                "-", "minus", "kurangi", 
                                "x", "*", "times", "kali", 
                                "/", "divided by", "dibagi"]:    
                operasi.append(userOp_input)
            elif userOp_input in ["=", "equal", "sama dengan", "sama dengan"]:
                break
            else:
                print("Masukkan Operasi yang Valid!")

                userOp_input: str = input("Masukkan Operasi: ").lower()

                if userOp_input in ["+", "add", "tambahkan", "tambah", "ditambah", 
                                    "-", "minus", "kurangi", "kurang", "dikurang", 
                                    "x", "*", "times", "kali", "dikali", 
                                    "/", "divided by", "dibagi", "bagi"]:    
                    operasi.append(userOp_input)
        except ValueError:
            print("!#### Masukkan angka dalam tipe integer (..., -2, -1 , 1, 2,...) atau Float (..., -2.1, -1.2 , 1.3, 2.4,... ) ####!")
            pass

    a, b, c, d = [], [], [], []
    
    x = 0
    for i in operasi:
        if i in ["+", "add", "tambahkan", "tambah", "ditambah"]:
            a.append(x)
        elif i in ["-", "minus", "kurangi", "kurang", "dikurang"]:
            b.append(x)
        elif i in ["x", "*", "times", "kali", "dikali"]:
            c.append(x)
        elif i in ["/", "divided by", "dibagi", "bagi"]:
            d.append(x)
        else:
            break
        x += 1
    opLen = [len(a), len(b), len(c), len(d)]
    opFilter(opLen) #mengfilter operasi
    
    if opLen[2] == True or opLen[3] == True: #ngecek ada kali atau bagi
        for i in range(len(angka) + 1):
            try:
                if i in c and i == 0:
                    hasil_1 = angka[0] * angka[1]
                    angka[0] = hasil_1
                    angka.pop(1) #menghilangkan angka di index 1
                elif i in d and i == 0:
                    hasil_1 = angka[0] / angka[1]
                    angka[0] = hasil_1 
                    angka.pop(1) #menghilangkan angka di index 1
                elif i in c:
                    hasil_1 = angka[i] * angka[i + 1]
                    angka[i] = hasil_1
                    angka.pop(i + 1) #menghilangkan angka di index 1
                    
                elif i in d: 
                    hasil_1 = angka[i] / angka[i + 1]
                    angka[i] = hasil_1
                    angka.pop(i + 1) #menghilangkan angka di index 1
            except IndexError:
                if i in c:
                    hasil_1 = angka[i - 1] * angka[i]
                    angka[i - 1] = hasil_1
                    angka.pop(i)
                elif i in d:
                    hasil_1 = angka[i - 1] / angka[i]
                    angka[i - 1] = hasil_1
                    angka.pop(i)
    
    if opLen[0] == True or opLen[1] == True: #ngecek ada + atau -
        for i in range (len(angka)):
            if i in a and i == 0:
                hasil_2 = angka[0] + angka[1]
                angka[0] = hasil_2
                angka.pop(1)
            elif i in b and i == 0:
                hasil_2 = angka[0] - angka[1]
                angka[0] = hasil_2
                angka.pop(1)
            elif i in a:
                hasil_2 = angka[0] + angka[1]
                angka[0] = hasil_2
                angka.pop(1)
            elif i in b:
                hasil_2 = angka[0] - angka[1]
                angka[0] = hasil_2
                angka.pop(1)
    print(f"= {angka[0]}")       
if __name__ == "__main__":
    main()