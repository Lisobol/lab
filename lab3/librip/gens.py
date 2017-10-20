import random


# Генератор вычленения полей из массива словарей
# Пример:
#goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
#]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        key = args[0]
        for d in items:
            dict1 = d[key]
            yield dict1
    else:
        for d in items:
            dict1 = {key: d[key] for key in args}
            yield dict1

# Необходимо реализовать генератор


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    x = (random.randint(begin, end) for i in range(num_count))
    return x

 #pass
# Необходимо реализовать генератор
