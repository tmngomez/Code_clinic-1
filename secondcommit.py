# help function
def help_function():
    """
    The function contains valid commands the user can follow to make a valid booking attempts
    """

    while True:
        user_input = input("Please enter response: ")
        if user_input == 'help':
            print(""" These are the commands you can use:
            help - gives you commands you can use
            doctor - to volunteer to be a tutor
            patient - to get assistance from a tutor
            make_slot - to confirm you are volunteering for the specified time
            book_slot - to confirm you are choosing to get help at the specified time
            choose_topic - to choose the topic you want to discuss during consultation
            cancel - to cancel an invalid action
            """)
            continue
        if user_input == 'cancel':
            print("Your action has been cancelled.")
            continue
        else:
            continue

#function call
help_function()
