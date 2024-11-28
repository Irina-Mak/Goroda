from locale import currency
from tkinter import *
from opencage.geocoder import OpenCageGeocode
import webbrowser
import requests




# Функция для очистки поля ввода
def show_clear():
    entry.delete(0,END)
    label.config(text = "")
    koordinaty.config(text=f"Координаты города :")


def get_coordinates(city, key):
    global lat, lon
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')

        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components'].get('country', 'Страна не определена')
            region = results[0]['components'].get('state', 'Регион не определен')
            valuta = results[0]['annotations']['currency']['name']


            # Получаем URL для OpenStreetMap
            osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}"



            return {
                "coordinates": f"Широта: {lat}, Долгота: {lon}\nСтрана: {country}\nРегион: {region}\nВалюта:{valuta}",
                "map_url": osm_url
            }
        else:
            return {"coordinates": "Город не найден", "map_url": None}
    except Exception as e:
        return {"coordinates": f"Ошибка: {e}", "map_url": None}

def show_coordinates(event=None):
    city = entry.get()
    result = get_coordinates(city, key)
    label.config(text=result["coordinates"])
    koordinaty.config(text=f"Координаты города {city}:")
    # Сохраняем URL в глобальной переменной для доступа из другой функции
    global map_url
    map_url = result["map_url"]

def show_map():
    if map_url:
        webbrowser.open(map_url)

# Интерфейс
window = Tk()
window.title("Поиск координат города")
window.geometry('360x400')

key = 'b73167678a934117b8be7c5b2b6600e0'
map_url = None

# Элементы интерфейса
entry = Entry()
entry.pack()
entry.bind("<Return>", show_coordinates)

button = Button(text="Поиск координат", command=show_coordinates)
button.pack()



koordinaty = Label(text="Кординаты города ")
koordinaty.pack()


label = Label(text="Введите город и нажмите Поиск")
label.pack()

map_button = Button(text="Показать карту", command=show_map)
map_button.pack()


clear_button = Button(text="Очистить", command=show_clear)
clear_button.pack()


window.mainloop()


