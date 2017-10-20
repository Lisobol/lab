#!/usr/bin/env python3
from librip.gens import field
from librip.gens import gen_random
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
]

# Реализация задания 1
print([x for x in field(goods, 'title',)])
print([x for x in field(goods, 'title', 'color')])

print([x for x in gen_random(1, 3, 5)])
