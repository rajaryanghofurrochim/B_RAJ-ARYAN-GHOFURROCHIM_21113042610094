# Shrinking guest list
guests = ['Raihan', 'Sendi', 'Akhdan', 'Ghiry']
print("Maaf, meja baru tidak datang tepat waktu. Hanya bisa mengundang 2 orang.")

while len(guests) > 2:
    dihapus = guests.pop()
    print(f"Maaf {dihapus}, saya tidak bisa mengundang Anda makan malam.")

for guest in guests:
    print(f"Halo {guest}, Anda masih diundang makan malam.")

del guests[0]
del guests[0]
print(guests)  # harus menampilkan list kosong: []