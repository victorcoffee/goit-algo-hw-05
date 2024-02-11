# Модуль 5. Завдання 4

import os
from pathlib import Path


# Декоратор обробляє винятки, що виникають у функціях - handler
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command"
        except ValueError:
            return "Enter the argument for the command"

    return inner


# Парсер команд
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Додавання контакту
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


# Зміна контакту
@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts.update({name: phone})
    return "Contact updated."


# Пошук номера телефону контакту
@input_error
def show_phone(args, contacts):
    name = args[0]
    phone = contacts.get(name)

    # Якщо контакт існує
    if phone:
        return phone
    else:
        return "This name is not in your Contacts."


#  Виведення всіх контаків
@input_error
def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{name} {phone}")

    return "All list of contacts printed."


# Основна програма
def main():
    os.system("cls")
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
