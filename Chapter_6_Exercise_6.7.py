print("\n=== 6-7. People ===")
person_1 = {
    'first_name': 'Raj',
    'last_name': 'Aryan',
    'age': 19,
    'city': 'Surakarta',
}
person_2 = {
    'first_name': 'Siti',
    'last_name': 'Rahayu',
    'age': 22,
    'city': 'Yogyakarta',
}
person_3 = {
    'first_name': 'Andi',
    'last_name': 'Wijaya',
    'age': 30,
    'city': 'Semarang',
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name}, umur {person['age']} tahun, tinggal di "
          f"{person['city']}.")