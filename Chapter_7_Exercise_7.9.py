def latihan_7_9():
    sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'ayam',
                       'pastrami', 'telur']
    finished_sandwiches = []

    print("Mohon maaf, pastrami di deli ini sudah habis.")

    # Hapus semua 'pastrami' dari daftar pesanan
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

    while sandwich_orders:
        current_sandwich = sandwich_orders.pop(0)
        print(f"Saya sedang membuat sandwich {current_sandwich} Anda.")
        finished_sandwiches.append(current_sandwich)

    print("\nSandwich yang selesai dibuat:")
    for sandwich in finished_sandwiches:
        print(f"- Sandwich {sandwich}")