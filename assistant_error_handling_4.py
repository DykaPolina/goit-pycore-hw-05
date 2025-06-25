NOT_FOUND = "Contact not found."


def input_error(func):
    """
    Decorator to handle common user input errors for bot commands.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
    return inner


def parse_input(user_input):
    """
    Parses the user input into command and arguments.
    Returns: command (str), args (list of str)
    """
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    raise KeyError


@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts.get(name, NOT_FOUND)


def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            if len(args) != 2:
                print("Usage: add [name] [phone]")
            else:
                print(add_contact(args, contacts))

        elif command == "change":
            if len(args) != 2:
                print("Usage: change [name] [new_phone]")
            else:
                print(change_contact(args, contacts))

        elif command == "phone":
            if len(args) != 1:
                print("Usage: phone [name]")
            else:
                print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
