from repository.fields.field import Field
import re

class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(value) == 10 and re.match('\d\d/\d\d/\d{4}', value):
            self.__value = value
        

