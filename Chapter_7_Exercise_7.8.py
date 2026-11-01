def latihan_7_8():
    sandwich_orders = ['tuna', 'ayam', 'telur', 'keju']
    finished_sandwiches = []

    while sandwich_orders:
        current_sandwich = sandwich_orders.pop(0)
        print(f"Saya sedang membuat sandwich {current_sandwich} Anda.")
        finished_sandwiches.append(current_sandwich)

    print("\nSemua sandwich sudah selesai dibuat:")
    for sandwich in finished_sandwiches:
        print(f"- Sandwich {sandwich}")