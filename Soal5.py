def kombinasi(n, r):
    if r > n:
        return 0
    elif r == 0 or r == n:
        return 1
    else:
        return kombinasi(n - 1, r - 1) + kombinasi(n - 1, r)

n = int(input("Masukkan bilangan pertama: "))
r = int(input("Masukkan bilangan kedua: "))
print(f"Kombinasi {n} dengan {r} adalah {kombinasi(n, r)}")