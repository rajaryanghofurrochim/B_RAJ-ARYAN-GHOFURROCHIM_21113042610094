print("\n=== 4-10. Slices ===")
cubes = [nilai ** 3 for nilai in range(1, 11)]
print("Tiga nilai pertama dari list:")
print(cubes[:3])

print("Tiga nilai tengah dari list:")
middle = len(cubes) // 2
print(cubes[middle - 1:middle + 2])

print("Tiga nilai terakhir dari list:")
print(cubes[-3:])