import sys
import csv
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox

class RegistrationApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registration App")
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        background_image = QLabel(central_widget)
        background_image.setGeometry(0, 0, 800, 600)
        pixmap = QPixmap(r"D:\code\code\123.jpg")  # Add your image file here
        background_image.setPixmap(pixmap)

        self.registration_data = []

        self.layout = QVBoxLayout()

        self.name_label = QLabel("Name:")
        self.name_label.setStyleSheet("color: black;")
        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)

        self.plate_label = QLabel("Registration:")
        self.plate_label.setStyleSheet("color: black;")
        self.plate_input = QLineEdit()
        self.layout.addWidget(self.plate_label)
        self.layout.addWidget(self.plate_input)

        self.phone_label = QLabel("Phone number:")
        self.phone_label.setStyleSheet("color: black;")
        self.phone_input = QLineEdit()
        self.layout.addWidget(self.phone_label)
        self.layout.addWidget(self.phone_input)

        self.email_label = QLabel("Email:")
        self.email_label.setStyleSheet("color: black;")
        self.email_input = QLineEdit()
        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_input)


        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet("background-color: green; color: white;")
        self.submit_button.clicked.connect(self.submit_registration)
        self.layout.addWidget(self.submit_button)

        self.view_button = QPushButton("View Register")
        self.view_button.setStyleSheet("background-color: blue; color: white;")
        self.view_button.clicked.connect(self.view_register)
        self.layout.addWidget(self.view_button)

        central_widget.setLayout(self.layout)

    def submit_registration(self):
        name = self.name_input.text()
        plate_number = self.plate_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        fine = self.fine_input.text()

        if not all([]):
            QMessageBox.warning(self, "Empty Fielname, plate_number, phone, email, fineds", "Please fill in all the fields.")
            return

        self.registration_data.append([name, plate_number, phone, email, fine])

        with open(r"D:\code\code\database.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, plate_number, phone, email, fine])

        QMessageBox.information(self, "Success", "Registration successful!")

        self.clear_fields()

    def clear_fields(self):
        self.name_input.clear()
        self.plate_input.clear()
        self.phone_input.clear()
        self.email_input.clear()
        self.fine_input.clear()

    def view_register(self):
        with open(r"D:\code\code\database.csv", mode="r") as file:
            reader = csv.reader(file)
            data = list(reader)

        view_window = QDialog(self)
        view_window.setWindowTitle("View Register")
        view_window.setGeometry(100, 100, 700, 600)

        table_widget = QTableWidget()
        table_widget.setColumnCount(5)
        table_widget.setRowCount(len(data))

        for row, item_list in enumerate(data):
            for col, text in enumerate(item_list):
                item = QTableWidgetItem(text)
                table_widget.setItem(row, col, item)

        layout = QVBoxLayout()
        layout.addWidget(table_widget)
        view_window.setLayout(layout)

        view_window.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationApp()
    window.show()
    sys.exit(app.exec_())