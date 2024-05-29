def prima(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

bilangan = int(input("Masukkan bilangan: "))
if prima(bilangan):
    print(f"{bilangan} adalah bilangan prima.")
else:
    print(f"{bilangan} bukan bilangan prima.")