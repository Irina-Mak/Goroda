from opencage.geocoder import OpenCageGeocode

key = 'b73167678a934117b8be7c5b2b6600e0'
def get_coordinates(city, key):
    """ Получает координаты города, используя библиотеку OpenCage. """
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city)

        if results:
            # Возвращает первый результат
            return results[0]['geometry']['lat'], results[0]['geometry']['lng']
        else:
            return "Город не найден"
    except Exception as e:
        return f"Общая ошибка: {e}"

# Пример использования
key = '97c595bec990457d975c12c16a4ec4a7'
city = 'Москва'
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")
