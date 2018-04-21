class Menu:

    quit = False

    def __init__(self):
        menu = self.main_menu()
        while self.quit != True:
            menu = menu()

    def main_menu(self):
        '''This is the root menu. The user selects which activity to perform
        and then the method returns the function for the activity.
        '''
        inputs = {
            'a' : {'text': 'Add new entry',
                   'function': self.add_entry},
            's' : {'text': 'Search in existing entries',
                   'function': self.search_entries},
            'q' : {'text': 'Quit program',
                   'function': self.quit_program}
        }
        while True:
            print("WORK LOG")
            print("What would you like to do?")
            for key, value in inputs.items():
                print("{}) {}".format(key, value['text']))
            user_entry = input("> ").lower()

            if user_entry not in inputs.keys():
                continue
            
            return inputs[user_entry]['function']

    def add_entry(self):
        print('ADD ENTRY')
        print('going back to main menu')
        return self.main_menu

    def search_entries(self):
        print('SEARCH ENTRIES')
        print('going back to main menu')
        return self.main_menu

    def quit_program(self):
        print("Quitting")
        self.quit = True

# ---------------------------

if __name__ == "__main__":

    menu = Menu()
