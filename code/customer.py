from reservation import Reservation


class Customer:
    """describes a customer"""

    def __init__(self, bowling_alley, name1, name2, email, password, phone):
        self.bowling_alley = bowling_alley
        self.name = name1 + ' ' + name2
        self.email = email
        self.password = password
        self.phone_number = phone

        self.reservations_list = []

    def get_bowling_alley(self):
        return self.bowling_alley

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_phone(self):
        return self.phone_number

    def get_reservations_list(self):
        return self.reservations_list

    '''Method to create a reservation and add it to the customer's reservation list.
    It initializes a reservation object.'''
    def add_reservation(self, date, time):     # add reservation-obj
        new_reservation = Reservation(self, self.bowling_alley, date, time)
        self.reservations_list.append(new_reservation)
        self.bowling_alley.current_reservations.append(new_reservation)

    '''-------------- NOT USED IN THE MAIN FUNCTION --------------'''

    '''Method to alter the customer's name.'''
    def change_name(self, new_name1, new_name2):
        # checks if new name is different than old name
        # returns boolean value indicating success or failure
        new = new_name1 + ' ' + new_name2
        if new != self.name:
            self.name = new
            return True
        else:
            return False

    '''Method to alter the customer's email.'''
    def change_email(self, new_email):
        # checks if new email is different than old email
        # returns boolean value indicating success or failure
        if new_email != self.email:
            self.email = new_email
            return True
        else:
            return False

    '''Method to alter the customer's password.'''
    def change_password(self, new_password):
        # checks if new password is different than old password
        # updates password
        # returns boolean value indicating success or failure
        if new_password != self.password and len(new_password) >= 8:
            self.password = new_password
        else:
            pass  # TODO: I think this is wrong

    '''Method to alter the customer's phone number.'''
    def change_phone(self, new_phone):
        # checks if new phone is different than old phone
        # updates phone
        # returns boolean value indicating success or failure
        if new_phone != self.phone_number:
            self.phone_number = new_phone
            return True
        return False
