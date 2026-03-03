n = int(input())
posisi = [-1] * n

def aman(baris, kolom):
    for i in range(baris):
        if posisi[i] == kolom:
            return False
        if abs(posisi[i] - kolom) == abs(i - baris):
            return False
    return True

def taruh_ratu(baris):
    if baris == n:
        return True
    for kolom in range(n):
        if aman(baris, kolom):
            posisi[baris] = kolom
            if taruh_ratu(baris + 1):
                return True
            posisi[baris] = -1
    return False
if taruh_ratu(0):
    for i in range(n):
        baris = ""
        for j in range(n):
            if posisi[i] == j:
                baris += "Q"
            else:
                baris += "."
        print(baris)
else:
    print("Kerajaan tidak dapat dilindungi!")