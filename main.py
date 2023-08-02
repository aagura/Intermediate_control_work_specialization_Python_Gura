from console_presenter import ConsolePresenter
from console_view import ConsoleView
from note_model import NoteModel

if __name__ == "__main__":
    model = NoteModel("notes.json")
    view = ConsoleView()
    presenter = ConsolePresenter(view, model)
    presenter.run()





