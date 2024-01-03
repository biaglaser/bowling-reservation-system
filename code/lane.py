class Lane:
    """this class defines a lane"""

    def __init__(self, number, bowling_alley):
        self.bowling_alley = bowling_alley
        self.lane_number = number
        self.is_empty = True

    def get_bowling_alley(self):
        return self.bowling_alley

    def get_number(self):
        return self.lane_number

    def get_empty(self):
        return self.is_empty

    '''Method to change the lane from free to occupied, and vice-versa.
    This method is called on the reservation_class, when reservations are changed from valid to expired.'''
    def change_status(self):
        if self.is_empty:
            self.is_empty = False
        else:
            self.is_empty = True
