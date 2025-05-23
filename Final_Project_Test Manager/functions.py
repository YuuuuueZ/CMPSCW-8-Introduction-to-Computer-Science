def print_options(options_dict):
    """
    Given a dictionary, print the keys
    and values as the formatted options:
     {key} - {value}
    """
    for key, value in options_dict.items():
        print(f" {key} - {value}")

######## LIST OPTION ########
def print_task(task, name_only = False):
    """
    param: task (dict) - a dictionary object that is
            assumed to have the following string keys:
    - "name": a string with the task's name
    - "info": a string with the task's details/description
            (the field is not displayed if the value is empty)
    - "rank": an integer, representing the task's priority
    - "due": a valid date-string in the US date format:
            <MM>/<DD>/<YEAR>
    - "done": a Boolean representing whether a task is completed or not

    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the task is printed.
            Otherwise, displays the formatted task fields as requested.

    returns: None; only prints the task values
    """
    fields = ("info", "rank", "due", "done")
    print(f"{task['name']}") # the name of the task is always displayed
    if not name_only: # if we didn’t want to display only the name
        for f in fields:
            print(f' * {f} - {task[f]}')

def print_tasks_list(task_list, name_only=False, show_completed=False, show_idx=False):
    """
    param: task_list (list) - a list containing dictionaries with
                    the task data
    param: name_only (Boolean) - by default, set to False.
    If True, then only the name of the task is printed.
    Otherwise, displays the formatted task fields.
    Passed as an argument into the helper function.
    param: show_completed (Boolean) - by default, set to False.
    If False, then only the unfinished tasks are shown.
    If True, all tasks (completed as well as unfinished)
    are displayed.
    param: show_idx (Boolean) - by default, set to False.
    If False, then the index of the task is not displayed.
    Otherwise, displays the "{idx} - " before the
    task name.

    returns: None; only prints the task values from the task_list

    Helper functions:
    - print_task() to print individual tasks
    """
    print("-" * 50)
    num_shown = 0
    for idx, task in enumerate(task_list):  # process each task in the list
        if task["done"] and not show_completed:
            continue  # skip completed tasks
        if show_idx:  # if the index of the task needs to be displayed
            print(f"{idx} - ", end="")  # Hint: idx need not be the same as num_shown and use enumerate at for loop above
        print_task(task, name_only)
        num_shown += 1
    print(f"Showing {num_shown} results")
    print("-" * 50)


######## DELETE OPTION ########

def delete_helper(task_collection):
    """
    param: task_collection (list) - holds all tasks;
            maps an integer ID/index to each task object (a dictionary)

    The function warns the user and returns, if there's nothing to delete.
    The function displays all tasks to the user and interactively allows
    the user to select the task ID, which needs to be deleted.
    If an invalid option or a task ID was given, displays a warning and
    returns without modifying the collection.

    Helper functions:
    - print_tasks_list
    - print_task
    - delete_task

    returns: None; directly modifies task_collection to remove tasks.
    """
    if not task_collection:
        print("WARNING: there is nothing to delete.")
        return

    print("Which task would you like to delete?")
    print_tasks_list(task_collection, name_only=True, show_completed=True, show_idx=True) # # TODO: make sure to set each keyword parameter = True
    print("::: Enter the number corresponding to the task ID")
    print("::: or enter A to delete all tasks in the collection.")
    user_input = input("> ")
    if user_input == "A": ### only accept upper-case
        del task_collection[:] # Delete all tasks
        print("Success! Deleted all tasks!")
        return
    elif not user_input.isnumeric() : ### if the user didn't enter a number
        print(f'WARNING: \'{user_input}\' is an invalid option!')
        # TODO: implement the WARNING: '{...}' is an invalid option!
        return

    result = delete_task(task_collection, user_input)
    if type(result) == dict:
        print("Success! Deleted the task:")
        print_task(result)
    else: ### prints an error as the item with that ID is not found
        # TODO: implement the WARNING: '{...}' is not found!
        print(f'WARNING: \'{user_input}\' is not found!')


def delete_task(task_collection, task_id):
    """
    param: task_collection (list) - holds all tasks;
    an integer ID indexes each task (stored as a dictionary)
    param: ... (str) - a string that is supposed to represent
    an integer ID that indexes the task in the list

    returns:
    0 - if the collection is empty.
    -1 - if the provided parameter is not a string or if it is not a string
    that contains a valid integer >=0 representing the task’s position on the list.
    Otherwise, returns the item (dict) that was removed from the
    provided collection.
    """
    if not task_collection:
        return 0

    if type(task_id) != str or not task_id.isnumeric():
        return -1

    if len(task_collection) <= int(task_id) or int(task_id) < 0:
        return -1

    return task_collection.pop(int(task_id))

def is_valid_year(date_list):
    """
        The function ...
    """
    if type(date_list[2]) == str and len(date_list[2]) >= 3 and date_list[2].isdigit():
        year = int(date_list[2])
        return year >= 1000
    return False

def is_valid_month(date_list):
    """
        The function ...
    """
    if type(date_list[0]) == str and len(date_list[0]) >= 1 and date_list[0].isdigit():
        month = int(date_list[0])
        return 1 <= month <= 12
    return False

def days_in_feb(year):
    """
            The function ...
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 29
    else:
        return 28

def is_valid_day(date_list):
    """
    The function ...
    """
    if len(date_list) >= 2 and type(date_list[1]) == str and date_list[1].isdigit():
        day = int(date_list[1])
        if is_valid_month(date_list):
            month = int(date_list[0])
            if month in [1, 3, 5, 7, 8, 10, 12]:
                return 1 <= day <= 31
            elif month in [4, 6, 9, 11]:
                return 1 <= day <= 30
            elif month == 2:
                return 1 <= day <= days_in_feb(int(date_list[2]))
    return False

def is_valid_date(date_str):
    """
    param: date_str (str) - stores either an empty string
            or a date in the `MM/DD/YYYY` format

    If the string is not empty and has the 3 required
    date components, the function checks each date component
    using the helper functions.

    Helper functions:
    - is_valid_year - only checks the year (a str, only digits,
        contains 1000 or above)
    - is_valid_month - only checks the month (accepts both
        formats: when the month has a leading 0, e.g. "02"
        as well when it does not, e.g., just "2")
    - is_valid_day - checks that the month is valid before
        checking that day is also correct (calls days_in_feb());
        accepts both formats: when the day has a leading 0,
        e.g. "07", as well when it does not, e.g., just "7"
    - days_in_feb - is called in is_valid_day() if the
        provided month is Feb to check if the given day
        is correct

    returns: True, if date_str is empty;
    returns False if the date_str does not have the 3 required
        date components (formed by splitting on the slash character);
    otherwise, returns a Boolean value based on the result
    of the helper functions.
    """
    if not date_str:
        return True

    separate = date_str.split('/')
    if len(separate) != 3:
        return False
    else:
        return is_valid_year(separate) and is_valid_month(separate) and is_valid_day(separate)



def check_valid_field(field, value):
    """
    param: field (str) - the name of a task field to validate
    param: value (str) - the proposed value for the field

    The function checks that the field is one of the
    expected keys. Expected fields stored in the function are
    ("name", "info", "rank", "due", "done").

    If the field is valid, the function checks that the provided
    value is the correct STRING value for the provided field:
    * `"name"`: a 2 or more characters string with the task’s name.
    * `"info"`: can be an empty string; no further validation is needed.
    * `"due"`: a string storing the date in the `MM/DD/YYYY` format.
        The string can be empty if the task has no due date.
        Checked using is_valid_date()
    * `"rank"`: a string which can be empty or contain one of five
        Fibonacci numbers ('1', '2', '3', '5', '8').
    * `"done"`: a string that contains “y” or “n”

    Helper functions:
    - is_valid_date

    returns:
    the name of the field if the field name is not found or
    if the value for a given field is invalid;
    otherwise, returns "valid"

    """
    # TODO: check that the field name is valid
    expected_fields = ('name', 'info', 'rank', 'due', 'done')
    if field not in expected_fields:
        return field

    flag = field

    if field == 'name' and len(value) >= 2:
        flag = 'valid'
    if field == 'info':
        flag = 'valid'
    if field == 'due' and (value == '' or is_valid_date(value)):
        flag = 'valid'
    if field == 'rank' and (value == '' or value in ('1', '2', '3', '5', '8')):
        flag = 'valid'
    if field == 'done' and value in ('y', 'n'):
        flag = 'valid'

    return flag


def add_helper(tasks_list):
    """
    param: tasks_list (list) - holds all tasks;
            each task is a dictionary.

    Collects the necessary information from the user and
    attempts to create a new task entry. If the provided
    information was valid, adds the new task to the list.
    Prints the added task via the print_task().
    Otherwise, prints a warning:
    "WARNING: trying to set '{...}' to an invalid option '{...}'!"
    where the first ellipses map to a name of a field and
    the second one is the value that the user provided.

    Helper functions:
    - get_new_task
    - print_task
    - is_valid_date

    The function does not return anything.
    """
    new_task = {} # TODO: a temporary dictionary to hold user values

    task_fields = {
        "name": "* Enter at least 2 letters for the task name:",
        "info": f"* Enter additional information for this task:",
        "rank": f"* Enter the priority of this task (1, 2, 3, 5, 8):",
        "due": f"* Enter a valid date in the US date format (MM/DD/YEAR):",
        "done": f"* Is this task completed? y/n"
    }
    print("::: Enter the task information:")
    for key in list(task_fields.keys()):
        print(task_fields[key]) # display the prompt
        value = input("> ") # get the data
        new_task[key] = value # store it in the temporary dictionary
    # print("Validating") ### DEBUGGING

    # for key in new_task:
    #    print(f"{key}: '{new_task[key]}'")

    result = get_new_task(new_task) # Attempt to create a new task object
    if type(result) == dict:
        print("Success! Adding a new task:")
        tasks_list.append(result) # add the dictionary that was returned
        print_task(result) # print the task that was just added
    else:
        print(f"WARNING: trying to set '{result}' to an invalid option '{new_task[result]}'!")



def get_new_task(values_dict):
    """
    param: values_dict (dict) - a dictionary that holds
            STRING values for all keys

    Helper functions:
    - check_valid_field

    For each key and value in the provided dictionary, calls
    the check_valid_field() to verify that they are valid.
    Does not modify values_dict.

    returns: a NEW dictionary that stores the values from the values_dict
        converted to the correct type / value, after each necessary value
        was verified by the check_valid_field().
        The only field that needs conversion is "done", since it is
        supposed to be stored as a Boolean and "rank", stored as an
        int (if its possible to convert it from string).
    Otherwise, returns the name of the invalid key or the valid key that
    stores the invalid data.
    """
    for key, value in values_dict.items():
        if check_valid_field(key, value) != "valid":
            return key

    new_task = values_dict.copy() # Make a copy of the values
    # TODO: Convert the string to Boolean, based on if 'y' or 'n' is stored

    if values_dict['done'] == 'y':
        new_task['done'] = True
    else:
        new_task['done'] = False

    # TODO: Convert the string to int for 'rank' field if possible

    if values_dict['rank'].isdigit():
        new_task['rank'] = int(values_dict['rank'])
    elif values_dict['rank'] == '':
        new_task['rank'] = ''
    else:
        return 'rank'

    return new_task

def get_task(task_collection, index_str):
    """
    param: task_collection (list) - holds all tasks;
            maps an integer ID/index to each task object (a dictionary)
    param: ... (str) - a string that is supposed to represent
            an integer ID that corresponds to a valid index in the
            collection

    returns:
    0 - if the collection is empty.
    -1 - if the provided parameter is not a string or if it is not
    a valid integer

    Otherwise, convert the provided string to an integer;
    returns None if the ID is not a valid index in the list
    or returns the existing item (dict) that was requested.
    """
    if not task_collection:
        return 0

    if type(index_str) != str or not index_str.isdigit():
        return -1

    index = int(index_str)
    if index < 0 or index >= len(task_collection):
        return None

    return task_collection[index]

def update_task(task_dict, key, value):
    """
    param: task_dict (dict) - a valid task dictionary
    param: key (str) - a valid key in the dictionary
    param: value - a valid value, depending on the key

    Helper function:
    - check_valid_field - verifies the validity of the key
    and the value

    Note: Convert the value to Boolean if the key is 'done', based on if 'y' or 'n' is the value.
    Note: Remember that the field 'rank' is supposed to be stored as an integer (if possible)

    returns: the key if either the key or value is invalid;
    otherwise, returns an updated dictionary.
    """
    if check_valid_field(key, value) != 'valid':
        return key
    if key == 'done':
        if value == 'y':
            task_dict[key] = True
        else:
            task_dict[key] = False
    elif key == 'rank':
        if not value.isdigit():
            return key
        else:
            task_dict[key] = int(value)
    else:
        task_dict[key] = value

    return task_dict


def update_helper(task_collection):
    """
    param: task_collection (list) - holds all tasks;
            maps an integer ID/index to each task object (a dictionary)

    Helper functions:
    - print_tasks_list
    - print_task
    - print_options
    - get_task
    - update_task

    The function does not return anything.
    """
    if not task_collection:
        print("WARNING: there is nothing to update.")
        return

    print("Which task would you like to update?")
    print_tasks_list(task_collection, name_only=True, show_completed=True, show_idx= True) # TODO: make sure to set each keyword parameter = True
    print("::: Enter the number corresponding to the task ID:")
    task_id = input("> ") # get the user input

    selected_task = get_task(task_collection, task_id)
    if type(selected_task) == dict:
        print("Success! Found:")
        print_task(selected_task, name_only=True)  # display only the name of the task
    elif selected_task == 0:
        print("WARNING: there is nothing to update.")
        return
    elif selected_task == -1:
        print(f"WARNING: '{task_id}' is an invalid option!")
        return
    else:
        print(f"WARNING: '{task_id}' is not found!")
        return

    print("Which field would you like to update?")
    print_options(selected_task) # display the selected task object: its keys and values
    print("::: Enter the field name:")
    field_name = input("> ") # get the key as an input
    if field_name not in list(selected_task.keys()):
        print(f"WARNING: '{field_name}' is an invalid field!")
        return

    print(f"::: Enter the {field_name} information instead of '{selected_task[field_name]}':")
    new_value = input("> ") # get the data

    updated_task = update_task(selected_task, field_name, new_value) # send the specific task to update
    if type(updated_task) == dict:
        print("Success!")
        print_task(updated_task)
        # print(task_collection)
    else:
        print(f"WARNING: trying to set '{field_name}' to an invalid value '{new_value}'!") # error when trying to set the given key to an invalid value provided by the user