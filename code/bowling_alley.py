from customer import Customer
from lane import Lane


class BowlingAlley:
    """this class defines the bowling alley"""

    def __init__(self, name, num_of_lanes):
        self.name = name
        self.customers = []
        self.num_lanes = num_of_lanes
        self.lanes = self.create_lanes(num_of_lanes)    # list of lanes
        self.current_reservations = []                  # list of valid reservations

    def get_name(self):
        return self.name

    def get_customers(self):
        return self.customers

    def get_num_lanes(self):
        return self.num_lanes

    def get_lanes(self):
        return self.lanes

    def get_current_reservations(self):
        return self.current_reservations

    '''Method to add a customer to the Bowling Alley register.'''
    def add_customer(self, firstname, lastname, email, password, phone):  # costumer info
        new_customer = Customer(self, firstname, lastname, email, password, phone)
        self.customers.append(new_customer)

    '''Method called upon object creation. It creates the alley lanes and set them on a list.'''
    def create_lanes(self, total):
        # create lane-obj and add them to the list/bowlingalley
        lanes_list = []
        number = 0
        while number < total:
            new_lane = Lane(number, self)
            lanes_list.append(new_lane)
            number += 1
        return lanes_list
