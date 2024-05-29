def palindrom(s):
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            return palindrom(s[1:-1])
        else:
            return False

kalimat = input("Masukkan kalimat: ")
if palindrom(kalimat):
    print(f"{kalimat} adalah palindrom.")
else:
    print(f"{kalimat} bukan palindrom.")