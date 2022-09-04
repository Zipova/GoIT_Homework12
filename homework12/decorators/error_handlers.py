def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This name do not exist in your phone book!'
        except ValueError:
            return 'Please enter a phone number in format +380111111111'
        except IndexError:
            return 'Give me name and phone please.'
    return inner

def birthday_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This name do not exist in your phone book!'
        except IndexError:
            return 'Incorrect input.'
        except AttributeError:
            return 'Enter birthday date in format DD/MM/YYYY.'
    return inner