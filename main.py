#практика 2
#задание 1
def basketball_players():

    players = {
        "Леброн Джеймс": 246,
        "Майкл Джордан": 198,
        "Стефен Карри": 191,
        "Шакил ОНил": 236,
        "Коби Брайант": 198
    }

    while True:
        print("баскетбольный справочник")
        print("1. Показать всех баскетболистов")
        print("2. Добавить баскетболиста")
        print("3. Удалить баскетболиста")
        print("4. Найти баскетболиста")
        print("5. Изменить рост баскетболиста")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            print("\nСписок баскетболистов:")
            for name, height in players.items():
                print(f"{name}: {height} см")

        elif choice == '2':
            name = input("Введите ФИО баскетболиста: ")
            try:
                height = int(input("Введите рост (в см): "))
                players[name] = height
                print(f"Баскетболист {name} добавлен!")
            except:
                print("Ошибка! Рост должен быть числом.")

        elif choice == '3':
            name = input("Введите ФИО баскетболиста для удаления: ")
            if name in players:
                del players[name]
                print(f"Баскетболист {name} удален!")
            else:
                print("Баскетболист не найден!")

        elif choice == '4':
            name = input("Введите ФИО для поиска: ")
            if name in players:
                print(f"{name}: {players[name]} см")
            else:
                print("Баскетболист не найден!")

        elif choice == '5':
            name = input("Введите ФИО баскетболиста: ")
            if name in players:
                try:
                    new_height = int(input("Введите новый рост: "))
                    players[name] = new_height
                    print("Рост обновлен!")
                except:
                    print("Ошибка! Рост должен быть числом.")
            else:
                print("Баскетболист не найден!")

        elif choice == '0':
            print("Выход из программы.")
            break


basketball_players()

#задание 2
def english_french_dictionary():
    dictionary = {
        "hello": "bonjour",
        "goodbye": "au revoir",
        "thank you": "merci",
        "yes": "oui",
        "no": "non"
    }

    while True:
        print("Англо-французкий словарь")
        print("1. Показать все слова")
        print("2. Добавить слово")
        print("3. Удалить слово")
        print("4. Найти перевод")
        print("5. Изменить перевод")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            print("\nСловарь:")
            for eng, fr in dictionary.items():
                print(f"{eng} -> {fr}")

        elif choice == '2':
            eng_word = input("Введите слово на английском: ").lower()
            fr_word = input("Введите французский перевод: ").lower()
            dictionary[eng_word] = fr_word
            print("Слово добавлено")

        elif choice == '3':
            eng_word = input("Введите английское слово для удаления: ").lower()
            if eng_word in dictionary:
                del dictionary[eng_word]
                print("Слово удалено!")
            else:
                print("Слово не найдено")

        elif choice == '4':
            eng_word = input("Введите английское слово: ").lower()
            if eng_word in dictionary:
                print(f"{eng_word} -> {dictionary[eng_word]}")
            else:
                print("Слово не найдено в словаре")

        elif choice == '5':
            eng_word = input("Введите английское слово: ").lower()
            if eng_word in dictionary:
                new_translation = input("Введите новый перевод: ").lower()
                dictionary[eng_word] = new_translation
                print("Перевод обновлен")
            else:
                print("Слово не найдено")

        elif choice == '0':
            print("До свидания")
            break

english_french_dictionary()


#задание 3
def company_database():
    employees = {
        1: {
            "ФИО": "Артем Филатов Борисович",
            "телефон": "+7 912 245-57-89",
            "email": "filatov@company.ru",
            "должность": "Менеджер",
            "кабинет": "101",
            "skype": "filatov_company"
        },
        2: {
            "ФИО": "Петрова Ирина Антоновна",
            "телефон": "+7 923 457-80-90",
            "email": "petrova@company.ru",
            "должность": "Программист",
            "кабинет": "205",
            "skype": "petrova_company"
        }
    }

    next_id = 3

    while True:
        print("база данных")
        print("1. Показать всех сотрудников")
        print("2. Добавить сотрудника")
        print("3. Удалить сотрудника")
        print("4. Найти сотрудника")
        print("5. Изменить данные сотрудника")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            print("\nСписок сотрудников:")
            for emp_id, info in employees.items():
                print(f"ID: {emp_id}")
                for key, value in info.items():
                    print(f"  {key}: {value}")

        elif choice == '2':
            print("\nДобавление нового сотрудника:")
            new_employee = {}
            new_employee["ФИО"] = input("ФИО: ")
            new_employee["телефон"] = input("Телефон: ")
            new_employee["email"] = input("Email: ")
            new_employee["должность"] = input("Должность: ")
            new_employee["кабинет"] = input("Номер кабинета: ")
            new_employee["skype"] = input("Skype: ")

            employees[next_id] = new_employee
            print(f"Сотрудник добавлен с ID: {next_id}")
            next_id += 1

        elif choice == '3':
            try:
                emp_id = int(input("Введите ID сотрудника для удаления: "))
                if emp_id in employees:
                    name = employees[emp_id]["ФИО"]
                    del employees[emp_id]
                    print(f"Сотрудник {name} удален!")
                else:
                    print("Сотрудник не найден!")
            except:
                print("Ошибка, Введите числовой ID.")

        elif choice == '4':
            search = input("Введите ФИО или ID для поиска: ")
            found = False

            try:
                emp_id = int(search)
                if emp_id in employees:
                    print("\nНайден сотрудник:")
                    for key, value in employees[emp_id].items():
                        print(f"{key}: {value}")
                    found = True
            except:
                pass

            if not found:
                for emp_id, info in employees.items():
                    if search.lower() in info["ФИО"].lower():
                        print(f"\nID: {emp_id}")
                        for key, value in info.items():
                            print(f"{key}: {value}")
                        found = True
                        break

            if not found:
                print("Сотрудник не найден!")

        elif choice == '5':
            try:
                emp_id = int(input("Введите ID сотрудника: "))
                if emp_id in employees:
                    print("\nТекущие данные:")
                    for key, value in employees[emp_id].items():
                        print(f"{key}: {value}")

                    field = input("\nКакое поле изменить? (ФИО, телефон, email, должность, кабинет, skype): ").lower()
                    if field in employees[emp_id]:
                        new_value = input(f"Введите новое значение для {field}: ")
                        employees[emp_id][field] = new_value
                        print("Данные обновлены!")
                    else:
                        print("Неверное название поля!")
                else:
                    print("Сотрудник не найден!")
            except:
                print("Ошибка! Введите числовой ID.")

        elif choice == '0':
            print("Выход из программы.")
            break


company_database()

#задание 4
def book_collection():
    books = {
        1: {
            "автор": "Лев Толстой",
            "название": "Война и мир",
            "жанр": "Роман",
            "год": 1867,
            "страницы": 1225,
            "издательство": "Русский вестник"
        },
        2: {
            "автор": "Федор Достоевский",
            "название": "Преступление и наказание",
            "жанр": "Роман",
            "год": 1866,
            "страницы": 672,
            "издательство": "Русский вестник"
        }
    }

    next_id = 3

    while True:
        print("КНИЖНАЯ КОЛЛЕКЦИЯ")
        print("1. Показать все книги")
        print("2. Добавить книгу")
        print("3. Удалить книгу")
        print("4. Найти книгу")
        print("5. Изменить данные книги")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            print("\nКоллекция книг:")
            for book_id, info in books.items():
                print(f"ID: {book_id}")
                print(f"  Автор: {info['автор']}")
                print(f"  Название: {info['название']}")
                print(f"  Жанр: {info['жанр']}")
                print(f"  Год: {info['год']}")
                print(f"  Страниц: {info['страницы']}")
                print(f"  Издательство: {info['издательство']}")

        elif choice == '2':
            print("\nДобавление новой книги:")
            new_book = {}
            new_book["автор"] = input("Автор: ")
            new_book["название"] = input("Название книги: ")
            new_book["жанр"] = input("Жанр: ")
            try:
                new_book["год"] = int(input("Год издания: "))
                new_book["страницы"] = int(input("Количество страниц: "))
            except:
                print("Ошибка! Год и страницы должны быть числами.")
                continue
            new_book["издательство"] = input("Издательство: ")

            books[next_id] = new_book
            print(f"Книга добавлена с ID: {next_id}")
            next_id += 1

        elif choice == '3':
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                if book_id in books:
                    title = books[book_id]["название"]
                    del books[book_id]
                    print(f"Книга '{title}' удалена!")
                else:
                    print("Книга не найдена!")
            except:
                print("Ошибка! Введите числовой ID.")

        elif choice == '4':
            search = input("Введите автора или название книги для поиска: ").lower()
            found = False

            for book_id, info in books.items():
                if (search in info["автор"].lower() or
                        search in info["название"].lower() or
                        search in info["жанр"].lower()):
                    print(f"\nID: {book_id}")
                    print(f"  Автор: {info['автор']}")
                    print(f"  Название: {info['название']}")
                    print(f"  Жанр: {info['жанр']}")
                    print(f"  Год: {info['год']}")
                    print(f"  Страниц: {info['страницы']}")
                    print(f"  Издательство: {info['издательство']}")
                    found = True

            if not found:
                print("Книги не найдены")

        elif choice == '5':
            try:
                book_id = int(input("Введите ID книги: "))
                if book_id in books:
                    print("\nТекущие данные книги:")
                    for key, value in books[book_id].items():
                        print(f"{key}: {value}")

                    field = input("\nКакое поле изменить? (автор, название, жанр, год, страницы, издательство): ")
                    if field in books[book_id]:
                        if field in ["год", "страницы"]:
                            try:
                                new_value = int(input(f"Введите новое значение для {field}: "))
                            except:
                                print("Ошибка! Значение должно быть числом.")
                                continue
                        else:
                            new_value = input(f"Введите новое значение для {field}: ")

                        books[book_id][field] = new_value
                        print("Данные обновлены")
                    else:
                        print("Неверное название поля")
                else:
                    print("Книга не найдена")
            except:
                print("Ошибка! Введите числовой ID.")

        elif choice == '0':
            print("Выход из программы.")
            break

book_collection()