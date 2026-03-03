n = int(input().strip())
A = input().strip()
B = input().strip()

# Jika sudah sama dari awal, tidak boleh (harus tepat satu pembalikan)
if A == B:
    print("Wah, tidak bisa :(")
else:
    l = 0
    while l < n and A[l] == B[l]:
        l += 1

    r = n - 1
    while r >= 0 and A[r] == B[r]:
        r -= 1

    # Balik substring B dari l sampai r
    B_balik = B[:l] + B[l:r+1][::-1] + B[r+1:]

    if B_balik == A:
        print("Tentu saja bisa!")
    else:
        print("Wah, tidak bisa :(")
