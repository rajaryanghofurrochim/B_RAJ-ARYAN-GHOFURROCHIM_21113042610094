print("\n=== 5-9. No Users ===")

# Dengan daftar yang berisi pengguna
usernames = ['admin', 'udin', 'rusdi', 'anton', 'reza']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Halo admin, selamat datang kembali di situs kami!")
        else:
            print(f"Halo {username.title()}, terima kasih telah mengunjungi website kami kembali.")
else:
    print("Kami perlu menemukan beberapa pengguna!")

# Setelah semua username dihapus
usernames = []
if usernames:
    for username in usernames:
        print(f"Halo {username.title()}!")
else:
    print("Kami perlu menemukan beberapa pengguna!")