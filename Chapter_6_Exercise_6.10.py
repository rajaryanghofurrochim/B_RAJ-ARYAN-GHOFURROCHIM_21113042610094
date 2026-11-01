print("\n=== 6-10. Favorite Numbers ===")
favorite_numbers = {
    'budi': [7, 10],
    'siti': [1],
    'andi': [21, 99],
    'rina': [22, 20],
    'dewi': [5, 25, 67],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} menyukai angka:")
    for number in numbers:
        print(f"- {number}")