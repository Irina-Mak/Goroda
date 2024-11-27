from auto_py_to_exe.config import language_hint
from opencage.geocoder import OpenCageGeocode

key = 'b73167678a934117b8be7c5b2b6600e0'
def get_coordinates(city, key):

    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language = 'ru')

        if results:
            # Возвращает первый результат
            return results[0]['geometry']['lat'], results[0]['geometry']['lng']
        else:
            return "Город не найден"
    except Exception as e:
        return f"Общая ошибка: {e}"

# Пример использования
key = 'b73167678a934117b8be7c5b2b6600e0'
city = 'London'
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")
