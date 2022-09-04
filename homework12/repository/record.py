from repository.fields.phone import Phone
from decorators.error_handlers import input_error
from datetime import date
from repository.fields.birthday import Birthday

class Record:
    def __init__(self, name, phone = None, birthday = None) -> None:
        self.name = name
        self.birthday = birthday
        self.phones = []
        self.phones.append(phone)

    def add_phone(self, phone):
        self.phones.append(phone)
        return 'Done!'

    def del_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p) 
                return 'Done!'
        return "This phone doesn't exist in this contact."

    @input_error
    def edit_phone (self, phone, phone_2):
        for p in self.phones:
            if p.value == phone:
                p.value = phone_2
                print(p.value)
                return 'Done!'
        return "This phone doesn't exist in this contact."

    def add_birthday(self, birthday):
        bd = Birthday(birthday)
        if bd.value == None:
            raise ValueError
        self.birthday = bd
        return 'Done!'

    def days_to_birthday(self):
        bd = self.birthday.value.split('/')
        current_date = date.today()
        bd_this_year = date(year=current_date.year, month=int(bd[1]), day=int(bd[0]))
        diff = bd_this_year - current_date
        if diff.days < 0:
            bd_this_year = date(year=current_date.year+1, month=int(bd[1]), day=int(bd[0]))
            diff = bd_this_year - current_date
        return diff.days

    def __repr__(self):
        phones = ', '.join(str(el) for el in self.phones)
        return '|{:^15}|{:^15}|{:^15}'.format(str(self.name), str(self.birthday), str(phones))