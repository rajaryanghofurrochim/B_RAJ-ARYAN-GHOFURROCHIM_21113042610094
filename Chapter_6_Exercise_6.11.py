print("\n=== 6-11. Cities ===")
cities = {
    'jakarta': {
        'country': 'Indonesia',
        'population': 10_800_000,
        'fact': 'Ibu kota Indonesia saat ini.',
    },
    'tokyo': {
        'country': 'Jepang',
        'population': 14_000_000,
        'fact': 'Salah satu kota terbesar di dunia.',
    },
    'paris': {
        'country': 'Prancis',
        'population': 2_100_000,
        'fact': 'Terkenal dengan Menara Eiffel.',
    },
}

for city, info in cities.items():
    print(f"\n{city.title()}")
    print(f"  Negara: {info['country']}")
    print(f"  Populasi: {info['population']:,}")
    print(f"  Fakta: {info['fact']}")
