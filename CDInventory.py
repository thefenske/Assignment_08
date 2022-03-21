#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# NFenske, 2022-Mar-20, added coding required to complete ToDOs
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:
        
    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
        
    methods:
        description:  creates a string in the defined formatting of the object
        __str__:  string method that invokes description method
        addCD:  appends the object to lstOfCDObjects
        
    """
    # -- Fields -- #

    # -- Constructor -- #
    def __init__(self, cd_id, cd_title, cd_artist):
        #   -- Attributes -- #
        self.__iden = cd_id
        self.__title = cd_title
        self.__artist = cd_artist

    # -- Properties -- #
    @property
    def iden(self):
        return self.__iden
    
    @iden.setter
    def iden(self, value):
        self.__iden = value
        
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        self.__title = value
        
    @property
    def artist(self):
        return self.__artist
    
    @artist.setter
    def artist(self, value):
        self.__artist = value

    # -- Methods -- #
    def description(self):
        return '{}, {}, {}'.format(self.iden, self.title, self.artist)
    
    def __str__(self):
        return self.description()
    
    def addCD(self):
        lstOfCDObjects.append(self)
        
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:
        
    properties:
        
    methods:
        read_file(file_name, table): -> None
        write_file(file_name): -> (table (a list of CD objects))
        
    """
    # Read data from file
    @staticmethod
    def read_file(file_name, table):
        try:
            table.clear()
            # open the file
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                # assign the values to variables
                cd_id = data[0]
                title = data[1]
                artist = data[2]
                # create a CD object
                CDobject = CD(cd_id, title, artist)
                CDobject.addCD()
            objFile.close()
        except FileNotFoundError:
            print('\nYour CD inventory is empty.\n')
            
    # Save data to file
    @staticmethod
    def write_file(file_name, table):
        objFile = open(file_name, 'w')
        for row in table:
            cd_input = row.description()
            objFile.write(cd_input + '\n')
        objFile.close()
        print("\nYour inventory was saved to the file.\n")
    
# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user
        
        Args:
            None.
            
        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s ,or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')

    @staticmethod
    def input_cd():
        """Function to ask the user for CD details to add to memory   
        """
        cd_id = ''
        #error handling to force user to input a number for the ID before continuing on
        validID = False
        while not validID:
            try:
                strID = int(input('Enter ID: ').strip())
            except ValueError:
                print('This is not an integer! Enter again!')
            else:
                validID = True
        title = input('Enter the CD\'s title: ').strip()
        artist = input('What is the Artist\'s name? ').strip()
        cd_id = int(strID)
        return cd_id, title, artist

# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start

FileIO.read_file(strFileName, lstOfCDObjects)

while True:
    # Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # let user exit program
    if strChoice == 'x':
        break
    # let user load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('Type \'yes\' to continue and reload from file. Otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.read_file(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('Canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # let user add data to the inventory
    elif strChoice == 'a':
        # ask user for new ID, CD Title and Artist
        strID, strAlbum, strArtist = IO.input_cd()
        CDobject = CD(strID, strAlbum, strArtist)
        # append the CD object to lstOfCDObjects
        CDobject.addCD()
        print('\nYour CD has been added to your inventory.\n')
        continue
    # show user current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue
    # let user save inventory to file
    elif strChoice == 's':
        # Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            # saves the data
            FileIO.write_file(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')