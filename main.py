# Задание 1. Определить, у которого из персонажей наибольший intelligence
import requests
# Исходные данные: имена супергероев
int_by_names = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}


# Набить вышеуказанный словарь значениями из загруженного словаря
def load_intelligence(superheroes, resp_dict):
    for name, intel in superheroes.items():
        if resp_dict['name'] == name:
            superheroes[name] = resp_dict['powerstats']['intelligence']


# Определить умнейшего
def define_smartest(superheroes):
    return max(superheroes, key=superheroes.get)


# Выкачиваем JSON
url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url=url).json()
# получили список с вложенными словарями, перебираем
for stats in resp:
    load_intelligence(int_by_names, stats)

print(f'Умнейший: {define_smartest(int_by_names)}')
