
from datetime import datetime


class ConsoleView:
    def show_menu(self):
        print("\nМеню:")
        print("1. Показать все заметки")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")

    def get_user_choice(self):
        while True:
            try:
                return int(input("Введите номер пункта меню: "))
            except ValueError:
                print("Ошибка: Введите цифру.")

    def get_note_data(self, message, note_data):
        if note_data:
            print(f"{message} (было: {note_data}): ", end="")
        else:
            print(f"{message}: ", end="")
        return input()

    def get_note_id(self):
        return int(input("Введите id заметки для редактирования или удаления: "))

    def show_all_notes(self, notes):
        if not notes:
            print("Записи отсутствуют. Создайте заметку.")
        else:
            print("\nСписок заметок:")
            for note in notes:
                print(f"ID: {note.id}, Заголовок: {note.head}, Текст: {note.body}, Дата: {note.date}")

    def show_note_details(self, note):
        if note:
            print(f"\nЗаметка ID: {note.id}")
            print(f"Заголовок: {note.head}")
            print(f"Текст: {note.body}")
            print(f"Дата: {note.date}")
        else:
            print("Заметка не найдена!")

    def show_message(self, message):
        print(message)
    

    
    def show_no_notes_in_period(self):
        print("В заданном периоде заметки отсутствуют.")

    def get_yes_or_no(self, message):
        while True:
            choice = input(message + " (Y/N): ").strip().upper()
            if choice == "Y" or choice == "N":
                return choice
            print("Ошибка: Введите 'Y' или 'N'.")

    def get_date(self, message):
        while True:
            date_str = input(message + " (Формат: ГГГГ-ММ-ДД): ")
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d')
                return date
            except ValueError:
                print("Ошибка: Введите дату в корректном формате (ГГГГ-ММ-ДД).")

