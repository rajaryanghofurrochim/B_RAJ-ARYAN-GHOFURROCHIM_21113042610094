def latihan_7_4():
    prompt = "\nMasukkan topping pizza (ketik 'quit' untuk selesai): "

    topping = ""
    while topping != 'quit':
        topping = input(prompt)
        if topping != 'quit':
            print(f"Baik, topping {topping} akan ditambahkan ke pizza Anda.")