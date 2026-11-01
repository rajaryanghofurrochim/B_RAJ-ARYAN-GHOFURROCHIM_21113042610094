print("\n=== 6-6. Polling ===")
bahasa_favorit = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people_to_poll = ['jen', 'budi', 'sarah', 'siti', 'phil', 'edward']

for person_name in people_to_poll:
    if person_name in bahasa_favorit:
        print(f"Terima kasih {person_name.title()}, sudah mengisi polling!")
    else:
        print(f"{person_name.title()}, silakan ikut polling bahasa "
              f"pemrograman favorit!")