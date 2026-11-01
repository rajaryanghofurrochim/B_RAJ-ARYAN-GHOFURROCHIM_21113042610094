print("\n=== 6-9. Favorite Places ===")
favorite_places = {
    'budi': ['Bali', 'Bromo', 'Raja Ampat'],
    'siti': ['Yogyakarta', 'Surakarta'],
    'andi': ['Lombok', 'Labuan Bajo', 'Toba'],
}

for name, places in favorite_places.items():
    print(f"\nTempat favorit {name.title()}:")
    for place in places:
        print(f"- {place}")