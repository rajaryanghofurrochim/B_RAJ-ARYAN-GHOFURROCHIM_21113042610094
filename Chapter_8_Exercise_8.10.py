def send_messages(messages, sent_messages):
    """Cetak setiap pesan, lalu pindahkan ke daftar sent_messages."""
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim pesan: {current_message}")
        sent_messages.append(current_message)


print("\n=== 8-10. Sending Messages ===")
pesan = ["Halo, apa kabar?", "Jangan lupa rapat jam 10.", "Terima kasih!"]
sent_messages = []

send_messages(pesan, sent_messages)
print("\nDaftar pesan asli :", pesan)
print("Daftar pesan terkirim:", sent_messages)