# Seeing the world
places = ['Yogyakarta', 'Bandung', 'Bali', 'Jakarta', 'Solo']

print("Urutan asli:", places)
print("sorted() abjad:", sorted(places))
print("Masih urutan asli:", places)

print("sorted() terbalik:", sorted(places, reverse=True))
print("Masih urutan asli:", places)

places.reverse()
print("Setelah reverse():", places)

places.reverse()
print("Reverse lagi (kembali asli):", places)

places.sort()
print("Setelah sort():", places)

places.sort(reverse=True)
print("Setelah sort(reverse=True):", places)