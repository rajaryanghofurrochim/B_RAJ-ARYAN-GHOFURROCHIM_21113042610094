# Kesamaan dan ketidaksamaan string
name = 'Raj'
print(name == 'Raj')        # True
print(name == 'Andi')        # False
print(name != 'Andi')        # True
print(name != 'Raj')        # False

# Metode lower()
print(name.lower() == 'Raj')    # True
print(name.lower() == 'raj')    # False

# Tes numerik: ==, !=, <, >, <=, >=
umur = 20
print(umur == 20)    # True
print(umur == 21)    # False
print(umur != 21)    # True
print(umur != 20)    # False
print(umur < 25)     # True
print(umur < 15)     # False
print(umur > 15)     # True
print(umur > 25)     # False
print(umur <= 20)    # True
print(umur <= 19)    # False
print(umur >= 20)    # True
print(umur >= 21)    # False

# And dan or
print(umur >= 18 and umur < 30)    # True
print(umur >= 18 and umur < 20)    # False
print(umur < 18 or umur == 20)     # True
print(umur < 18 or umur > 30)      # False

# Item ada di dalam list
fruits = ['Apel', 'Pisang', 'Alpukat']
print('Pisang' in fruits)        # True
print('Mangga' in fruits)        # False

# Item tidak ada di dalam list
print('Mangga' not in fruits)     # True
print('Apel' not in fruits)    # False