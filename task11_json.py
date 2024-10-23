import requests
import re


def get_num_temp(city):
    temp_str = re.search(r'-?\d+(?:\.\d+)?', city['Температура воздуха'])
    if temp_str:
        return int(temp_str.group())
    return -100


response = requests.get(url='https://parsinger.ru/3.4/1/json_weather.json')
weather_towns = response.json()

sort_weather_towns = sorted(weather_towns, key=lambda city: get_num_temp(city))
print(sort_weather_towns[0]['Дата'])

# URL = "https://parsinger.ru/3.4/1/json_weather.json"
# # Подсмотрел, там список словарей
# lst = requests.get(URL).json()
# # Сортировка списка по значению ключа словаря 'Температура воздуха'
# # Если что,[:-2] -это чтобы отсечь последние два знака(°C)
# sorted_lst = sorted(lst, key=lambda x: float(x['Температура воздуха'][:-2]))
# # Печать значения по ключу 'Дата' для словаря с самой низкой температурой
# print(sorted_lst[0]['Дата'])