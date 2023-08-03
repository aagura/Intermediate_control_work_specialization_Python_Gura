from datetime import datetime as dt

class Note:
    def __init__(self, head, body, date=None):
        self.id = None
        self.head = head
        self.body = body
        self.date = dt.now().strftime('%Y-%m-%d %H:%M:%S') if date is None else date
