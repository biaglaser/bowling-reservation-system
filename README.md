# Y2_2022_21033_
# Bowling Alley - reservation system

## Introduction
This reservation system allows customers of different Bowling Alley companies register themselves, book and cancel 
lane reservations.

## File and directory structure
- create_alley.py: create a Bowling Alley company and save it to a file (with possible pre-existing customers and 
reservations)
- main.py: run the user-interactive program based on a loaded file (with a BowlingAlley-obj), where users can register,
log in, and book and cancel reservations.
- bowling_alley.py: define BowlingAlley class
- lane.py: define Lane class
- customer.py: define Customer class
- reservations.py: define Reservations class
- GUI_windows.py: define different QWidget classes
- main_GUI.py: run GUI program (only illustrative, does not actually work with the main program)

## Installation instructions
This program only uses PyQt5 and other inbuilt python libraries that do not require installation (such as pickle and 
datetime).

## User instructions
Before running the main.py directory, first run create_alley.py. This will create a Bowling Alley - object and save it 
to a text file of your choice. Further instructions are found on this directory (create_alley.py), which is modifiable 
for different Bowling Alley companies that would wish to use this program.

Once the file is created, add the name of the file on line 263.
You can now run the main.py function for the user experience and interaction with the main program.

The main_GUI.py directory runs an illustrative view of what the graphical interface would look like. The buttons are 
clickable, and you are guided through different windows. However, this is not connected with the main function (i.e. 
no information is stored/processed).