
class ConsolePresenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def show_all_notes(self):
        load_result = self.model.load_notes()
        if load_result == "Записи прочитаны успешно":
            notes = self.model.notes
            self.view.show_all_notes(notes)
            choice = self.view.get_yes_or_no("Отфильтровать под дате? Y/N")
            if choice == "Y":
                start_date = self.view.get_date("Введите начальную дату (в формате YYYY-MM-DD)")
                end_date = self.view.get_date("Введите конечную дату (в формате YYYY-MM-DD)")
                filtered_notes = self.model.get_notes_by_date_range(start_date, end_date)
                if not filtered_notes:
                    self.view.show_no_notes_in_period()
                else:
                    self.view.show_all_notes(filtered_notes)
        elif load_result == "Файл не найден":
            self.view.show_message("Записи отсутствуют. Создайте заметку.")
        else:
            self.view.show_message(load_result)

    def add_note(self):
        head = self.view.get_note_data("Введите заголовок заметки", None)
        body = self.view.get_note_data("Введите текст заметки", None)
        note = self.model.add_note(head, body)
        self.view.show_message(f"Заметка ID: {note.id} успешно добавлена!")

    def edit_note(self):
        note_id = self.view.get_note_id()
        note = self.model.get_note_by_id(note_id)
        if note:
            updated_head = self.view.get_note_data("Введите новый заголовок заметки", note.head)
            updated_body = self.view.get_note_data("Введите новое тело заметки", note.body)
            edited_note = self.model.edit_note(note_id, updated_head, updated_body)
            if edited_note:
                self.view.show_message(f"Заметка ID: {edited_note.id} успешно отредактирована!")
            else:
                self.view.show_message("Заметка не найдена!")
        else:
            self.view.show_message("Заметка не найдена!")

    def delete_note(self):
        note_id = int(self.view.get_note_id())
        deleted_note = self.model.delete_note_by_id(note_id)
        if deleted_note:
            self.view.show_message(f"Заметка ID: {deleted_note.id} успешно удалена!")
        else:
            self.view.show_message("Заметка не найдена!")

    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.get_user_choice()

            if choice == 1:
                self.show_all_notes()
            elif choice == 2:
                self.add_note()
            elif choice == 3:
                self.edit_note()
            elif choice == 4:
                self.delete_note()
            elif choice == 5:
                break
            else:
                self.view.show_message("Некорректный выбор. Попробуйте еще раз.")



