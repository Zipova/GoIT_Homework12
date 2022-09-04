from repository.fields.field import Field
import re

class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(value) == 13 and re.match('[+380]{1}\d{9}', value):
            self.__value = value
        else:
            raise ValueError

    def __str__(self):
        return f'{self.value}'
