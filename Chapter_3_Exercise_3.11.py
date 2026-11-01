# Intentional Error

motor = ['honda', 'yamaha', 'suzuki']
try:
    print(motor[3])
except IndexError as e:
    print(f"Terjadi error: {e}")
    print(f"Panjang list = {len(motor)}, indeks valid: 0 sampai {len(motor) - 1}")