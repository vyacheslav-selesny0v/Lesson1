dct = {"city": "Москва", "temperature": "20"}

print(dct.get('country', 'такого ключа нет'))

print(dct.get('country', 'Россия'))

dct['date'] = '27.05.2019'

print(len(dct))