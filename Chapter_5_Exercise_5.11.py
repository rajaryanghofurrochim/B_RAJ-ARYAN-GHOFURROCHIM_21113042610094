print("\n=== 5-11. Ordinal Numbers ===")
nomor = list(range(1, 25))

for number in nomor:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
