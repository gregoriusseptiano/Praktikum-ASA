# Mohon untuk Mengisi identitas berikut sebelum mengerjakan
# Nama : Gregorius Septiano Ariadi 
# NIM  : 24060124120026
# Lab  : E1

# Input nilai awal
inputAwal = list(map(int, input().split()))
N = inputAwal[0]
Y = inputAwal[1] + 1
X = inputAwal[2]

# Input kondisi jalan
lintasan = list(map(int, input().split()))
mutiara = 0          # jumlah mutiara yang terkumpul
posisi = 0           # posisi sekarang
masihJalan = True    # status bisa lanjut atau tidak

while posisi < N and masihJalan:
    isi = lintasan[posisi]
    # Ambil efek dari isi jalan
    if isi < 7:
        Y += isi
    elif isi == 7:
        mutiara += 1

    # Cek tenaga sebelum jalan
    if Y == 0:
        if mutiara > 0:
            mutiara -= 1
            Y += 7
        else:
            masihJalan = False

    # Kalau masih bisa jalan, lanjut
    if masihJalan:
        Y -= 1
        posisi += 1

# Cek hasil akhir
if posisi == N and mutiara >= X:
    print(mutiara)
else:
    print(-1)
    
#Gimana, Aman ?
#Tinggalkan saran di sini : 