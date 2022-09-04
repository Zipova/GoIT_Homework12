from repository.address_book import AddressBook
from decorators.error_handlers import input_error, birthday_error

def main():
    phone_book = AddressBook()
    myiter = iter(phone_book)
    print("Hello! I am Your Phone Book! You can add Your friends' contacts and birthday or load your Phone Book from file. Let's start!")
    while True:
        user_command = input('>>>')
        if user_command.lower() == 'hello':
            print(greeting())
        elif user_command.lower() in (".", "good bye", "close", "exit"):
            print(good_buy())
            break
        elif user_command.lower() == 'show all':
            print(show_all(phone_book))
        elif user_command.lower() == 'show page':
            print(show_page(myiter))
        elif user_command.lower().startswith('days to birthday'):
            print(days_to_bd(user_command, phone_book))
        elif user_command.lower().startswith('save to '):
            print(save_to_file(user_command, phone_book))
        elif user_command.lower().startswith('load from '):
            phone_book = load_from_file(user_command, phone_book)
            myiter = iter(phone_book)
            print('Done!')
        else:
            command = user_command.split(' ')
            if command[0].lower() == 'add':
                print(add(command, phone_book))
            elif command[0].lower() == 'change':
                print(change(command, phone_book))
            elif command[0].lower() == 'phone':
                print(phone(command, phone_book))
            elif command[0].lower() == 'delate':
                print(delate(command, phone_book))
            elif command[0].lower() == 'birthday':
                print(birthday(command, phone_book))
            elif command[0].lower() == 'find':
                print(find(command, phone_book))
            else:
                print('Unknown command.')


def greeting():
    return 'How can I help you?'

def good_buy():
    return 'Good buy!'

def show_all(phone_book):
    return phone_book

def show_page(phone_book):
    return next(phone_book)
    
@input_error
def add(command, phone_book): 
    if len(command) != 3:
        raise IndexError()
    return phone_book.add_record(command[1], phone = command[2])

@input_error
def change(command, phone_book):
    if len(command) != 4:
        raise IndexError()
    if command[1] not in phone_book.keys():
        raise KeyError()
    phone_book[command[1]].edit_phone(command[2], command[3])
    return 'Done!'

@input_error
def delate(command, phone_book):
    if len(command) != 3:
        raise IndexError()
    if command[1] not in phone_book.keys():
        raise KeyError()
    return phone_book[command[1]].del_phone(command[2])
    

@input_error
def phone(command, phone_book):
    if len(command) != 2:
        raise IndexError()
    if command[1] not in phone_book.keys():
        raise KeyError()
    all_phones = ''
    for p in phone_book[command[1]].phones:
            all_phones += str(p.value) + ', ' 
    return (all_phones[:-2])


@birthday_error
def birthday(command, phone_book):
    if len(command) == 2:
        name = command[1]
        if name not in phone_book.keys():
            raise KeyError()
        return phone_book[name].birthday.value
    elif len(command) == 3:
        return phone_book.add_record(command[1], birthday=command[2])
    else:
        raise IndexError()

@birthday_error
def days_to_bd(user_command, phone_book):
    command = user_command.split(' ')
    if len(command) != 4:
        raise IndexError()
    name = command[3]
    if name in phone_book.keys():
        return phone_book[name].days_to_birthday()
    else:
        raise KeyError

def find (command, phone_book):
    if len(command) != 3:
        return 'Incorrect input.'
    return phone_book.find(command[1], command[2])

def save_to_file(user_command, phone_book):
    command = user_command.split(' ')
    if len(command) != 3:
        return 'Incorrect input.'
    return phone_book.save_to_file(command[2])

def load_from_file(user_command, phone_book):
    command = user_command.split(' ')
    if len(command) != 3:
        return 'Incorrect input.'
    return phone_book.load_from_file(command[2])


if __name__ == "__main__":
    main()