# Age Calculator

This is a simple Python application that calculates a person's age based on their date of birth. The graphical user interface (GUI) is built using PyQt6, and the project is developed using object-oriented programming (OOP) principles.

## Features

- Input for name
- Input for date of birth in DD/MM/YYYY format
- Button to calculate age
- Display of calculated age

## Requirements

- Python 3.6+
- PyQt6

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AVRSANAND/Age_Calculator_GUI.git
    cd Age_Calculator_GUI
    ```

2. Install the required packages:
    ```bash
    pip install PyQt6
    ```

## Usage

1. Run the application:
    ```bash
    python main.py
    ```

2. Enter the name and date of birth in the respective fields.

3. Click the "Calculate Age" button.

4. The calculated age will be displayed below the button.

## Object-Oriented Programming (OOP) Approach

This project is designed using OOP principles, ensuring modularity, reusability, and maintainability. 

- **Class-Based Structure:** The `AgeCalculator` class encapsulates the functionality and GUI elements of the application.
- **Inheritance:** The `AgeCalculator` class inherits from `QWidget`, a fundamental class for all GUI objects in PyQt6.
- **Encapsulation:** The properties and methods related to the age calculation and GUI are encapsulated within the `AgeCalculator` class.

## Code Overview

The main logic of the application is in the `main.py` file. Here's a brief explanation of the code:

- The `AgeCalculator` class inherits from `QWidget` and sets up the GUI.
- The GUI includes labels, text input fields (`QLineEdit`), and a button (`QPushButton`).
- The `calculate_age` method calculates the age based on the current year and the input date of birth.
- The application is run by creating an instance of `QApplication` and `AgeCalculator`, and then executing the application loop with `sys.exit(app.exec())`.

## Example

![image](https://github.com/user-attachments/assets/4efa5cc7-04bd-4fee-be89-70d254a769fe)


## Acknowledgments

- [PyPI Python Package Index -> PyQt6](https://pypi.org/project/PyQt6/)
- [PyQt6 documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
