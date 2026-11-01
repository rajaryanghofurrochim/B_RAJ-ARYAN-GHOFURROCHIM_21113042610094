print("=== 6-5. Rivers ===")
sungai = {
    'nil': 'mesir',
    'amazon': 'brasil',
    'citarum': 'indonesia',
}

for river, country in sungai.items():
    print(f"Sungai {river.title()} mengalir melalui {country.title()}.")

print("\nSungai yang ada dalam kamus:")
for river in sungai.keys():
    print(f"- {river.title()}")

print("\nNegara yang ada dalam kamus:")
for country in sungai.values():
    print(f"- {country.title()}")