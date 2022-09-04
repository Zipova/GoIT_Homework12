from repository.fields.field import Field

class Name(Field):
    def __str__(self):
        return f'{self.value}'