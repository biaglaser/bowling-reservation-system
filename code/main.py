import datetime
import pickle

'''
This function is responsible for saving the BowlingAlley object into a file. The information is saved as bits.
'''
def save_to_file(filename, alley_obj):
    # add customers to a file to save them
    file = open(filename, 'wb')
    pickle.dump(alley_obj, file)
    file.close()


'''
This function is responsible for loading a bowling alley's information from a file. The information on the
file should be saved with bits. The function returns the BowlingAlley object that was retrieved from the file.
'''
def load_from_file(filename):
    # load the existing bowling alley information
    try:
        file_handler = open(filename, 'rb')
        alley_obj = pickle.load(file_handler, encoding='UTF-8')
        file_handler.close()
        return alley_obj
    except EOFError:
        return None


'''
Function to guide the user through the log in process. It asks for the user's email and password and checks if
the user exists in the BowlingAlley register. The function takes the alley's customer's list as a parameter. It
returns 'None' if the log in fails (due to the email not being registered) or it returns the customer-obj that
is being logged in.
'''
def log_in(customers_list):
    # ask for user email and password
    email = str(input("Enter your email: "))
    password = str(input("Enter your password: "))
    email_ok = False
    if not customers_list:  # checks if the alley's register is empty
        print("There are no customers registered.")
        return None
    else:
        for customer in customers_list:  # checks if the email has been registered in the alley
            if customer.get_email() == email:
                email_ok = True
                break  # to stop at the correct customer index
        if not email_ok:
            print("This email is not registered.")
            return None

        while customer.get_password() != password:  # checks if the password is correct
            print("Incorrect password!")
            password = str(input("Enter your password: "))

    return customer  # returns the logged in customer


'''
Function to guide the user through the sign up process. It asks for the user's information and creates a new
customer in the alley register.
'''
def sign_in(alley):
    incorrect = True
    wrong = 0
    while incorrect:  # check if email is already registered
        email = str(input("Enter your email: "))
        for customer in alley.get_customers():
            if customer.get_email() == email:
                print("This email is already registered. Please input a new one.")
                wrong = 1
        if email == "":
            print("Email cannot be an empty line.")
        elif wrong == 0:
            incorrect = False
        wrong = 0

    incorrect = True
    while incorrect:
        name = str(input("Enter your first name: "))
        if name == "":
            print("Your first name cannot be an empty line.")
        else:
            incorrect = False

    incorrect = True
    while incorrect:
        name2 = str(input("Enter your last name: "))
        if name2 == "":
            print("Your last name cannot be an empty line.")
        else:
            incorrect = False

    incorrect = True
    while incorrect:
        phone = str(input("Enter your phone number: "))
        if phone == "":
            print("Your phone number cannot be an empty line.")
        else:
            incorrect = False

    password = str(input("Enter your password: "))
    while len(password) < 8:  # makes sure the password is of correct length
        password = str(input("The password should have at least 8 characters. Please input a new one: "))

    alley.add_customer(name, name2, email, password, phone)  # create customer and add it to the alley


'''
Function to guide the user through all the reservation-related options of the program. Here the user can
set up a new reservation, look at their valid reservations or quit the program.
When making a new reservation, the function creates a new reservation-obj and adds it to the list of current
reservations of the alley.
When looking at valid reservations, the function prints all valid reservations the customer has.
'''
def reservations(customer, alley):
    # give reservation options for the user
    print("You are now logged in as {}".format(customer.get_name()))
    print("Choose an option!\n1- make new reservation\n2- check current reservations\n3- cancel a current "
          "reservation\n4- exit the program")
    line = input()

    ongoing = True
    # get today's date and time to make sure no un-valid reservations will be booked.
    today = datetime.date.today()
    time_now = datetime.datetime.now()
    current_hour = time_now.time()

    skip = False

    # main loop that allows the user to keep inputting until the quit-command (3) is typed
    while ongoing:

        try:  # makes sure user inputs an integer
            option = int(line)
        except ValueError:
            print("Please input an integer.")
            line = input("1- make new reservation\n2- check current reservations\n3- cancel a current reservation\n4- "
                         "exit the program\n")
            skip = True

        if not skip:
            if option == 1:  # if user chooses to make a new reservation
                loop2 = True
                while loop2:  # choose a valid date
                    day = str(input("Please type the day you would like to book. In format: dd/mm/yyyy\n"))
                    parts = day.split("/")
                    if len(parts) == 3:  # check if input is correct
                        try:
                            if parts[2] != '2022':  # check if the reservation is made for 2022
                                print("It is only possible to book reservations for this year.")
                            else:
                                d = int(parts[0])
                                m = int(parts[1])
                                date = datetime.date(2022, m, d)  # create date-obj for the reservation
                                if date < today:  # check if date is valid
                                    print("This day has already passed. Please input a valid date.")
                                else:
                                    loop2 = False
                        except ValueError:
                            print("Please input a valid date.")
                    else:
                        print("Please input a valid date.")
                loop3 = True
                while loop3:  # choose a valid time
                    try:
                        hour = int(input("Please type the hour you would like to book (from 10-22)\n"))
                        if 10 <= hour <= 22:  # check if hour is valid for the alley
                            time = datetime.time(hour)
                            if date == today and time < current_hour:  # check if the our is in the future
                                print("This hour has already passed. Please input a valid hour.")
                            else:
                                loop3 = False
                        else:
                            print("Please choose a time within our working hours.")
                    except ValueError:
                        print("Please input a valid hour.")

                reservation_count = 0
                for reservation in alley.get_current_reservations():
                    if reservation.get_date() == date:
                        if reservation.time == time:
                            reservation_count += 1

                # check if there are available lanes & create the reservation
                if reservation_count < alley.get_num_lanes():
                    customer.add_reservation(date, time)
                    print("Your bowling lane is now reserved!")
                    print("Please choose another action.")
                    line = input("1- make new reservation\n2- check current reservations\n3- cancel a current "
                                 "reservation\n4- exit the program\n")
                else:
                    print("There are no available lanes at this date and time... please choose another date/time.")

            elif option == 2:  # if user chooses to see their current reservations
                customer_reservations = customer.get_reservations_list()
                printed = 0
                if reservations:  # check if user has any valid reservations and print them
                    for reservation in customer_reservations:
                        if reservation.valid():
                            print("You have a valid reservation on the day {} at {}.".format(reservation.get_date(),
                                                                                             reservation.get_time()))
                            printed += 1
                if printed == 0:
                    print("You have no current reservations. Press 1 to make a new one or 4 to exit the program.")
                    line = input()
                else:
                    print("You have {} current reservation(s) in total.".format(printed))
                    print("Choose another action!")
                    print(
                        "1- make new reservation\n2- check current reservations\n3- cancel a current reservation\n4- "
                        "exit the program")
                    line = input()
            elif option == 3:
                print("These are your currently valid reservations:")
                customer_reservations = customer.get_reservations_list()
                printed = 0
                options_delete = []
                if reservations:  # check if user has any valid reservations and print them
                    for reservation in customer_reservations:
                        if reservation.valid():
                            print("{} - You have a valid reservation on the day {} at {}.".format(printed,
                                                                                                  reservation.get_date(),
                                                                                                  reservation.get_time()))
                            options_delete.append(reservation)
                            printed += 1
                if printed == 0:
                    print("You have no current reservations. Press 1 to make a new one or 4 to exit the program.")
                    line = input()
                else:
                    incorrect = True
                    while incorrect:
                        try:
                            index = int(input("Type the index of the reservation you would like to cancel.\n"))
                            if 0 <= index < printed:
                                for r in alley.get_current_reservations():
                                    if r == options_delete[index]:
                                        r.change_valid()
                                        alley.get_current_reservations().remove(r)
                                incorrect = False
                        except ValueError:
                            print("Invalid input. Please enter a valid input:")
                    print("Your reservation has been cancelled.")
                    line = input(
                        "1- make new reservation\n2- check current reservations\n3- cancel a current reservation\n4- "
                        "exit the program\n")
            elif option == 4:  # if user chooses to quit the program
                ongoing = False  # ends the main loop of this function

            else:  # if user inputs and invalid command
                print("Incorrect command! Please input 1, 2, 3 or 4.")
                line = input()
        skip = False


'''
Main function to control the program and interact with the user. It gives input options and guides the user
through the program.
'''
def main():
    # load info from file
    end_program = 0
    file = 'saved_file.b'   # input the desired file here.
    alley = load_from_file(file)
    if not alley:
        print("Could not upload Bowling Alley information from file.")
        print("Exiting program...")
        end_program = 1

    if end_program == 0:
        now = datetime.datetime.now()  # get today's date and time to un-validate any expired reservations
        time_now = now.time()
        today = now.date()
        print(now)

        for reservation in alley.get_current_reservations():  # un-validate expired reservations
            if reservation.get_date() < today:
                reservation.change_valid()
                alley.get_current_reservations().remove(reservation)
            elif reservation.get_date() == today and reservation.get_time() < time_now:
                reservation.change_valid()
                alley.get_current_reservations().remove(reservation)

        # welcome user and give first instructions
        print("Welcome to our bowling reservation system!")
        print("Do you have an account with us? Type in:")

        customers = alley.get_customers()
        ongoing = True

        line = input("1- to log in\n2- to sign up\n3- to exit program\n")
        correct_input = False

        skip = False

        # main loop that handles user input (btw log in/sign up/quit)
        while ongoing:

            try:  # makes sure user inputs an integer
                choice = int(line)
            except ValueError:
                print("Please input an integer.")
                line = input("1- to log in\n2- to sign up\n3- to exit program\n")
                skip = True

            if not skip:
                if choice == 1:  # if user chooses to log in
                    customer = log_in(customers)  # call log in function
                    if customer is None:
                        line = input("Log in failed. Type 1 to log in with another email, 2 to sign up or 3 to "
                                     "exit:\n")
                    else:
                        reservations(customer, alley)  # call reservations function
                        line = 3
                elif choice == 2:  # if user chooses to sign up
                    sign_in(alley)  # call sign up function
                    cust_list = alley.get_customers()
                    reservations(cust_list[-1], alley)  # call reservations function
                    line = 3
                elif choice == 3:  # if user uses to quit
                    print("Saving changes to {}'s file...".format(alley.get_name()))
                    save_to_file(file, alley)  # save actions to file
                    print("Thank you for using the program! See you next time! Exiting...")
                    ongoing = False
                else:  # if user inputs invalid command
                    print("Incorrect command! Please input 1, 2 or 3.")
                    line = input()
            skip = False


main()
