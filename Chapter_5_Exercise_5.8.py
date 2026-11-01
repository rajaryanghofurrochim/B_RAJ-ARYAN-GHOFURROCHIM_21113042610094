print("\n=== 5-8. Hello Admin ===")
usernames = ['admin', 'udin', 'rusdi', 'anton', 'reza']

for username in usernames:
    if username == 'admin':
        print("Halo admin, selamat datang kembali di situs kami!")
    else:
        print(f"Halo {username.title()}, terima kasih telah mengunjungi website kami kembali.")