#function to get user input and return in lowercase to avoid case sensitivity
def get_input():
    user_input = input("Please enter response: ")
    return user_input.lower()

# help function
def help_function():
    """
    The function contains valid commands the user can follow to make a valid booking attempts
    The function has evolved to be a function of understood commands
    """

    while True:
        user_input = get_input()
        if user_input == 'help':
            print(""" These are the commands you can use:
            help - gives you commands you can use
            doctor - to volunteer to be a tutor
            patient - to get assistance from a tutor
            make_slot - to confirm you are volunteering for the specified time
            book_slot - to confirm you are choosing to get help at the specified time
            choose_topic - to choose the topic you want to discuss during consultation
            cancel_booking - to cancel a booking
            cancel - to cancel an invalid action
            """)
            continue
        if user_input == 'cancel':
            #code to be added to take the necessary cancellation steps
            print("Your action has been cancelled.")
            continue
        #to make testing barable
        if user_input == 'off':
            print("shutting down")
            break
        else:
            continue

           
#function call
help_function()
