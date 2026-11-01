guests = ['Raihan', 'Sendi', 'Akhdan']
print("Kabar baik! Saya menemukan meja makan yang lebih besar.")

guests.insert(0, 'Ghiry')            # awal
guests.insert(len(guests) // 2, 'Hafizh')  # tengah
guests.append('Yohanes')            # akhir

for i in range(len(guests)):
    print(f"Halo {guests[i]}, saya mengundang Anda makan malam.")