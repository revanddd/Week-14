def jumlah_digit(n):
    if n < 10:
        return n
    else:
        return n % 10 + jumlah_digit(n // 10)

bilangan = int(input("Masukkan bilangan: "))
print(f"Jumlah digit dari {bilangan} adalah {jumlah_digit(bilangan)}")