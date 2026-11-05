kunci_akses = "statbis2026"

while True:
    input_sandi = input("Masukkan password: ")

    if input_sandi == kunci_akses:
        print("Login Berhasil, Selamat Datang!")
        break
    else:
        print("Password salah, silakan coba lagi!")