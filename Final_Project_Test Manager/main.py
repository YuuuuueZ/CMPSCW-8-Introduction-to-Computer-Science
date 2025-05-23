# TODO 0: add an import statement to load the functions from functions.py
from functions import *


options = {'A': 'List all tasks',
           'L': 'List unfinished tasks',
           'D': 'Delete a task',
           'N': 'Add a new task',
           'U': 'Update a task',
           'Q': 'Quit this program'} # TODO 1: a dictionary to hold the program instructions
opt = None

test_tasks = [
    {
        "name": "Collect unicorn glitter",
        "info": "",
        "rank": 3,
        "due": '05/28/2042',
        "done": True
    },
    {
        'name': 'Build a time machine',
        'info': 'Clean the parabolic collector reflectors',
        'rank': 5,
        'due': '06/05/2042',
        'done': False
    },
    {
        "name": "Take a quantum leap",
        "info": "Ignore all safety rules for best results",
        "rank": 5,
        "due": '06/05/2042',
        "done": False
    }
]

while True:
    print("What would you like to do?")
    print_options(options) # TODO 2: define the function in the functions.py, uncomment, and call it
    opt = input("Enter a menu option\n::: ")
    opt = opt.upper() # to allow users to input lower- or upper-case letters

    if opt not in list(options.keys()): # TODO 3: check if the selection is missing from the options dictionary
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue

    print(f"You selected {opt} to {options[opt]}.") # TODO 4: map the selection to its text stored in the dictionary

    if opt == 'Q':  # TODO 5: quit the program
        print("Goodbye!\n")
        break       # TODO 6: exit the main `while` loop
    elif opt == "A":
        print_tasks_list(test_tasks, show_completed=True)
    elif opt == "L":
        print_tasks_list(test_tasks)
    elif opt == 'D':
        delete_helper(test_tasks)
    elif opt == 'N':
        add_helper(test_tasks)
    elif opt == 'U':
        update_helper(test_tasks)
    # ----------------------------------------------------------------
    # Pause before going back to the main menu
    input("::: Press Enter to continue")

print("Have a productive day!")