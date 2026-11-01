print("\n=== 5-10. Checking Usernames ===")

pengguna_saat_ini = ['amba', 'Udin', 'rusdi', 'Anton', 'reza']
pengguna_baru = ['amba', 'Rina', 'siti', 'Dewi', 'eko']

# Membuat daftar pengguna saat ini dalam huruf kecil
pengguna_saat_ini_lower = [pengguna.lower() for pengguna in pengguna_saat_ini]

for nama in pengguna_baru:
    if nama.lower() in pengguna_saat_ini_lower:
        print(f"'{nama}' sudah dipakai. Silakan masukkan username lain.")
    else:
        print(f"Username '{nama}' tersedia.")