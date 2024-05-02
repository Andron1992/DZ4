def total_salary(path):
    total_salary = 0
    num_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                salary = int(salary)
                total_salary += salary
                num_developers += 1
        average_salary = total_salary / num_developers
        return total_salary, average_salary

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None, None


total, average = total_salary("data/salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


print("\t")
print("\t")
print("\t")

def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_info = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
                cats_info.append(cat_info)

        return cats_info

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка: {e}")
        return []

cats_info = get_cats_info("data/cats_file.txt")
print(cats_info)

print("\t")
print("\t")
print("\t")

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(contacts, name, phone_number):
    if name in contacts:
        return "Contact already exists."
    contacts[name] = phone_number
    return "Contact added."

def change_contact(contacts, name, new_phone_number):
    if name not in contacts:
        return "Contact not found."
    contacts[name] = new_phone_number
    return "Contact updated."

def show_phone(contacts, name):
    if name not in contacts:
        return "Contact not found."
    return contacts[name]

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    all_contacts = "\n".join([f"{name}: {contacts[name]}" for name in contacts])
    return all_contacts

def main():
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
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()