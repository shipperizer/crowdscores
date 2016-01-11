class SingleMethodList(object):
    def __init__(self, l):
       self._list = l

    def get(self, index):
        try:
            return self._list[index]
        except IndexError:
            return None

    def __len__(self):
        # implement __len__ to allow for testing
        return len(self._list)      
