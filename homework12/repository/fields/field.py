class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(value) > 0:
            self.__value = value

    def __repr__(self):
        return f'{self.value}'
