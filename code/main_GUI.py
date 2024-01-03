import sys

from PyQt5.QtWidgets import QApplication

from bowling_alley import BowlingAlley
from GUI_windows import Window


def main():
    '''this main function calls the GUI.'''
    # create bowling alley object
    test_alley = BowlingAlley("alley", 5)

    App = QApplication(sys.argv)
    main_window = Window(test_alley)
    sys.exit(App.exec())


if __name__ == "__main__":
    main()
