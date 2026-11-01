def city_country(city, country):
    """Kembalikan teks berformat 'Kota, Negara'."""
    return f"{city.title()}, {country.title()}"


print("\n=== 8-6. City Names ===")
print(city_country('madrid', 'spanyol'))
print(city_country('jakarta', 'indonesia'))
print(city_country('tokyo', 'jepang'))