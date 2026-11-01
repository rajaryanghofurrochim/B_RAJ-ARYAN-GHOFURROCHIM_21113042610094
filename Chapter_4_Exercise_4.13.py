print("\n=== 4-13. Buffet ===")
buffet = ['nasi', 'ayam goreng', 'kentang goreng', 'salad', 'sup ikan']

print("Menu awal:")
for makanan in buffet:
    print(makanan)

# Mengubah satu makanan
try:
    buffet[0] = 'roti'
except TypeError as error:
    print(f"\nPython menolak perubahan: {error}")

# Restoran mengganti dua makanan
buffet = ['nasi', 'ikan goreng', 'kentang goreng', 'salad', 'sup jamur']

print("\nMenu baru:")
for makanan in buffet:
    print(makanan)