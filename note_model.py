# note_model.py
import datetime
import json
from note import Note

class NoteModel:
    def __init__(self, filename):
        self.filename = filename
        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for item in data:
                    note = Note(item['head'], item['body'], item['date'])
                    note.id = item['id']
                    self.notes.append(note)
        except FileNotFoundError:
            pass

    def save_notes(self):
        data = [{'id': note.id, 'head': note.head, 'body': note.body, 'date': note.date} for note in self.notes]
        with open(self.filename, 'w') as file:
            json.dump(data, file)

    def add_note(self, head, body):
        note = Note(head, body)
        if self.notes:
            note.id = max(note.id for note in self.notes) + 1
        else:
            note.id = 1
        self.notes.append(note)
        self.save_notes()
        return note

    def edit_note(self, note_id, head, body):
        note = self.get_note_by_id(note_id)
        if note:
            note.head = head
            note.body = body
            note.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.save_notes()
            return note
        return None

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
