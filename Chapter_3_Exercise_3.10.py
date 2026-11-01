# Every function

mountains = ['Semeru', 'Rinjani', 'Merapi', 'Bromo']
print("Awal:", mountains)

print("Elemen pertama:", mountains[0])
print("Elemen terakhir:", mountains[-1])

mountains[0] = 'Kerinci'            # modifikasi
print("Setelah diubah:", mountains)

mountains.append('Slamet')          # tambah di akhir
mountains.insert(1, 'Gede')         # sisip di indeks 1
print("Setelah tambah:", mountains)

mountains.remove('Bromo')           # hapus berdasarkan nilai
print("Setelah remove('Bromo'):", mountains)

terakhir = mountains.pop()          # hapus & ambil elemen terakhir
print(f"pop() mengambil: {terakhir} -> {mountains}")

del mountains[0]                    # hapus berdasarkan indeks
print("Setelah del mountains[0]:", mountains)

mountains.sort()
print("sort():", mountains)

mountains.sort(reverse=True)
print("sort(reverse=True):", mountains)

print("sorted():", sorted(mountains))

mountains.reverse()
print("reverse():", mountains)

print("Panjang list (len):", len(mountains))
