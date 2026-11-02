# Masalah: Menggunakan Tab acak, ada kalimat yang sangat panjang, dan terlalu banyak baris kosong senggang.

my_favorite_foods = ['pizza', 'burger', 'sushi', 'martabak manis', 'ayam geprek premium dengan keju leleh ekstra pedas level sepuluh']

for food in my_favorite_foods:
	print(f"Saya sangat suka makan {food} terutama jika disajikan selagi masih hangat bersama teman-teman dekat.")

print("Semua makanan di atas adalah favorit saya!")

# Setelah diperbaiki sesuai pada PEP 8

my_favorite_foods = [
    'pizza', 'burger', 'sushi', 'martabak manis', 
    'ayam geprek premium'
]

for food in my_favorite_foods:
    # Menggunakan tepat 4 spasi untuk baris di bawah
    message = (
        f"Saya sangat suka makan {food} terutama jika "
        "disajikan selagi masih hangat."
    )
    print(message)

print("Semua makanan di atas adalah favorit saya!")