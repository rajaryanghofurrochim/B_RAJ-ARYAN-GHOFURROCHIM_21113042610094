def make_sandwich(*items):
    """Ringkas bahan-bahan sandwich yang dipesan."""
    print("\nSandwich Anda dibuat dengan bahan:")
    for item in items:
        print(f"- {item}")


print("\n=== 8-12. Sandwiches ===")
make_sandwich('roti gandum', 'keju')
make_sandwich('roti putih', 'telur', 'tomat', 'selada')
make_sandwich('roti gandum', 'ayam', 'keju', 'selada', 'saus mayonaise')