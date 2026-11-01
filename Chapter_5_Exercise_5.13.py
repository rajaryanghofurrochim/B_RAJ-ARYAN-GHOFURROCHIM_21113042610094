# Program belanja dengan metode diskon

total_belanja = 150000
is_member = True

if total_belanja >= 100000 and is_member == True:
    total_akhir = total_belanja * 0.90  # Diskon 10%
    print(f"Selamat! Anda dapat diskon 10%. Total bayar: Rp{total_akhir}")
    print("Bonus: Gratis 1 botol minuman dingin!")
elif total_belanja >= 100000 and is_member == False:
    total_akhir = total_belanja * 0.95  # Diskon 5%
    print(f"Anda dapat diskon 5%. Total bayar: Rp{total_akhir}")
else:
    print(f"Total bayar: Rp{total_belanja}. (Dapatkan diskon dengan belanja minimal Rp100.000)")