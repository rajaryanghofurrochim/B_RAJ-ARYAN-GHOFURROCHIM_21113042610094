def describe_city(city, country='Indonesia'):
    """Tampilkan kalimat sederhana tentang sebuah kota."""
    print(f"{city.title()} berada di {country.title()}.")


print("\n=== 8-5. Cities ===")
describe_city('surakarta')
describe_city('bandung')
describe_city('berlin', 'jerman')