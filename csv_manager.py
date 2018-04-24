import csv

class CSVManager:

    def load_csv(self, filename, delimiter=',', quotechar='"'):
        '''Opens the specified file. If the specified file is not found,
        prompts the user for an alternative filename.
        Accepts optional arguments for:
        `delimiter`
        `quotechar`
        In case the CSV is encoded with a different format
        Turns each row of the file into a list where each element corresponds
        to a column in the CSV file.
        '''
        csv_data = None
        while csv_data is None:
            try:
                file_handle = open(filename, 'r')
            except FileNotFoundError:
                print("{} not found.".format(filename))
                print("please try an alternative filename")
                filename = input("> ")
            else:
                csv_data = []
                csv_reader = csv.reader(file_handle, 
                                        delimiter=delimiter,
                                        quotechar=quotechar)
                for line in csv_reader:
                    csv_data.append(line)
                file_handle.close()
        return csv_data
    
    def save_file(self, file_data, filename):
        file_handle = open(filename, 'a')
        file_handle.write('hello, world') # do we need to add a trailing newline?
        file_handle.close()

# -----------------------------

if __name__ == "__main__":
    print("Tests")

    print("Test1")
    filename = "test.csv"
    csv_manager = CSVManager()
    csv_data = csv_manager.load_csv(filename)

    for row in csv_data:
        print(row)