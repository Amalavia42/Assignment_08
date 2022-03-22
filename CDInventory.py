#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignnment 08 - Working with classes and the overall concept of OOP [Object Oriented Programming]
# Change Log: Amalavia on 2022-Mar-21 at 1803 hrs
# Amalavia, 2022-Mar-21, created the file
# Amalavia, 2022-Mar-21, adding code in the TODO areas of the starter script.
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
        output = will create string values for the object we are creating.
        __str__: custom __str__ method which then calls the oputput method above.
        add_cds_lstobj: will add the object to the list of objects (lstOfCDObjects).
        txt: values are formatted as plain text.
        
    """
    # -- FIELDS -- #

    # -- CONSTRUCTOR -- #
    def __init__(self, cd_id, cd_title, cd_artist):
        # -- ATTRIBUTES --#
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
    
    # -- PROPERTIES --# 
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, ID):
        self.__cd_id = ID
    
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, title):
        self.__cd_title = title
    
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, artist):
        self.__cd_artist = artist
        
    # -- METHODS --#
    def output(self):
        return '{}, {}, {}'.format(self.cd_id, self.cd_title, self.cd_artist)
        
    def add_cds_lstobj(self):
        lstOfCDObjects.append(self)

    def __str__(self):
        return self.output()

    def text(self):
        return '{},{},{}'.format(self.cd_id, self.cd_title, self.cd_artist)

# -- PROCESSING -- # 
class FileIO:

    """Processing the data to and from a text file
    
    Save_inventory(file_name, lst_Inventory): -> None
    load_inventory(file_name): -> (a list of CD objects)
    """
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data reading in from a file to a list of objects

    Reads the data from file identified by file_name into a 2D table
    (list of objects) table one line in the file represents one object in the table.

        Args:
        file_name (string): name of file used to read the data from
        table (list of objects): 2D data structure (list of objects) that holds the data during runtime

        Returns:
        None.
        """
        try:
           table.clear()
           objFile = open(file_name, 'r')
           for line in objFile:
               data = line.strip().split(',')
               cd_id = data[0]
               cd_title = data[1]
               cd_artist = data[2]
               CDInfo = CD(cd_id, cd_title, cd_artist)
               CDInfo.add_cds_lstobj()
           objFile.close()
        except Exception:
            print('\nThere is no CD in the inventory')
            
    @staticmethod
    def write_file(file_name, table):
        """Function to save data to a given txt file
        Saving the data from the 2D talbe to txt file
    
        Args:
        file_name (string): name of the file that we are saving the data to
        table (list of objects): 2D data structure and contains the list of CDs for writing to file
        
        Rerturns:
        None
        """
        try:
            objFile = open(file_name, 'w')
            for item in table:
                Data = item.text()
                objFile.write(Data + '\n')
            objFile.close()
            print('\nYou have saved your CD Inventory to your txt file')
        except FileNotFoundError:
            print('\n There was an error processing your request. Please check the file path and try again')

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""
    
    # Code to show the menu to the user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
            """
    print('\nMenu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')
    
    # Code to capture user's choice
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x
            """
        # Error handling so that it will keep looping until user makes a correct selection out of the choices provided.
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            try:
                choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
                print()
            except Exception:
                print('That is an incorrect selection! Only choose from the provide options')
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
        for item in table:
            print(item)
        print('======================================')
        
    @staticmethod
    def input_data():
       """Request user input for ID, Title and Artist for the CD

       Args:
           None.

       Returns:
           strID = ID of the CD, int converted to string, input by the user
           strTitle = TTitle of the CD, which is a string, input by the user
           strArtist = Artist for the CD, which is a string, inputy by the user
       """
       # Included error handling if the user does not pick a numerical ID.
       cd_id = ''
       while True:
           try:
               cd_id = int(input('Please enter a number: ').strip())
               break
           except ValueError:
               print('The value entered is not a numerical ID. Please try again.')
       cd_title = input('What is the CD\'s title? ').strip()
       cd_artist = input('What is the Artist\'s name? ').strip()
       return cd_id, cd_title, cd_artist

# -- MAIN BODY OF THE SCRIPT --# [Calling our Classes]
# Load data from file into a list of CD objects when the script starts
FileIO.read_file(strFileName, lstOfCDObjects)

# Start main loop
while True:
    # Display menu to user
    IO.print_menu()
    # Process menu selection.
    strChoice = IO.menu_choice()
    
    # Process exiting the while loop first.
    if strChoice == 'x':
        break

    # Let the user load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.read_file(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # Show the user the current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)

    # Let the user add data to the inventory
    elif strChoice == 'a':
        # Ask user for new ID, CD Title and Artist
        strID, strTitle, strArtist = IO.input_data()
        # Create the object for the reqeustd information above and add to the function defined as add_cds_lstobj
        CDObject = CD(strID, strTitle, strArtist)
        CDObject.add_cds_lstobj()
        # Add item to the table
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    # Let the user save inventory to file
    elif strChoice == 's':
        # Display current inventory and ask user for confirmation to save the data.
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        
        # Process the choice made.
        if strYesNo == 'y':
       
            # Save the data
            FileIO.write_file(strFileName, lstOfCDObjects)
    else:
        print('General Error')
