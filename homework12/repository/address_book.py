from collections import UserDict
from repository.fields.name import Name
from repository.fields.phone import Phone
from decorators.error_handlers import input_error, birthday_error
from repository.record import Record
from repository.fields.birthday import Birthday
import pickle

class AddressBook(UserDict):
    __items_per_page = 3

    def items_per_page(self, value):
        self.__items_per_page = value

    items_per_page = property(fget=None, fset=items_per_page)

    @input_error
    @birthday_error
    def add_record(self, name, phone=None, birthday=None):
        name = Name(name)
        if phone:
            phone_number = Phone(phone)
            #if phone_number.value == None:
                #raise ValueError
            if name.value in self.data.keys():
                rec = self.data[name.value]
                rec.add_phone(phone_number)
                return 'Done!'
            rec = Record(name, phone_number)
            self.data[rec.name.value] = rec
            return 'Done!'
        if birthday:
            bd = Birthday(birthday)
            if bd.value == None:
                raise ValueError
            if name.value in self.data.keys():
                self.data[name.value].birthday = bd
                return 'Done!'
            else:
                rec = Record(name, birthday=bd)
                self.data[rec.name.value] = rec
                return 'Done!'

    def __repr__(self):
        title = '|{:^15}|{:^15}|{:^15}'.format('Name', 'Birthday', 'Phone')
        result = title + '\n'
        records = list(self.data.items())
        for record in records:
            result += str(record[1]) + '\n'
        return result

    def __iter__(self):
        self.page = 0
        return self

    def __next__(self):
        records = list(self.data.items())
        start_index = self.page * self.__items_per_page
        end_index = (self.page + 1) * self.__items_per_page
        if len(records) == 0:
            return 'Your phone book is empty.'
        if len(records) > end_index:
            to_return = records[start_index:end_index]
            self.page += 1
        else:
            if len(records) > start_index:
                to_return = records[start_index : len(records)] 
                self.page = 0
            else:
                to_return = records[0:self.__items_per_page]
                self.page = 1
        title = '|{:^15}|{:^15}|{:^15}'.format('Name', 'Birthday', 'Phone')
        result = title + '\n'
        for record in to_return:
            result += str(record[1]) + '\n'
        return result
    

    def find(self, option, key):
        matches = []
        if option == 'name':
            for name in self.data.keys():
                if name.find(key) != -1:
                    matches.append(name)
            if matches == []:
                return "No mathes."
            title = '|{:^15}|{:^15}|{:^15}'.format('Name', 'Birthday', 'Phone')
            result = title + '\n'
            for name in matches:
                result += str(self.data[name]) + '\n'
            return result
        elif option == 'phone':
            for record in self.data.values():
                for number in record.phones:
                    if number.value.find(key) != -1:
                        matches.append(record)
            if matches == []:
                return "No mathes."
            title = '|{:^15}|{:^15}|{:^15}'.format('Name', 'Birthday', 'Phone')
            result = title + '\n'
            for record in matches:
                result += str(record) + '\n'
            return result


    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        return 'Done!'

    def load_from_file(self, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)