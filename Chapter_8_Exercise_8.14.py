def make_car(manufacturer, model, **car_info):
    """Simpan informasi sebuah mobil dalam dictionary."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


print("\n=== 8-14. Cars ===")
car = make_car('bugatti', 'chiron', color='biru', tow_package=True)
print(car)