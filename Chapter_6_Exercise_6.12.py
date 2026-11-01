print("\n=== 6-12. Extensions ===")
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
    }
}
languages = {
    'jakarta': 'Bahasa Indonesia',
    'tokyo': 'Bahasa Jepang',
    'paris': 'Bahasa Prancis',
}

for city, language in languages.items():
    cities[city]['language'] = language

for city, info in cities.items():
    print(f"\n{city.title()}, {info['country']}")
    print(f"  Bahasa: {info.get('language', 'Tidak tersedia')}")
    print(f"  Populasi: sekitar {info['population']:,} jiwa")
    print(f"  Fakta: {info['fact']}")