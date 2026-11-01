# Changing guest list
guests = ['B.J. Habibie', 'Ki Hadjar Dewantara', 'Kartini']
tidak_bisa_hadir = guests[2]
print(f"{tidak_bisa_hadir} tidak bisa hadir di acara makan malam.")

guests[2] = 'RM Said'  # ganti dengan tamu baru

for i in range(len(guests)):
    print(f"Halo {guests[2]}, saya mengundang Anda makan malam.")