"""This file has the GUI windows, which work with the main_GUI.py file.
The GUI is only illustrative, it does not function with the actual program."""
from PyQt5 import QtGui

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QLineEdit, \
    QCalendarWidget

'''This class sets the widgets shown in the Calendar Window.'''
class CalendarWindow(QWidget):
    def __init__(self):     # set characteristics of the window
        super().__init__()
        self.setWindowTitle("Calendar")
        self.top = 400
        self.left = 400
        self.width = 800
        self.height = 700

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.calendar()

    '''Method to set the calendar widget'''
    def calendar(self):
        vbox = QVBoxLayout()
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)

        self.button = QPushButton("Enter", self)
        self.button.setGeometry(QRect(500, 700, 200, 40))
        # add button connection

        vbox.addWidget(self.calendar)
        vbox.addWidget(self.button)

        self.setLayout(vbox)


'''This class sets the widgets shown in the Reservation Window and opens the Calendar Window once the button
is pressed.'''
class ReservationWindow(QWidget):
    def __init__(self):     # set characteristics of the window
        super().__init__()
        self.setWindowTitle("Reservation")
        self.top = 400
        self.left = 400
        self.width = 800
        self.height = 700

        self.setGeometry(self.left, self.top, self.width, self.height)

        # set window widgets
        label = QLabel("Make a new reservation!", self)
        label.setFont(QtGui.QFont('Calibri', 10))
        label.adjustSize()
        label.move(300, 250)

        button = QPushButton("Choose a date", self)
        button.setGeometry(QRect(300, 300, 200, 40))
        button.clicked.connect(self.open_calendar_window)

    '''creates a CalendarWindow class and shows its gui items'''
    def open_calendar_window(self):
        self.w = CalendarWindow()
        self.w.show()
        self.hide()


'''This class sets the widgets shown in the Log in Window and opens the Reservation Window once the button "Enter"
is pressed.'''
class LoginWindow(QWidget):
    def __init__(self):     # set characteristics of the window
        super().__init__()
        self.setWindowTitle("Log in")
        self.top = 400
        self.left = 400
        self.width = 800
        self.height = 700

        self.setGeometry(self.left, self.top, self.width, self.height)

        # set window widgets
        label = QLabel("Enter your information:", self)
        label.setFont(QtGui.QFont('Calibri', 20))
        label.adjustSize()
        label.move(50, 50)

        email_label = QLabel("Email Address:", self)
        email_label.setFont(QtGui.QFont('Calibri', 10))
        email_label.adjustSize()
        email_label.move(60, 160)
        email_input = QLineEdit(self)
        email_input.move(200, 150)
        email_input.resize(280, 40)
        # user_email = email_input.text()

        password_label = QLabel("Password:", self)
        password_label.setFont(QtGui.QFont('Calibri', 10))
        password_label.adjustSize()
        password_label.move(60, 210)
        password_input = QLineEdit(self)
        password_input.setEchoMode(QLineEdit.Password)
        password_input.move(200, 200)
        password_input.resize(280, 40)
        # user_password = password_input.text()

        button = QPushButton("Enter", self)
        button.setGeometry(QRect(250, 300, 100, 40))
        button.clicked.connect(self.open_reservation_window)

        # check = self.check_info(user_email, user_password) -> deleted function bc it was not working

    '''creates a ReservationWindow class and shows its gui items'''
    def open_reservation_window(self):
        self.w = ReservationWindow()
        self.w.show()
        self.hide()


'''This class sets the widgets shown in the Sign up Window and opens the Reservation Window once the button "Enter"
is pressed.'''
class SignupWindow(QWidget):
    def __init__(self):     # set characteristics of the window
        super().__init__()
        self.setWindowTitle("Sign up")
        self.top = 400
        self.left = 400
        self.width = 800
        self.height = 700

        self.setGeometry(self.left, self.top, self.width, self.height)

        # set window widgets
        label = QLabel("Enter your information:", self)
        label.setFont(QtGui.QFont('Calibri', 20))
        label.adjustSize()
        label.move(50, 50)

        name_label = QLabel("First name:", self)
        name_label.setFont(QtGui.QFont('Calibri', 10))
        name_label.adjustSize()
        name_label.move(60, 160)
        name_input = QLineEdit(self)
        name_input.move(200, 150)
        name_input.resize(280, 40)
        # user_name = name_input.text()

        name2_label = QLabel("Last name:", self)
        name2_label.setFont(QtGui.QFont('Calibri', 10))
        name2_label.adjustSize()
        name2_label.move(60, 210)
        name2_input = QLineEdit(self)
        name2_input.move(200, 200)
        name2_input.resize(280, 40)
        # user_name2 = name2_input.text()

        phone_label = QLabel("Phone number:", self)
        phone_label.setFont(QtGui.QFont('Calibri', 10))
        phone_label.adjustSize()
        phone_label.move(60, 260)
        phone_input = QLineEdit(self)
        phone_input.move(200, 250)
        phone_input.resize(280, 40)
        # user_phone = phone_input.text()

        email_label = QLabel("Email Address:", self)
        email_label.setFont(QtGui.QFont('Calibri', 10))
        email_label.adjustSize()
        email_label.move(60, 310)
        email_input = QLineEdit(self)
        email_input.move(200, 300)
        email_input.resize(280, 40)
        # user_email = email_input.text()

        password_label = QLabel("Password:", self)
        password_label.setFont(QtGui.QFont('Calibri', 10))
        password_label.adjustSize()
        password_label.move(60, 360)
        password_input = QLineEdit(self)
        password_input.setEchoMode(QLineEdit.Password)
        password_input.move(200, 350)
        password_input.resize(280, 40)
        # user_password = password_input.text()

        button = QPushButton("Enter", self)
        button.setGeometry(QRect(250, 450, 100, 40))
        button.clicked.connect(self.open_reservation_window)

    '''creates a ReservationWindow class and shows its gui items'''
    def open_reservation_window(self):
        self.w = ReservationWindow()
        self.w.show()
        self.hide()


'''This class sets the widgets shown in the main Window. It opens the Log in Window if the button "Log in"
is pressed, and the Sign up Window if the button "Sign up" is pressed.'''
class Window(QMainWindow):
    def __init__(self, alley):      # set characteristics of the window
        super().__init__()
        self.alley = alley
        self.title = "Reservation System"
        self.top = 400
        self.left = 400
        self.width = 800
        self.height = 700

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # set window widgets
        self.first_window_components()

        self.show()

    def get_alley(self):
        return self.alley

    '''Method that defines the gui items in this window.'''
    def first_window_components(self):
        label = QLabel("Welcome to our bowling reservation system!", self)
        label.setFont(QtGui.QFont('Calibri', 10))
        label.adjustSize()
        label.move(245, 250)

        self.button = QPushButton("Log in", self)
        self.button.setGeometry(QRect(250, 300, 100, 40))
        self.button.clicked.connect(self.open_login)

        self.button2 = QPushButton("Sign up", self)
        self.button2.setGeometry(QRect(450, 300, 100, 40))
        self.button2.clicked.connect(self.open_signup)

    '''creates a LoginWindow class and shows its gui items'''
    def open_login(self):
        self.w = LoginWindow()
        self.w.show()
        self.hide()

    '''creates a SignupWindow class and shows its gui items'''
    def open_signup(self):
        self.w = SignupWindow()
        self.w.show()
        self.hide()
