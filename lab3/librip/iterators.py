# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        if type(items)is list:
            self.items = iter(items)
        else:
            self.items = items
        self.ignore_case = kwargs.get('ignore_case', False)
        self.mas = set()

    def __next__(self):
        while True:
            try:
                item = next(self.items)
                if type(item)is str and self.ignore_case is True:
                    i = item.lower()
                else:
                    i = item
                if i not in self.mas:
                    self.mas.add(i)
                    return i
            except Exception:
                raise StopIteration

    def __iter__(self):
        return self


