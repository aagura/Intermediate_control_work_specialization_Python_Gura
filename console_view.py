# console_view.py

class ConsoleView:
    def show_menu(self):
        #   def show_menu(self):
        print("\nМеню:")
        print("1. Показать все заметки")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")

    def get_user_choice(self):
        return int(input("Введите номер пункта меню: "))

    def get_note_data(self):
        head = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        return head, body

    def get_note_id(self):
        return int(input("Введите id заметки для редактирования или удаления: "))

    def show_all_notes(self, notes):
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
