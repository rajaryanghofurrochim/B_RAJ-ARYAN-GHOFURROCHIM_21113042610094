print("\n=== 6-8. Pets ===")
pet_1 = {'animal': 'kucing', 'owner': 'Budi'}
pet_2 = {'animal': 'anjing', 'owner': 'Siti'}
pet_3 = {'animal': 'kelinci', 'owner': 'Andi'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"{pet['owner']} memelihara seekor {pet['animal']}.")