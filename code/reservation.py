from extras import Extras


class Reservation:
    """describes a single reservation"""

    lane_price = 15

    def __init__(self, customer, bowling_alley, date, time):
        self.bowling_alley = bowling_alley      # bowling alley-obj
        self.owner = customer                   # customer-obj
        self.lane = self.set_lane()             # lane-obj
        self.date = date                        # date-obj
        self.time = time                        # time-obj
        self.is_valid = True  # if date < current date, True
        '''-------------- NOT USED IN THE MAIN FUNCTION --------------'''
        self.extras = Extras()                  # extras-obj
        '''-----------------------------------------------------------'''

    def get_owner(self):
        return self.owner

    def get_lane(self):
        return self.lane

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_extras(self):
        return self.extras

    def get_info(self):
        return self.info

    def valid(self):
        return self.is_valid

    def set_lane(self):
        for lane in self.bowling_alley.get_lanes():
            if lane.get_empty():
                lane.change_status()
                break
        return lane

    def change_valid(self):
        # change is_valid to False
        self.lane.change_status()
        self.is_valid = False

    def cancel(self):
        self.is_valid = False

    '''-------------- NOT USED IN THE MAIN FUNCTION --------------'''

    def get_total_price(self):
        # default lane price: 15e
        # add lane price with snack prices
        # return total price
        return Reservation.lane_price + self.extras.get_price()
