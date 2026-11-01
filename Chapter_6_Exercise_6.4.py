print("\n=== 6-4. Glossary 2 ===")
glossary = {
    'variable': "Nama yang menyimpan sebuah nilai.",
    'function': "Blok kode bernama yang bisa dipanggil berulang kali.",
    'boolean': "Nilai yang hanya bisa True atau False.",
    'index': "Posisi sebuah item di dalam list, dimulai dari 0.",
    'comment': "Catatan dalam kode yang diabaikan oleh Python."
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")