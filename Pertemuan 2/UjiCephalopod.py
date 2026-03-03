kalimat = input()

def cekXY(teksInput, jumlahXY):
    if len(teksInput) < 2 and jumlahXY == 0:
        print(False)
    else:
        potong = teksInput[0:2]
        if potong == "XY":
            jumlahXY += 1
        if len(teksInput) == 1:
            print(jumlahXY % 2 == 0)
        else:
            cekXY(teksInput[1:], jumlahXY)

cekXY(kalimat, 0)