'''This function has the purpose of facilitating testing.

This file should be used to create bowling alleys and save them to a file. In the real world it would be run
by the Bowling Alley company that wants to register their alley and use the user-program run on main.py.

You can use this file to create multiple bowling alleys. When running the main program in main.py, you
should add the name of the file you saved your alley and wish to upload on line 263 (of the main.py file).

BowlingAlleys are created with the attributes name and number_of_lanes.
Here you can also comment and un-comment "add_customer" and "add_reservation" parts to initiate and save your
bowling alley with as many customers/reservations as you want!

It is assumed that all information to create the alley is correct. E.g.: password has at least 8 characters.
Any error handling happens only the user-program run by the main.py file.
'''

import datetime
import pickle

from bowling_alley import BowlingAlley


'''Function to save the BowlingAlley-obj created by this file.'''
def save_to_file(filename, alley_obj):
    # add customers to a file to save them
    file = open(filename, 'wb')
    pickle.dump(alley_obj, file)
    file.close()


'''Function to create the BowlingAlley-obj. Here you input the name and number of lanes of your bowling alley.

Additionally, you can already register pre-existing customers and/or reservations. This can be done by commenting or
un-commenting "add_customer" and "add_reservation" parts. Optionally, you can also change such information.'''
def create_alley():
    alley_name = 'test_alley'  # add here the desired name for the bowling alley
    number_of_lanes = 2     # change the number of lanes as you wish. The number should be 1 or bigger.

    # create BowlingAlley object
    alley = BowlingAlley(alley_name, number_of_lanes)

    # add_customer
    name = 'test'       # change to any desired inputs
    name2 = 'test2'
    email = 'test@gmail.com'
    password = 'test_test'
    phone = '00000000'
    # create customer
    alley.add_customer(name, name2, email, password, phone)

    # get customer that was just created
    customer_list = alley.get_customers()
    test_customer = customer_list[0]

    # add_reservation
    day = datetime.date(2022, 5, 6)     # change date and time as desired
    hour = datetime.time(14)
    # create reservation
    test_customer.add_reservation(day, hour)

    # call save to file
    save_to_file('saved_file_2.b', alley)     # change name of the file as desired


create_alley()
