# console_presenter.py
from console_view import ConsoleView
from note_model import NoteModel

class ConsolePresenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def show_all_notes(self):
        notes = self.model.notes
        self.view.show_all_notes(notes)

    def add_note(self):
        head, body = self.view.get_note_data()
        note = self.model.add_note(head, body)
        self.view.show_message(f"Заметка ID: {note.id} успешно добавлена!")

    def edit_note(self):
        note_id = self.view.get_note_id()
        note = self.model.get_note_by_id(note_id)
        if note:
            head, body = self.view.get_note_data()
            edited_note = self.model.edit_note(note_id, head, body)
            if edited_note:
                self.view.show_message(f"Заметка ID: {edited_note.id} успешно отредактирована!")
            else:
                self.view.show_message("Ошибка при редактировании заметки.")
        else:
            self.view.show_message("Заметка не найдена!")

    def delete_note(self):
        note_id = self.view.get_note_id()
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
