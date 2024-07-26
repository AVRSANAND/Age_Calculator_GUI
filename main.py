import sys
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton


class AgeCalculator(QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        # Create widgets
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()

        dob_label = QLabel("Date of Birth DD/MM/YYYY:")
        self.dob_edit = QLineEdit()

        calculator_button = QPushButton("Calculate Age")
        calculator_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(dob_label, 1, 0)
        grid.addWidget(self.dob_edit, 1, 1)
        grid.addWidget(calculator_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year
        dob = self.dob_edit.text()
        year_of_birth = datetime.strptime(dob, "%d/%m/%Y").date().year
        age = current_year - year_of_birth
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old.")


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
