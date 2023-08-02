# note.py
from datetime import datetime

class Note:
    def __init__(self, head, body, date=None):
        self.id = None
        self.head = head
        self.body = body
        self.date = date if date else datetime.now().strftime('%Y-%m-%d %H:%M:%S')
