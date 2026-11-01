def latihan_7_10():
    responses = {}
    polling_active = True

    while polling_active:
        name = input("\nSiapa nama Anda? ")
        place = input("Jika Anda bisa mengunjungi satu tempat di dunia, "
                      "ke mana Anda akan pergi? ")

        responses[name] = place

        repeat = input("Apakah ada orang lain yang ingin menjawab? "
                       "(ya/tidak) ")
        if repeat.lower() != 'ya':
            polling_active = False

    print("\n--- Hasil Polling ---")
    for name, place in responses.items():
        print(f"{name.title()} ingin mengunjungi {place.title()}.")