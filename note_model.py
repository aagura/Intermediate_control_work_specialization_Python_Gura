from datetime import datetime
import json
from note import Note

class NoteModel:
    def __init__(self, filename):
        self.filename = filename
        self.notes = []
        self.load_notes()

    def clear_notes(self):
        self.notes.clear()

    def load_notes(self):
        try:
            self.clear_notes() 
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for item in data:
                    note = Note(item['head'], item['body'])
                    note.id = item['id']
                    note.date = datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S')
                    self.notes.append(note)
            return "Записи прочитаны успешно"  
        except FileNotFoundError:
            return "Файл не найден"  
        except json.JSONDecodeError:
            return "Неправильный формат данных в файле notes.json. Отредактируйте или удалите файл"  




    def save_notes(self):
        data = [{'id': note.id, 'head': note.head, 'body': note.body, 'date': note.date.strftime('%Y-%m-%d %H:%M:%S')} for note in self.notes]
        with open(self.filename, 'w') as file:
            json.dump(data, file)

    def edit_note(self, note_id, head, body):
        note = self.get_note_by_id(note_id)
        if note:
            note.head = head
            note.body = body
            note.date = datetime.now()
            self.save_notes()
            return note
        return None

    def add_note(self, head, body):
        note = Note(head, body)
        if self.notes:
            note.id = max(note.id for note in self.notes) + 1
        else:
            note.id = 1
        note.date = datetime.now()
        self.notes.append(note)
        self.save_notes()
        return note

    def delete_note_by_id(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            self.save_notes()
            return note
        return None

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None
    
    def get_notes_by_date_range(self, start_date, end_date):
        filtered_notes = []
        for note in self.notes:
            if start_date <= note.date <= end_date:
                filtered_notes.append(note)
        return filtered_notes