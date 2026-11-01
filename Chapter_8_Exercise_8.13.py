def build_profile(first, last, **user_info):
    """Bangun dictionary berisi semua yang kita ketahui tentang pengguna."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


print("\n=== 8-13. User Profile ===")
profile = build_profile('Raj', 'Aryan',
                        location='surakarta',
                        field='teknik industri',
                        hobby='kreasi benda')
print(profile)
