def latihan_7_5():
    prompt = "\nBerapa umur Anda? (ketik 'quit' untuk selesai) "

    while True:
        umur = input(prompt)
        if umur == 'quit':
            break

        umur = int(umur)
        if umur < 3:
            print("Tiket Anda gratis.")
        elif umur <= 12:
            print("Harga tiket Anda $10.")
        else:
            print("Harga tiket Anda $15.")