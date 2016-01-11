class SingleMethodList(object):
    def __init__(self, l):
       self._list = l

    def get(self, index):
        try:
            return self._list[index]
        except IndexError:
            return None
