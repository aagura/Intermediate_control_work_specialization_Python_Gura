from console_presenter import ConsolePresenter
from console_view import ConsoleView
from note_model import NoteModel

def main():
    view = ConsoleView()
    model = NoteModel("notes.json")
    presenter = ConsolePresenter(view, model)

    presenter.run()
 
       

if __name__ == "__main__":
    main()


