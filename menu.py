import datetime

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
    
    # STATUS VARIABLES
    quit = False

    # INITIALIZERS
    def __init__(self):
        self.OPTIONS = {
            'date format' : self.DATE_FORMATS['iso 8601']
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
            date_format = self.OPTIONS['date format']
            input_text = "Please use the '{}' date format: "
            user_entry = input(input_text.format(date_format['UI format']))
            # validate date entry
            validated = self.validate_date_entry(user_entry, date_format)
            if validated[0] != None:  # error
                print(validated[0])
                continue
            else:
                print(validated[1])

            print("Time spent")
            input_text = input("Enter a whole number of minutes (rounded) ")
            time_spent = input_text
            print("Notes")
            input_text = input("(Optional, leave blank for none) ")
            notes = input_text
            # call method to write data to file
            return self.main_menu

    def options(self):
        print('OPTIONS')
        print('going back to main menu')
        return self.main_menu

    def search_entries(self):
        '''This is the search menu. The user selects how they want to search.
        '''
        inputs = {
            'd' : {'text': 'single Date',
                   'function': self.search_exact_date},
            #'r' : {'text': 'date Range',
            #       'function': self.search_date_range},
            't' : {'text': 'Time spent',
                   'function': self.search_time_spent}
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
        print('going back to main menu')
        return self.main_menu
    
    def search_date_range(self):
        print('SEARCH DATE RANGE')
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
    def display_entry(self, entry):
        '''This method displays a selected entry, showing:
        - date (read from file in iso 8601 and displayed in whatever is set in options)
        - task name
        - time taken
        - any notes
        '''
        print("TO DO")

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






# ---------------------------

if __name__ == "__main__":

    menu = Menu()
