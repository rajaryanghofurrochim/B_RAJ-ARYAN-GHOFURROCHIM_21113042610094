def latihan_7_6():
    # Versi 1: tes kondisional langsung di dalam while
    print("--- Versi 1: tes kondisional di while ---")
    topping = ""
    while topping != 'quit':
        topping = input("Topping pizza (ketik 'quit' untuk selesai): ")
        if topping != 'quit':
            print(f"Topping {topping} ditambahkan.")

    # Versi 2: variabel 'active' sebagai penanda
    print("\n--- Versi 2: variabel active ---")
    active = True
    while active:
        topping = input("Topping pizza (ketik 'quit' untuk selesai): ")
        if topping == 'quit':
            active = False
        else:
            print(f"Topping {topping} ditambahkan.")

    # Versi 3: pernyataan break
    print("\n--- Versi 3: pernyataan break ---")
    while True:
        topping = input("Topping pizza (ketik 'quit' untuk selesai): ")
        if topping == 'quit':
            break
        print(f"Topping {topping} ditambahkan.")