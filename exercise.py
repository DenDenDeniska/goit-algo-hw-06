from collections import UserDict
from hmac import new

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

class Name(Field):
    # реалізація класу
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    # реалізація класу
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("Телефон неверного формата")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: list = []

    # реалізація класу
    def add_phone(self, number):
        self.phones.append(Phone(number))
    
    def edit_phone(self, old_number, new_number):
        number = next(num for num in self.phones if num.value == old_number)
        self.phones[self.phones.index(number)] = Phone(new_number)

    def find_phone(self, number):
        number = next(num for num in self.phones if num.value == number)
        return self.phones[self.phones.index(number)]

    def remove_phone(self, number):
        number = next(num for num in self.phones if num.value == number)
        del self.phones[self.phones.index(number)]

    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, name):
        self.data.update({name.name.value: name})

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")

john_record.add_phone("1234567890")
john_record.add_phone("5555555555")


# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
print(john)
john.edit_phone("1234567890", "1112223333")
print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
