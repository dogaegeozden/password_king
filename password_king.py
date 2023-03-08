# LIBRARIES
# PySide2 modules
from PySide2.QtCore import QAbstractListModel, Qt
from PySide2.QtWidgets import QMenu, QApplication, QMainWindow, QDialog, QFileDialog, QAction, QLineEdit
from PySide2.QtGui import QPixmap, QIcon

# Builtin python modules
from sys import argv
from os import path, listdir, makedirs, remove
from random import choices, shuffle
from json import dump, load
from pathlib import Path
from logging import basicConfig, DEBUG, debug, disable, CRITICAL
from pyminizip import compress, uncompress
from shutil import rmtree
from webbrowser import open as wbopen
from re import compile

# GUIs
from user_interfaces.main_window_ui import Ui_MainWindow
from user_interfaces.password_generator_win_ui import Ui_PasswordGeneratorDialog
from user_interfaces.username_generator_win_ui import Ui_UsernameGeneratorDialog
from user_interfaces.credits_dialog_win_ui import Ui_CreditsDialog
from user_interfaces.login_win_ui import Ui_LoginWindow
from user_interfaces.create_a_new_safe_win_ui import Ui_CreateNewSafeDialog

# Resources
import resources_rc


# Configuring debugging feature code
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# GLOBAL VARIABLES
# Creating a variable called base_dir which leads to the current working directory.
base_dir = path.dirname(__file__)

# Creating a list called list_of_usernames
list_of_usernames = ["bob", "joe", "cristal", "gary", "john", "selena", "jason", "andrea"]

# Creating a list called list_of_small_letters
list_of_small_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Creating a list called list_of_capital_letters
list_of_capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Creating a list called list_of_numbers
list_of_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# Creating a list called list_of_symbols
list_of_symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", ",", ".", "<", ">", "/", "?", ";", ":"]

# Creating a variable called help_page_url which is a string equal to the help page's url
help_page_url = 'https://github.com/dogaegeozden/password_king#readme/'

# Creating a list called FILE_FILTERS.
FILE_FILTERS = [
    "Zip files (*.zip)",
    "All files (*)",
]

def main():
    """The main function which runs the entire application."""
    app = QApplication(argv)
    global login_win
    login_win = LoginWindow()
    login_win.show()
    app.exec_()

# CLASSES
# Creating a data class called PasswordDataModel to control how the data objects will be created/stored
class PasswordDataModel(QAbstractListModel):
    def __init__(self, passwords=None):
        super().__init__()
        # Creating a list called passwords
        self.passwords = passwords or []

    def data(self, index, role):
        """A function which specifiys the data object model"""
        if role == Qt.DisplayRole:
            object_name_text, username_text, password_text, the_url_text = self.passwords[index.row()]
            return object_name_text

    def rowCount(self, index):
        """A function which returns the number of rows from the passwords list's length"""
        return len(self.passwords)

# Creating a dialog class called CreditsDialog
class CreditsDialog(QDialog, Ui_CreditsDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loading the GUI
        self.setupUi(self)

# Creating a dialog class called CreateNewSafeDialog
class CreateNewSafeDialog(QDialog, Ui_CreateNewSafeDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loading the GUI
        self.setupUi(self)
        # Connecting the create_button menu item with the create_a_new_safe function in a way that the function will going to trigger with a trigger signal
        self.create_button.pressed.connect(self.create_a_new_safe)
    
    def create_a_new_safe(self):
        """A function which creates a new safe"""
        # Creating a regular expression to valide file names
        file_name_regex = compile(r'\w{1,24}')
        # Creating a regular expression to validate passwords
        password_regex = compile(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d@$!#%*?&]{20,40}')
        
        # Creating a boolean variable called password_validity_status which is False by default
        password_validity_status = False
        # Creating a boolean variable called file_name_validity_status which is False by default
        file_name_validity_status = False

        # Creating a variable called new_safe_file_name from the safe_name_line_edit widget's text value
        new_password_file_name = str(self.safe_name_line_edit.text())
        # Creating a variable called new_safe_password from the password_line_edit widget's text value
        new_safe_password = str(self.password_line_edit.text())

        # Checking if pattern matchin is not returning None
        if file_name_regex.search(new_password_file_name) != None:
            # Checking pattern macthing result is fully mathing with the new_password_file_name
            if file_name_regex.search(new_password_file_name).group() == new_password_file_name:
                # Setting file_name_validity_status to True
                file_name_validity_status = True
                # Creating a variable called new_password_file_name_with_extension by concatenating new_password_file_name with ".json"
                new_password_file_name_with_extension = f'{new_password_file_name}.json'
                # Creating a path which leads to the location where the password file will be stored temporarly
                new_password_file_path = str(Path(Path.home(), "Desktop", new_password_file_name_with_extension))
                # Searching the pattern in the new_safe_password and making sure it's not returning None
                if password_regex.search(new_safe_password) != None:
                    # Checking if the pattern macthing result is equal to new_safe_password. 
                    if password_regex.search(new_safe_password).group() == new_safe_password:
                        # Setting password_validity_status to True
                        password_validity_status = True
                        # Checking if both password_validity_status and file_name_validity_status is equal to True
                        if password_validity_status == True and file_name_validity_status == True:
                            # Creating a variable called new_safe_file_path by concatenating the home path, the destkop path, and the new_safe_file_name
                            new_safe_file_path = str(Path(Path.home(), "Desktop", f'{new_password_file_name}.zip'))
                            # Creating a new password file temporarly 
                            with open(new_password_file_path, "w") as new_password_file:
                                new_password_file.write("new file")
                            # Creating a password protected safe(zip)
                            compress(new_password_file_path, None, new_safe_file_path, new_safe_password, 9)
                            # Removing the temporary unprotected password file.
                            remove(new_password_file_path)
                            # Setting the info_label widget's style sheet
                            self.info_label.setStyleSheet(u"#info_label {color: lightgreen;}")
                            # Setting the info_label widget's text
                            self.info_label.setText(f'Password protected safe has been created at {new_safe_file_path}')
                            # Setting the tool tip of the info_label widget
                            self.info_label.setToolTip(new_safe_file_path)
                        else:
                            # Setting the info_label widget's text
                            self.info_label.setText('File name or password is not valid.')
                            # Setting the info_label widget's style sheet
                            self.info_label.setStyleSheet(u"#info_label {color: red;}")
                    else:
                        # Setting the info_label widget's text
                        self.info_label.setText('Password must be between 20-40 characters long, must include capital letters, small letters, numbers and can only include the following symbols @$!#%*?&')
                        # Setting the info_label widget's style sheet
                        self.info_label.setStyleSheet(u"#info_label {color: red;}")
                else:
                    # Setting the info_label widget's text
                    self.info_label.setText('Password must be between 20-40 characters long, must include capital letters, small letters, numbers and can only include the following symbols @$!#%*?&')
                    # Setting the info_label widget's style sheet
                    self.info_label.setStyleSheet(u"#info_label {color: red;}")
            else:
                # Setting the info_label widget's text
                self.info_label.setText('Safe file name must be in between 1-24 characters long. And can only include letters, numeric digits, or the underscore character.')
                # Setting the info_label widget's style sheet
                self.info_label.setStyleSheet(u"#info_label {color: red;}")
        else:
            # Setting the info_label widget's text
            self.info_label.setText('Safe file must be in between 1-24 characters long. And can include only letters, numeric digits, or the underscore character.')
            # Setting the info_label widget's style sheet
            self.info_label.setStyleSheet(u"#info_label {color: red;}")


# Creating a dialog class called EditDataUsernameGeneratorDialog
class EditDataUsernameGeneratorDialog(QDialog, Ui_UsernameGeneratorDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loading the GUI
        self.setupUi(self)
        # Connecting the generate_button with the generate_username function in a way that the function will going to trigger with press signal.
        self.generate_button.pressed.connect(self.generate_username)
        # Connecting the save_button with the save_the_username function in a way that the function will going to trigger with a press signal.
        self.save_button.pressed.connect(self.save_the_username)
        # Connecting the cancel_button with the close function in a way that the function will going to trigger with a press signal. Hint: In this close function is a building function which closes the window.
        self.cancel_button.pressed.connect(self.close)

    def capitalize_the_first_letter(self):
        """A function which capitalizes the first letter."""
        # Defining a global variable called capitalize
        global capitalize
        # Initializing the capitalize variable with the check state of the capitalize_checkbox
        capitalize = self.capitalize_checkbox.checkState()
        
        # Checking the if capitalize_checbox state is Unchecked
        if capitalize == "PySide2.QtCore.Qt.CheckState.Unchecked":
            # Setting the capitalize variable to False
            capitalize = False
        # Checking if capitalize_checbox state is Checked
        elif capitalize == "PySide2.QtCore.Qt.CheckState.Checked":
            # Setting capitalize variable to True
            capitalize = True

    def generate_username(self):
        """A function which generates a random user name"""
        # Creating a list called random username by selecting a random username from the list_of_random_usernames
        random_username = choices(list_of_usernames, k=1)
        # Creating a variable called capitalize_checkbox_state which is equal to the capitalize_checkbox widget's check state
        capitalize_checkbox_state = self.capitalize_checkbox.checkState()
        # Creating a variable called include_numbers_checkbox_state which is equal to the include_numbers_checkbox widget's check state
        include_numbers_checkbox_state = self.include_numbers_checkbox.checkState()
        
        # Checking if capitalize_checkbox widget's check state is equal to checked
        if capitalize_checkbox_state == 2:
            # Creating a random_username which's first letter is capital
            random_username = "".join(random_username).capitalize()
        
        # Checking if capitalize_checkbox widget's check state is equal to unchecked
        elif capitalize_checkbox_state == 0:
            # Creating a random username which's first letter is not capital
            random_username = "".join(random_username)

        # Checking the check state of the include_numbers_checkbox widget is equal to checked
        if include_numbers_checkbox_state == 2:
            # Creating a variable called random_number_amount which is equal to random integer in between 1 to 5
            random_number_amount = int(choices(list_of_numbers[1:5], k=1)[0])
            # Creating a variabe called random_numbers which is equal to a 1 to 5 character long number in string form
            random_numbers = "".join(choices(list_of_numbers, k=random_number_amount))
            # Concatenating the random_username string with the random_numbers string
            random_username += random_numbers

        # Setting username_line_edit widget's text to the random_username string 
        self.username_line_edit.setText(random_username)

    def save_the_username(self):
        """A function which updates the edit the object group view's user name edit line"""
        # Creating a variable called random_username from the username_line_edit widget's text value 
        random_username = self.username_line_edit.text()
        # Setting the eto_username_line_edit widget's text to the random_username which is located in the main_window 
        main_window.eto_username_line_edit.setText(random_username)
        # Closing the dialog
        self.close()

class EditDataPasswordGeneratorDialog(QDialog, Ui_PasswordGeneratorDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loading the GUI
        self.setupUi(self)
        # Connecting the generate_button with the generate_random_password function in a way that the function will going to trigger with a press signal
        self.generate_button.pressed.connect(self.generate_random_password)
        # Connecting the save_button with the update_eto_password_line_edit function in a way that the function will going to trigger with a press signal
        self.save_button.pressed.connect(self.update_eto_password_line_edit)
        # Connecting the cancel_button with the close function in a way that the function will going to trigger with a press signal. Hint: In this case close function is a built in function which closes the dialog
        self.cancel_button.pressed.connect(self.close)

    def update_eto_password_line_edit(self):
        """A function that gets the random password from password generators random password line edit area and updates the edit the password object's password line edit area with this value"""
        # Creating a variable called random_password from the password_line_edit widget's text value
        random_password = self.password_line_edit.text()
        # Setting the eto_password_line_edit widget's text value which is located in the main window, to random_password variable's value
        main_window.eto_password_line_edit.setText(random_password)
        # Closing the dialog
        self.close()

    def generate_random_password(self):
        """A function that generates a random password and then updates password generator's mainPGLEA area"""
        # Creating a variable called small_letters_count which is equal to small_letters_spin_box widget's value
        small_letters_count = self.small_letters_spin_box.value()
        # Creating a variable called capital_letters_count which is equal to capital_letters_spin_box widget's value
        capital_letters_count = self.capital_letters_spin_box.value()
        # Creating a variable called numbers_count which is equal to the numbers_spin_box widget's value
        numbers_count = self.numbers_spin_box.value()
        # Creating a variable called symbols_count which is equal to the symbols_spin_box widget's value
        symbols_count = self.symbols_spin_box.value()

        # Creating a list of random small letter
        random_small_letters = choices(list_of_small_letters, k=small_letters_count)

        # Creating a list of random capital letters
        random_capital_letters = choices(list_of_capital_letters, k=capital_letters_count)

        # Creating a list of random list of random numbers
        random_numbers = choices(list_of_numbers, k=numbers_count)

        # Creating a list of random list_of_symbols
        random_symbols = choices(list_of_symbols, k=symbols_count)

        # Creating a new list from random small letters, random capital letters, random number and random symbols
        new_password_char_list = random_small_letters + random_capital_letters + random_numbers + random_symbols

        # Suffling the new_password_char_list
        shuffle(new_password_char_list)

        # Creating a new password from the new_password_char_list list
        random_password = "".join(new_password_char_list)

        # Setting the password_line_edit widget's text
        self.password_line_edit.setText(random_password)


class CreateDataUsernameGeneratorDialog(QDialog, Ui_UsernameGeneratorDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loading the GUI
        self.setupUi(self)
        # Connecting the generate_button with the generate_random_username function in a way that the function will going to trigger with press signal
        self.generate_button.pressed.connect(self.generate_random_username)
        # Connecting the cancel_button with the close function in a way that the function will going to trigger with press signal. Hint: In this case close function is a built in function which closes the dialog
        self.cancel_button.pressed.connect(self.close)
        # Connecting the save_button with the save_the_random_username function in a way that the function will going to trigger with a press signal
        self.save_button.pressed.connect(self.save_the_random_username)

    def capitalize_the_first_letter(self):
        # Creating a global variable called capitalize
        global capitalize
        # Initializing the capitalize function with the capitalize_checkbox widget's check state
        capitalize = self.capitalize_checkbox.checkState()
        # Checking if capitalize_checkbox's check state is unchecked
        if capitalize == "PySide2.QtCore.Qt.CheckState.Unchecked":
            # Setting the capitalize variable's value to False
            capitalize = False
        # Checking if capitalize_checkbox's check state is checked
        elif capitalize == "PySide2.QtCore.Qt.CheckState.Checked":
            # Setting the capitalize variable's value to True
            capitalize = True

    def generate_random_username(self):
        """A function which generates a random user name"""
        # Creating a list called random_username
        random_username = choices(list_of_usernames, k=1)
        # Creating a variable called capitalize_checkbox_state from the capitalize_checkbox widget's check state
        capitalize_checkbox_state = self.capitalize_checkbox.checkState()
        # Creating a variable called include_numbers_checkbox from the include_numbers_checkbox widget's check state
        include_numbers_checkbox = self.include_numbers_checkbox.checkState()
        # Checking the if the check state of the capitalize_checkbox widget is equal to checked
        if capitalize_checkbox_state == 2:
            # Creating a random_username which's first letter is capital
            random_username = "".join(random_username).capitalize()
        # Checking if the check state of the capitalize_checkbox widget is equal to unchecked
        elif capitalize_checkbox_state == 0:
            # Creating a random_username which's first letter is not capital
            random_username = "".join(random_username)
        # Checking if the check state of the include_numbers_checkbox widget is equal to checked
        if include_numbers_checkbox == 2:
            # Creating a variable called random_numbers_amount which is equal to random integer in between 1 to 5
            random_number_amount = int(choices(list_of_numbers[1:5], k=1)[0])
            # Creating a variabe called random_numbers which is equal to a 1 to 5 character long number in string form
            random_numbers = "".join(choices(list_of_numbers, k=random_number_amount))
            # Concatenating the random_username string with the random_numbers string
            random_username += random_numbers

        # Setting the username_line_edit widget's text to the random username that is generated by this function
        self.username_line_edit.setText(random_username)
            
    def save_the_random_username(self):
        """A function which updates the edit the object group view's user name edit line"""
        # Creating a variable called random_username from the username_line_edit widget's text
        random_username = self.username_line_edit.text()
        # Setting the cao_username_line_edit widget which is located in the main window text to the random_username variable's value
        main_window.cao_username_line_edit.setText(random_username)
        # Closing the dialog
        self.close()

class CreateDataPasswordGeneratorDialog(QDialog, Ui_PasswordGeneratorDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loading the GUI
        self.setupUi(self)
        # Connecting the generate_button with the generate_random_password function in a way that the function will going to trigger with a press signal.
        self.generate_button.pressed.connect(self.generate_random_password)
        # Connecting the save_button with the update_eto_line_edit function in a way that the function will going to trigger with a press signal
        self.save_button.pressed.connect(self.update_eto_line_edit)
        # Connecting the cancel_button with the close function in a way that the function will going to trigger with a press signal. Hint: In this case the close function is a built in function which closes the dialog
        self.cancel_button.pressed.connect(self.close)

    def update_eto_line_edit(self):
        """A function that gets the random password from password generators random password line edit area and updates the edit the password object's password line edit area with this value"""
        # Creating a variable called random_password which is equal to password_line_edit widget's text value
        random_password = self.password_line_edit.text()
        # Setting the cao_password_line_edit widget's text value which is located in the main window to random_password variable's value
        main_window.cao_password_line_edit.setText(random_password)
        # Closing the dialog window
        self.close()

    def generate_random_password(self):
        """A function that generates a random password and then updates password generator's mainPGLEA area"""
        # Creating a variable called small_letter_amount from the small_letters_spin_box widget's value
        small_letter_amount = self.small_letters_spin_box.value()
        # Creating a variable called capital_letter_amount from the capital_letters_spin_box widget's value
        capital_letter_amount = self.capital_letters_spin_box.value()
        # Creating a variable called number_amount from the numbers_spin_box widget's value
        number_amount = self.numbers_spin_box.value()
        # Creating a variable called symbol_amount
        symbol_amount = self.symbols_spin_box.value()
        # Creating a list called random_small_letters_list
        random_small_letters_list = choices(list_of_small_letters, k=small_letter_amount)
        # Creating a list called random_capital_letters_list
        random_capital_letters_list = choices(list_of_capital_letters, k=capital_letter_amount)
        # Creating a list called random_numbers_list
        random_numbers_list = choices(list_of_numbers, k=number_amount)
        # Creating a list called random_symbols_list
        random_symbols_list = choices(list_of_symbols, k=symbol_amount)
        # Creating a list called random_chars_list by appending random_small_letters_list, random_capital_letters_list, random_numbers_list and random_symbols_list lists to one another
        random_chars_list = random_small_letters_list + random_capital_letters_list + random_numbers_list + random_symbols_list
        # Suffleing the random_chars_list list
        shuffle(random_chars_list)
        # Creating a random password by creating a string from the random_chars_list list's items
        random_password = "".join(random_chars_list)
        # Setting the password_line_edit widget's text value
        self.password_line_edit.setText(random_password)

# Creating a MainWindow class
class MainWindow(QMainWindow, Ui_MainWindow):
    # Initializing the main window to make it self contained.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loading the GUI
        self.setupUi(self)
        # Creating a model from the PasswordDataModel class
        self.model = PasswordDataModel()
        # Setting the list_of_passwords_list_view list view's data model 
        self.list_of_passwords_list_view.setModel(self.model)
        # Loading the data
        self.load()
        # Connecting the credits_action help menu item with the show_credits_dialog function in a way that the function will going to trigger with a trigger signal
        self.credits_action.triggered.connect(show_credits_dialog)
        # Connecting the cao_add_button with the add function in a way that the function will going to trigger with a press signal
        self.cao_add_button.pressed.connect(self.add)
        # Connecting the cao_cancel_button with the cancel_creating function in a way that the function will going to trigger with a press signal
        self.cao_cancel_button.pressed.connect(self.cancel_creating)
        # Connecting the list_of_passwords_list_view list elements with the edit function in a way that the function will going to trigger with a click signal
        self.list_of_passwords_list_view.clicked.connect(self.edit)
        # Connecting the eto_cancel_button with the cancel_editing function in a way that the function will going to trigger with press signal
        self.eto_cancel_button.pressed.connect(self.cancel_editing)
        # Connecting the eto_generate_username_button with the show_eto_username_generator_dialog function in a way that the function will going to trigger with a press signal
        self.eto_generate_username_button.pressed.connect(self.show_eto_username_generator_dialog)
        # Connecting the eto_generate_password_button with the show_eto_password_generator_dialog function in a way that the function will going to trigger with a press signal
        self.eto_generate_password_button.pressed.connect(self.show_eto_password_generator_dialog)
        # Connecting the cao_generate_username_button with the show_cao_username_generator_dialog function in a way that the function will going to trigger with a press signal
        self.cao_generate_username_button.pressed.connect(self.show_cao_username_generator_dialog)
        # Connecting the cao_generate_password_button with the show_cao_username_generator_dialog function in a way that the function will going to trigger with a press signal
        self.cao_generate_password_button.pressed.connect(self.show_cao_password_generator_dialog)
        # Connecting the help_page_action menu bar item with the show_the_help_page function in a way that the function will going to trigger with a trigger signal
        self.help_page_action.triggered.connect(show_the_help_page)

    # Creating a contex menu.
    def contextMenuEvent(self, e):
        # Creating the context menu. Hint: This is the menu which opens when the user right clicks to the gui.
        self.context_menu = QMenu()
        # Creating a delete context menu button
        self.delete_button = QAction("Delete")
        # Creating a save_and_exit context menu button
        self.save_button = QAction("Save")
        # Connecting the delete_button with the delete function in a way that the function will going to trigger with a trigger signal.
        self.delete_button.triggered.connect(self.delete)
        # Connecting the save_and_exit button with the save function in a way that the function will going to trigger with a trigger signal.
        self.save_button.triggered.connect(self.save)
        # Adding the save_and_exit_button into the context menu
        self.context_menu.addAction(self.save_button)
        # Adding the delete_button into the context menu.
        self.context_menu.addAction(self.delete_button)
        # Showing the context_menu.
        self.context_menu.exec_(e.globalPos())

    def import_password_file(self):
        """A function which uses a file discovery dialog to replace the data.json file"""
        initial_filter = FILE_FILTERS[1]
        filters = ";;".join(FILE_FILTERS)

        chosen_password_file, selected_file_filter = QFileDialog.getOpenFileName(self, filter=filters, initialFilter=initial_filter,)
        with open(chosen_password_file, "r") as password_king_file:
            password_king_file_contents = password_king_file.read()

        with open(Path(base_dir, "password_folder", "data.json"), "w") as password_king_file:
            password_king_file.write(password_king_file_contents)
        self.load()

    def export_password_file(self):
        """A function which exports the password file from the password manager to the selected location with a file dialog"""
        caption = "" # Empty uses default caption.
        initial_directory = path.expanduser('~')
        inital_filter = FILE_FILTERS[1] # Select one from the list.
        filters = ";;".join(FILE_FILTERS)
        file_path_to_save, selected_filter = QFileDialog.getSaveFileName(
            self,
            caption=caption,
            directory=initial_directory,
            filter=filters,
            initialFilter=inital_filter,
        )

        with open(Path(base_dir, "password_folder", "data.json"), "r") as password_king_file:
            password_king_file_content = password_king_file.read()

        with open(file_path_to_save, "w") as password_king_file:
            password_king_file.write(password_king_file_content)

    def show_eto_username_generator_dialog(self):
        """A function which opens the edit data random username generator dialog box with a click signal"""
        dialog = EditDataUsernameGeneratorDialog()
        dialog.exec_()

    def show_eto_password_generator_dialog(self):
        """A function which opens the edit data random password generator dialog box with a click signal"""
        dialog = EditDataPasswordGeneratorDialog()
        dialog.exec_()

    def show_cao_username_generator_dialog(self):
        dialog = CreateDataUsernameGeneratorDialog()
        dialog.exec_()

    def show_cao_password_generator_dialog(self):
        dialog = CreateDataPasswordGeneratorDialog()
        dialog.exec_()

    def load(self):
        """A function that gets/loads passwords from the password json file"""
        try:
            with open(password_file_path, "r") as f:
                passwords_data = load(f)
                self.model.passwords = passwords_data
                remove(password_file_path)
        except Exception:
            pass

    def save(self):
        """A function which saves passwords in to the password json file"""
        # Opening the password file in write mode
        with open(password_file_path, "w") as f:
            # Writing the json data in to file
            data = dump(self.model.passwords, f)
        
        # Creating a variable called initial_filter which is equal to second element of the FILE_FILTERS list 
        inital_filter = FILE_FILTERS[1] # Select one from the list.
        # Creating a string called filters by concatenating the list elements of FILE_FILTERS list
        filters = ";;".join(FILE_FILTERS)
        # Getting the file path of the location where user wants to save the file using a QFileDialog 
        file_path_to_save = str(QFileDialog.getSaveFileName(self, dir=str(Path(Path.home(), "Documents")), filter=filters, selectedFilter=inital_filter,)[0])
        # Checking if the file is ending with ".zip"
        if file_path_to_save.endswith(".zip"):
            # Doing nothing
            pass
        # Checking if the file doesn't ending with ".zip"
        else:
            # Adding ".zip" to the end of the file path
            file_path_to_save = f'{str(QFileDialog.getSaveFileName(self, dir=str(Path(Path.home(), "Documents")), filter=filters, selectedFilter=inital_filter,)[0])}.zip'
        # Creating a password protected compressed folder.
        compress(password_file_path, None, file_path_to_save, zip_password, 9)
        # Delete the password file for security
        remove(password_file_path)

    def add(self):
        """Add an item to password objects list, getting the text from the QLineEdit fields and then clearing them after the job."""
        # Get the object name from the create an object name line edit text area
        object_name_text = self.cao_object_name_line_edit.text().strip()
        # Get the user name from the create an object user name line edit text area
        username_text = self.cao_username_line_edit.text().strip()
        # Get the password form the create an object password line edit text area
        password_text = self.cao_password_line_edit.text().strip()
        # Get the url from the create an object url line edit text area
        the_url_text = self.cao_url_line_edit.text().strip()
        # Creating a list called list_of_object_names
        list_of_object_names = [ str(self.model.passwords[0][i]) for i in range(len(self.model.passwords)) ]
        # Making sure application is not creating an object which has no name, which is already exists or which's name is equal to " "
        if object_name_text != "" and object_name_text != " " and object_name_text not in list_of_object_names:
            # Accessing to the passwords list via the model
            self.model.passwords.append((object_name_text, username_text, password_text, the_url_text))
            # Triggering refresh
            self.model.layoutChanged.emit()
            # Clearing the input areas
            self.cao_object_name_line_edit.setText("")
            self.cao_username_line_edit.setText("")
            self.cao_password_line_edit.setText("")
            self.cao_url_line_edit.setText("")

    def delete(self):
        """A function which deletes password objects"""
        # Creating a list from the selected indexes in list_of_passwords_list_view
        indexes = self.list_of_passwords_list_view.selectedIndexes()
        # Checking if any of the list items has been selected. Hint: Indexes is a single-item list in single-select mode.
        if indexes:
            # Creating a variable called index which is the selected item's identifier in string form 
            index = indexes[0]
            # Removing the object
            del self.model.passwords[index.row()]
            # Triggering refresh
            self.model.layoutChanged.emit()
            # Clearing the selection in the list_of_passwords_list_view
            self.list_of_passwords_list_view.clearSelection()
            # Clearing the input areas
            self.eto_object_name_line_edit.setText("")
            self.eto_username_line_edit.setText("")
            self.eto_password_line_edit.setText("")
            self.eto_url_line_edit.setText("")

    def edit(self):  # Not an index, i is a QListItem
        """A function that sets the selected password's data in to QLineEdit widgets."""
        # Creating a list from the selected indexes in list_of_passwords_list_view
        indexes = self.list_of_passwords_list_view.selectedIndexes()
        # Checking if any of the list items has been selected. Hint: Indexes is a single-item list in single-select mode.
        if indexes:
            # Creating a variable called index which is the selected item's identifier in string form 
            index = indexes[0]
            # Setting eto_object_name_line_edit widget's text from the password file by accessing it's properties using the selection index and a positional index number
            self.eto_object_name_line_edit.setText(self.model.passwords[index.row()][0])
            # Setting eto_username_line_edit widget's text from the password file by accessing it's properties using the selection index and a positional index number
            self.eto_username_line_edit.setText(self.model.passwords[index.row()][1])
            # Setting eto_password_line_edit widget's text from the password file by accessing it's properties using the selection index and a positional index number
            self.eto_password_line_edit.setText(self.model.passwords[index.row()][2])
            # Setting eto_url_line_edit widget's text from the password file by accessing it's properties using the selection index and a positional index number
            self.eto_url_line_edit.setText(self.model.passwords[index.row()][3])
            # Connecting the eto_update_button with teh update function in a way that the function will going to trigger with a pressed signal
            self.eto_update_button.pressed.connect(self.update)

    def update(self):
        """A function that updates the passwords in the password json file"""
        # Loading the password data
        self.load()
        # Try to update password
        try:
            # Creating a list from the selected indexes in list_of_passwords_list_view
            indexes = self.list_of_passwords_list_view.selectedIndexes()
            # Checking if any of the list items has been selected. Hint: Indexes is a single-item list in single-select mode.
            if indexes:
                # Creating a variable called index which is the selected item's identifier in string form 
                index = indexes[0]
                # Creating a variable called new_object_name from the eto_object_name_line_edit widget's text value
                new_object_name = self.eto_object_name_line_edit.text()
                # Creating a variable called new_username from the eto_username_line_edit widget's text value
                new_username = self.eto_username_line_edit.text()
                # Creating a variable called new_password from the eto_password_line_edit widget's text value
                new_password = self.eto_password_line_edit.text()
                # Creating a variable called new_url from the eto_url_line_edit widget's text value
                new_url = self.eto_url_line_edit.text()
                # Changing the password object's object name to new_object_name
                self.model.passwords[index.row()][0] = new_object_name
                # Changing the password object's username to new_username
                self.model.passwords[index.row()][1] = new_username
                # Changing the password object's pasword to new_password
                self.model.passwords[index.row()][2] = new_password
                # Changing the password object's url to new_url
                self.model.passwords[index.row()][3] = new_url
                # Triggering refresh
                self.model.layoutChanged.emit()
                # Clearing the selection in the list_of_passwords_list_view list view
                self.list_of_passwords_list_view.clearSelection()
                # Clearing the input areas
                self.eto_object_name_line_edit.setText("")
                self.eto_username_line_edit.setText("")
                self.eto_password_line_edit.setText("")
                self.eto_url_line_edit.setText("")
                self.eto_info_label.setText("")
        
        # Instructing the computer about what to do when the app fails to update the passwords.
        except:
            # Changing the eto_info_label widget's text
            self.eto_info_label.setText("Try to save first")
            # Changing the eto_info_label widget's style sheet
            self.eto_info_label.setStyleSheet(u"#eto_info_label {color: red;}")

    def cancel_editing(self):
        """A function that clears the edit object QLineEdit Widgets and cancels the selection"""
        # Clearing the input areas
        self.eto_object_name_line_edit.setText("")
        self.eto_username_line_edit.setText("")
        self.eto_password_line_edit.setText("")
        self.eto_url_line_edit.setText("")
        # Clearing the selection in the list_of_passwords_list_view
        self.list_of_passwords_list_view.clearSelection()

    def cancel_creating(self):
        """A function which cancels object creation"""
        # Clearing the input areas
        self.cao_object_name_line_edit.setText("")
        self.cao_username_line_edit.setText("")
        self.cao_password_line_edit.setText("")
        self.cao_url_line_edit.setText("")
        # Clearing the selection in the list_of_passwords_list_view
        self.list_of_passwords_list_view.clearSelection()

# Creating a MainWindow class called LoginWindow
class LoginWindow(QMainWindow, Ui_LoginWindow):
    # Initializing the window to make it self contained.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loading the GUI
        self.setupUi(self)
        # Loading the data
        self.load()
        # Connecting the select_the_zip_file_button with the select_the_zip_file function in a way that the function will going to trigger with a pressed signal
        self.select_the_zip_file_button.pressed.connect(self.select_the_zip_file)
        # Connecting the unlock_button with the unlock_the_safe function in a way that the function will going to trigger with a press signal
        self.unlock_button.pressed.connect(self.unlock_the_safe)
        # Connecting the credits_action menu bar item with the show_credits_dialog function in a way that the function will going to trigger with a trigger signal
        self.credits_action.triggered.connect(show_credits_dialog)
        # Connecting the help_page_action menu bar item with the show_the_help_page function in a way that the function will going to trigger with a trigger signal
        self.help_page_action.triggered.connect(show_the_help_page)
        # Connecting the create_a_new_safe_action menu bar item with the show_create_a_new_safe_dialog
        self.create_a_new_safe_action.triggered.connect(self.show_create_a_new_safe_dialog)
        # Connecting the display_the_password with the change_echo_mode function in a way that the function will going to trigger with a pressed signal
        self.eye_button.pressed.connect(self.change_echo_mode)

    def change_echo_mode(self):
        """A function which changes the echo mode to hide and display the password"""
        # Creating a variable called echo_mode which is equal to the password_line_edit wiget's echo mode
        echo_mode = self.password_line_edit.echoMode()
        # Checking if the echo mode of the password_line_edit widget is Password
        if echo_mode == QLineEdit.EchoMode.Password:
            # Changing the widget's echo mode to Normal
            self.password_line_edit.setEchoMode(QLineEdit.EchoMode.Normal)
            # Creating an icon
            open_eye_icon = QIcon()
            # Adding pixmap to the icon
            open_eye_icon.addPixmap(QPixmap(str(Path(base_dir, "icons", "visibility_black_24dp.svg"))))
            # Setting the eye_button's icon
            self.eye_button.setIcon(open_eye_icon)
        # Checking if the echo mode of the password_line_edit widget is not Password
        else:
            # Changing the widget's echo mode to Password
            self.password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
            # Creating an icon
            half_eye_icon = QIcon()
            # Adding pixmap to the icon
            half_eye_icon.addPixmap(QPixmap(str(Path(base_dir, "icons", "visibility_off_black_24dp.svg"))))
            # Setting the eye_button's icon
            self.eye_button.setIcon(half_eye_icon)

    def show_create_a_new_safe_dialog(self):
        """A function which opens the create a new safe dialog"""
        dialog = CreateNewSafeDialog()
        dialog.exec_()

    def select_the_zip_file(self):
        """A function which allows users to select a file from the file system with a grafical user interface"""
        # Creating a variable called initial_filter which is equal to the FILE_FILTERS list's first element
        initial_filter = FILE_FILTERS[0]
        # Concatenating FILE_FITLERS list's elements together by putting ";;" in between them
        filters = ";;".join(FILE_FILTERS)
        # Creating a global variable called chosen_zip_file
        global chosen_zip_file
        # Allowing the user select a file using QFileDialog
        chosen_zip_file = QFileDialog.getOpenFileName(self, dir=str(Path.home()), filter=filters, selectedFilter=initial_filter,)[0]
        # Checking if path exists.
        if path.exists(chosen_zip_file) == True:
            # Setting zip_file_path_label widget's text
            self.zip_file_path_label.setText(chosen_zip_file)
            # Setting zip_file_path_label widget's tool tip so, users can see the full text by hovering over the text
            self.zip_file_path_label.setToolTip(chosen_zip_file)

    def load(self):
        """A function that gets/loads passwords from the password king file"""
        # Try to execute the code which is inside the try block
        try:
            # Opening the password_file_path in read mode
            with open(password_file_path, "r") as f:
                # Loading the json data in to the passwords list
                self.model.passwords = load(f)
        # Instructing the computer about what to do if it failt to execute the code which is inside the try block
        except Exception:
            # Skipping without doing anything.
            pass

    def unlock_the_safe(self):
        """A function which unlocks the password protected zip file, read the password file's contents and shows the main window"""
        # Creating a boolean called unlock_validity_status which False by default
        unlock_validity_status = False

        # Creating a code block which reads the password from the password_line_edit_text widget, tries to unlock the zip and sets the unlock_validity_status to True.
        try:
            # Creating a global variable called zip_password
            global zip_password
            # initializing the zip_password variable with the password_line_edit widget's text value
            zip_password = self.password_line_edit.text()
            # Checking if the password_folder is not empty
            if len(str(Path(base_dir, "password_folder"))) != 0:
                # Removing the tree after password_folder path
                rmtree(str(Path(base_dir, "password_folder")))
            # Creating a new directory caleld password_folder if it's not already exists    
            makedirs(str(Path(base_dir, "password_folder")), exist_ok=True)
            # Uncompressing the password protected zip file
            uncompress(chosen_zip_file, zip_password, str(Path(base_dir, "password_folder")), 9)
            # Creating a variable called password_file_name from the file which is located inside the password_folder
            password_file_name = listdir(str(Path(base_dir, "password_folder")))[0]
            # Creating a global variable called password_file_path
            global password_file_path
            # Initializing the variable with a path which leads to the password_file
            password_file_path = str(Path(base_dir, "password_folder", password_file_name))
            # Checking if password_folder is not empty
            if len(listdir(Path(base_dir, "password_folder"))) != 0:
                # Creating a boolean called unlock_validtiy_status which is True by default
                unlock_validity_status = True
            # Checking if the password_folder is empty. Hint: If the password_folder is empty it means application failed to unlock the folder
            else:
                # Setting the info_label widget's text
                self.info_label.setText("Wrong password")
                # Setting the info_label widget's style sheet
                self.info_label.setStyleSheet(u"#info_label {color: red;}")
            
        # Instructing the computer about what to do if the application fails to execute the code inside the try block
        except Exception:
            # Setting the info_label widget's text
            self.info_label.setText("Wrong password")
            # Setting the info_label widget's style sheet
            self.info_label.setStyleSheet(u"#info_label {color: red;}")

        if unlock_validity_status == True:
            # Closing all windows
            QApplication.closeAllWindows()
            # Creating a global variable called main_window
            global main_window
            # Creating a variable caleld main_window using the MainWindow class
            main_window = MainWindow()
            # Opening the main window
            main_window.show().exec_()
            # Deleting the file password file after reading it's contents for security
            remove(password_file_path)

def show_the_help_page():
    """A function which opens the help page in the default browser"""
    wbopen(help_page_url)

def show_credits_dialog():
    """A function which opens the credits dialog window"""
    dialog = CreditsDialog()
    dialog.exec_()

# Evaluate if the source is being run on its own or being imported somewhere else. With this conditional in place, your code can not be imported somewhere else.
if __name__ == '__main__':
    main()


