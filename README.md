Password Generator
This project is a GUI-based password generator written in Python. It allows users to create random passwords with customizable options, including the inclusion of numbers and special characters. The user can specify the minimum length of the password, and the application will generate a password that meets the specified criteria.

Features
Generate random passwords with a specified minimum length.
Option to include or exclude numbers.
Option to include or exclude special characters.
User-friendly graphical interface built with Tkinter.

Installation
Clone the repository 
Run the application in vscode using github desktop *click "run python file" instead of just running it 

Usage
Open the application:

Run the password_generator.py script to open the password generator application.

Specify the minimum length:

Enter the desired minimum length for the password in the "Minimum Length" field.

Select options:

Check or uncheck the "Include Numbers" option to include or exclude numbers in the generated password.
Check or uncheck the "Include Special Characters" option to include or exclude special characters in the generated password.
Generate password:

Click the "Generate Password" button to generate a password. The generated password will be displayed in the application window.

Code Overview
generate_password function
This function generates a random password based on the specified criteria:

min_length: Minimum length of the password.
numbers: Boolean indicating whether to include numbers.
special_characters: Boolean indicating whether to include special characters.
The function ensures that the generated password meets the criteria specified by the user.

on_generate_password function
This function handles the button click event to generate a password. It retrieves user input, validates it, and displays an error message if the input is invalid. If the input is valid, it generates and displays the password.

Tkinter GUI
The application uses Tkinter to create a graphical user interface. The main components of the interface are:

Entry widget for specifying the minimum length of the password.
Checkbuttons for selecting options to include numbers and special characters.
Button to generate the password.
Label to display the generated password.
Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Credits
Kenley Hilaire: Project creator and developer.



