def deret_ganjil(n):
    if n <= 0:
        return 0
    else:
        return n + deret_ganjil(n - 2)

n = int(input("Masukkan nilai n: "))
print(f"Jumlah deret ganjil dari 1 + 3 + 7 + ... + {n} adalah {deret_ganjil(n)}")