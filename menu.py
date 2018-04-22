import datetime

class Menu:

    # CONSTANTS
    DATE_FORMATS = {
        'default': {'UI format': 'yyyy-mm-dd',
                     'datetime format': '%Y-%m-%d'
                   },
        'uk':      {'UI format': 'dd/mm/yyyy',
                    'datetime format': '%d/%m/%Y'
                   },
        'us':      {'UI format': 'mm/dd/yyyy',
                    'datetime format': '%m/%d/%Y'
                   },
    }
    
    # STATUS VARIABLES
    quit = False

    # INITIALIZERS
    def __init__(self):
        self.OPTIONS = {
            'date format' : self.DATE_FORMATS['default']
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
            'd' : {'text': 'exact Date',
                   'function': self.search_exact_date},
            'r' : {'text': 'Range of dates',
                   'function': self.search_date_range},
            's' : {'text': 'exact Search',
                   'function': self.search_exact_search},
            'x' : {'text': 'use regeX pattern',
                   'function': self.search_regex},
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
        '''This is the menu where the user specifies a date to search by
        '''
        while True:
            print("\nSEARCH EXACT DATE")
            print("Enter the date")
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
            
            # call method to write data to file
            return self.main_menu
    
    def search_date_range(self):
        print('SEARCH_DATE_RANGE')
        print('going back to main menu')
        return self.main_menu
    
    def search_exact_search(self):
        print('SEARCH EXACT')
        print('going back to main menu')
        return self.main_menu
    
    def search_regex(self):
        print('REGEX')
        print('going back to main menu')
        return self.main_menu

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
