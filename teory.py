# None это ничего
# a , b = b , a поменять значения местами
# ord посмотреть id символа
# chr посмотреть символ под id
# list.remove('something') удалить под названием
# del list[index] удалить по индексу
# a = [x, for x in range(number) условие если есть]
# x = tuple(something)
# Словари # dict
# {Ключ: значение,}
#d = {"house": "дом", "road": "дopoгa"}
#print(d["house"]) # "дом"
#d["new_key"] = "new_value" # добавить новые ключ:значение
#d["road"] = "путь" # заменить
#del d["house"] # удалить
#from datetime import *

# Время сейчас now = datetime.now()
# Получить из объекта времени отдельные типы времени
# print(now.hour, now.minute) # часы, минуты

# Количество секунд с начала цифр века seconds = datetime.timestamp(now)

# Количество дней с 1/1/1 (начало нашей эры) days = datetime.toordinal(now)

# Изменить атрибуты datetime now.replace(year=2000, day=1)
# Создать объект времени, в котором будет храниться 3 часа three_hour = timedelta(hours=3)

# Вычитает из объекта времени "now" 3 часа edit_time = now - three_hour

# Создать фиксированную дату 
# fixdate = datetime (year=1, month=1, day=1) a = now fixdate
# Форматирование объекта даты в строку, с гибкими найстроками s = datetime.strftime(
#       now, "%d.%m.%Y | %H:%M:%S"
#)

# Форматирование строки в объект t = datetime.strptime(
#       s, "%d.%m.%Y | %H:%M:%S"
#)

#s2 = "0001"
#t2 = datetime.strptime(
#s2, "%Y")
#"git add .; git commit -a -m 'commit'; git push; clear; python -u"