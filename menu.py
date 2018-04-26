import datetime

from csv_manager import CsvManager


class Menu:

    # CONSTANTS
    DATE_FORMATS = {
        'iso 8601': {'UI format': 'yyyy-mm-dd',
                     'datetime format': '%Y-%m-%d'
                    },
        'uk':       {'UI format': 'dd/mm/yyyy',
                     'datetime format': '%d/%m/%Y'
                    },
        'us':       {'UI format': 'mm/dd/yyyy',
                     'datetime format': '%m/%d/%Y'
                    },
    }

    HEADERS = {
        'date': 'Date',
        'task_name': 'Task Name',
        'duration': 'Duration (minutes)',
        'notes': 'Notes'
    }

    DATASTORE_FILENAME = 'temp.csv'
    
    # STATUS VARIABLES
    quit = False

    # INITIALIZERS
    def __init__(self):
        self.OPTIONS = {
            'date format' : self.DATE_FORMATS['iso 8601'],
            'save format (date)'  : self.DATE_FORMATS['iso 8601'],
        }

        menu = self.main_menu()
        while self.quit != True:
            menu = menu()

    # MENU METHODS
    def main_menu(self):
        '''This is the root menu. The user selects which activity to perform
        and then the method returns the function for the activity.
        '''
        inputs = {
            'a' : {'text': 'Add new entry',
                   'function': self.add_entry},
            's' : {'text': 'Search in existing entries',
                   'function': self.search_entries},
            'o' : {'text': 'Options',
                   'function': self.options},
            'q' : {'text': 'Quit program',
                   'function': self.quit_program}
        }
        while True:
            print("\nWORK LOG")
            print("What would you like to do?")
            for key, value in inputs.items():
                print("{}) {}".format(key, value['text']))
            user_entry = input("> ").lower()

            if user_entry not in inputs.keys():
                continue
            
            print(user_entry)
            print(inputs[user_entry])

            return inputs[user_entry]['function']

    def add_entry(self):
        '''This is the menu where the user can add a task that was completed
        '''
        while True:
            print("\nADD ENTRY")
            print("Date of the Task")
            user_entry = self.date_entry()
            if user_entry[0] != None:  # error
                print(user_entry[0])
                continue
            else:
                date = user_entry[1]
            print("Name of the Task") 
            input_text = input("Enter the name of the task > ")
            task_name = input_text
            print("Time spent")
            input_text = input("Enter a whole number of minutes (rounded) ")
            time_spent = input_text
            print("Notes")
            input_text = input("(Optional, leave blank for none) ")
            notes = input_text
            # call method to write data to file
            csvm = CsvManager()
            file_data = [{
                self.HEADERS['date']: date,
                self.HEADERS['task_name']: task_name,
                self.HEADERS['duration']: time_spent,
                self.HEADERS['notes']: notes
            }]
            csvm.save_csv(file_data, self.DATASTORE_FILENAME)
            return self.main_menu

    def options(self):
        '''This is the menu where the user can specify user-configurable
        options
        '''
        print('OPTIONS')
        print("Choose a display date format")
        
        menu_choices = list(self.DATE_FORMATS.keys())
        menu_size = len(menu_choices)

        for i in range(len(menu_choices)):
            print("({}) - {}".format(i + 1, menu_choices[i]))
        input_text = input("> ")
        if input_text in [str(x) for x in range(1, menu_size + 1)]:
            choice = int(input_text) - 1
            choice = menu_choices[choice]
            print("You chose: {}".format(choice))
            self.OPTIONS['date format'] = self.DATE_FORMATS[choice]
            print('going back to main menu')
        else:
            print("Invalid entry, returning to main menu")
        return self.main_menu

    def search_entries(self):
        '''This is the search menu. The user selects how they want to search.
        '''
        inputs = {
            'd' : {'text': 'single Date',
                   'function': self.search_exact_date},
            'r' : {'text': 'date Range',
                   'function': self.search_date_range},
            't' : {'text': 'Time spent',
                   'function': self.search_time_spent},
            's' : {'text': 'text Search',
                   'function': self.search_text_search},
            'x' : {'text': 'regeX pattern search',
                   'function': self.search_regex_search},
            'b' : {'text': 'Back to main menu',
                   'function': self.main_menu}
        }
        while True:
            print("\nSEARCH ENTRIES")
            print("How would you like to search?")
            for key, value in inputs.items():
                print("{}) {}".format(key, value['text']))
            user_entry = input("> ").lower()

            print(user_entry)
            print(inputs[user_entry])

            if user_entry not in inputs.keys():
                continue
            print(inputs[user_entry]['function'])
            return inputs[user_entry]['function']

    def quit_program(self):
        print("Quitting")
        self.quit = True
    
    def search_exact_date(self):
        '''This is the menu where the user browses dates and entries and picks
        the date from a list
        '''
        print("\nSEARCH EXACT DATE")
        # load the csv
        csvm = CsvManager()
        csv_data = csvm.load_csv(self.DATASTORE_FILENAME)
        print(csv_data)
        date_records = self.get_column(csv_data,
                                       self.HEADERS['date'],
                                       unique=True)
        for i, value in enumerate(date_records):
            print("{}) {}".format(i + 1, value))
        user_input = input("> ")
        # perform input validation
        user_input = int(user_input) - 1
        selected_date = date_records[user_input]
        # when a date is selected, show all the entries with that date
        matching_records = self.get_matching_records(csv_data,
                                                     self.HEADERS['date'],
                                                     selected_date)
        for record in matching_records:
            if len(matching_records) == 1:
                self.display_entry(record, verbose=True)
            else:
                self.display_entry(record)
        print('going back to main menu')
        return self.main_menu
    
    def search_date_range(self):
        '''This is the menu where the user can enter a from date and to date
        and get back every entry from within that range
        '''
        print('SEARCH DATE RANGE')
        # get from_date
        # get to_date
        # loop through every loop in range (inclusive)
        #   enumerate entry
        
        print('going back to main menu')
        return self.main_menu
    
    def search_time_spent(self):
        '''This is the menu where the user enters the number of minutes a task
        took and be able to choose one to see entries from
        '''
        print('SEARCH BY TIME SPENT')
        print('going back to main menu')
        return self.main_menu

    def search_text_search(self):
        '''This is the menu where the user enters a text string and is presented
        with all entries containing that string in the task name or notes
        '''
        print('SEARCH USING TEXT STRING')
        print('going back to main menu')
        return self.main_menu
    
    def search_regex_search(self):
        '''This menu is just like `search_text_search` except the user provides
        a regex pattern instead of a text string
        '''
        print('REGEX')
        print('going back to main menu')
        return self.main_menu
    
    # Other UI Methods
    def display_entry(self, entry, verbose=False):
        '''This method displays a selected entry, showing:
        - date (read from file in iso 8601 and displayed in whatever is set in options)
        - task name
        - time taken
        - any notes
        '''
        date = entry[self.HEADERS['date']]
        task_name = entry[self.HEADERS['task_name']]
        time_taken = entry[self.HEADERS['duration']]
        notes = entry[self.HEADERS['notes']]
        if verbose:
            line1 = "{}: {}".format(date, task_name) 
            print(line1)
            print("-" * len(line1))
            print("{} minutes".format(time_taken))
            print("{}".format(notes))
        else:
            print("{} ({}m): {} | {}".format(date,
                                             time_taken,
                                             task_name,
                                             notes))

    # Helper Methods
    def validate_date_entry(self, date_string, date_format):
        '''Takes a date_string and date_format and attempts to create
        a valid datetime object with those imports.
        Returns a tuple in the form (error, datetime) where:
        - `error` is None if valid and a description of the error text if 
          invalid;
        - `datetime` is a datetime object if valid and None if invalid
        '''
        try:
            naive_datetime = datetime.datetime.strptime(date_string, 
                                                        date_format['datetime format'])
        except ValueError:
            error_text = "{date_string} is not a valid date in the format {date_format}"
            error_args = {"date_string": date_string,
                          "date_format": date_format['UI format']}
            return (error_text.format(**error_args), None)
        else:
            return (None, naive_datetime)
    
    def date_entry(self):
        '''This helper function asks for a date input in the user's preferred
        format and then returns that date as a naive datetime object
        '''
        date_format = self.OPTIONS['date format']
        input_text = "Please use the '{}' date format: "
        user_entry = input(input_text.format(date_format['UI format']))
        # validate date entry
        validated = self.validate_date_entry(user_entry, date_format)
        if validated[0] != None:  # error
            return validated
        else:
            save_format_date = self.OPTIONS['save format (date)']
            date_format = save_format_date['datetime format']
            date = validated[1].strftime(date_format)
            return (None, date)

    def get_column(self, data_set, field_title, unique=False):
        '''takes a data set and the name of a column and returns a list of all
        records in that column.
        
        If unique is set to True, returns only unique values (while
        preserving order)'''
        items = [row[field_title] for row in data_set] 
        if not unique:
            return items
        else:
            unique_items = []
            for item in items:
                if item not in unique_items:
                    unique_items.append(item)
            return unique_items
    
    def get_matching_records(self, data_set, field_title, value):
        '''takes a data set and the name of a column and a value and returns
        all the rows where the specified column has the specified value
        '''
        return [row for row in data_set if row[field_title] == value]







# ---------------------------

if __name__ == "__main__":

    menu = Menu()
