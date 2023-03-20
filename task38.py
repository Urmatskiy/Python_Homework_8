def main():
    while True:
        show_menu()
        choice = int(input("Ваш выбор: "))
        if choice == 1:
            try:
                show_data()
            except FileNotFoundError:
                print("Файл не создан")
        elif choice == 2:
            data = input("Введите данные: ")
            save_data(data)
        elif choice == 3:
            data = input("Введите известные вам данные о человеке: ")
            new_data = input("Введите новые данные: ")
            change_data(data, new_data)
            print("Данные изменены")
        elif choice == 4:
            data = input("Введите известные вам данные о человеке: ")
            delete_data(data)
            print("Данные удалены")
        elif choice == 5:
            data = input("Введите известные вам данные о человеке: ")
            result = find_data(data)
            if result:
                for elem in result:
                    print(elem.rstrip("\n"))
            else:
                print("В файле нет таких данных")
        else:
            break


def show_menu():
    print("Нажмите 1, чтобы посмотреть все данные")
    print("Нажмите 2, чтобы добавить данные")
    print("Нажмите 3, чтобы изменить данные")
    print("Нажмите 4, чтобы удалить данные")
    print("Нажмите 5, чтобы найти данные")
    print("Нажмите 6, чтобы выйти из программы")


def show_data():
    print()
    with open("Homework_8\data.txt", "r", encoding="utf-8") as file:
        print(file.read())
    print()


def save_data(stroka):
    with open("Homework_8\data.txt", "a", encoding="utf-8") as file:
        file.write(f"{stroka}\n")


def change_data(old, new):
    with open("Homework_8\data.txt", "r", encoding="utf-8") as file:
        info = file.readlines()
    with open("Homework_8\data.txt", "w", encoding="utf-8") as file:
        for line in info:
            if old.lower() not in line.lower():
                file.write(line)
            else:
                file.write(f"{new}\n")


def delete_data(old):
    with open("Homework_8\data.txt", "r", encoding="utf-8") as file:
        info = file.readlines()
    with open("Homework_8\data.txt", "w", encoding="utf-8") as file:
        for line in info:
            if old.lower() not in line.lower():
                file.write(line)
            else:
                file.write("")


def find_data(data):
    result = []
    with open("Homework_8\data.txt", "r", encoding="utf-8") as file:
        info = file.readlines()
        for line in info:
            if data.lower() in line.lower():
                result.append(line)
    return result


main()
