from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from modules.personnel import Student, Advisor
import modules.db as db


def get_checked_advisors(checkboxes: dict) -> list:
    checked_boxes = []
    for adv_id, checkbox in checkboxes.items():
        if checkbox.isChecked():
            checked_boxes.append(checkbox.text())
    return checked_boxes


def get_advisor_name_surname(advisor):
    """Returns advisor's name and surname separately"""
    name_surname = advisor.split()
    return name_surname[0], name_surname[1]


class Academy(QMainWindow):
    """GUI class responsible for connecting GUI elements with database functionality
    and handling the app behaviour"""

    def __init__(self) -> None:
        """Initialize database, UI and connect buttons with methods"""
        super().__init__()
        db.create_data()

        self.ui = loadUi("ui/academy.ui", self)
        self.stackedWidget.setCurrentIndex(0)

        self.checkboxes = {1: self.ui.checkBox,
                           2: self.ui.checkBox_2,
                           3: self.ui.checkBox_3,
                           4: self.ui.checkBox_4,
                           5: self.ui.checkBox_5}

        self.ui.pushButton_8.clicked.connect(self.add_student)
        self.ui.pushButton_2.clicked.connect(self.search_student_by_advisor)
        self.ui.pushButton.clicked.connect(self.go_to_search_page)
        self.ui.pushButton_3.clicked.connect(self.go_home)

    def go_home(self) -> None:
        """Return to home page from search page"""
        self.stackedWidget.setCurrentIndex(0)

    def go_to_search_page(self):
        """Switch to student search"""
        self.stackedWidget.setCurrentIndex(1)

    def add_student(self):
        name = self.ui.lineEdit.text()
        surname = self.ui.lineEdit_2.text()

        if name != '' and surname != '':
            # Create student object but don't save to database yet
            student = Student(name, surname)
            # Get list of selected advisors for a student
            selected_advisors = get_checked_advisors(self.checkboxes)

            if len(selected_advisors) > 0:
                student.create()

                for advisor in selected_advisors:
                    advisor_name, advisor_surname = get_advisor_name_surname(advisor)
                    advisor_id = student.get_advisor_id(advisor_name, advisor_surname)
                    student.add_advisor_student_relation(advisor_id)

                self.ui.label_10.setStyleSheet("color: green; background-color: transparent")
                self.ui.label_10.setText('Success')

            else:
                self.ui.label_10.setStyleSheet("color: red; background-color: transparent")
                self.ui.label_10.setText('Please add advisor')

        else:
            self.ui.label_10.setStyleSheet("color: red; background-color: transparent")
            self.ui.label_10.setText('Enter student name and surname')

    def search_student_by_advisor(self):
        # Clear table widget if there's any content
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)

        advisor = self.ui.comboBox_2.currentText()
        advisor_name, advisor_surname = get_advisor_name_surname(advisor)
        advisor_id = self.ui.comboBox_2.currentIndex() + 1

        advisor_obj = Advisor(advisor_name, advisor_surname)
        students = advisor_obj.get_students(advisor_id)

        column_names = ['ID', 'Name', 'Surname']
        self.ui.tableWidget.setRowCount(advisor_obj.get_students_count(advisor_id))
        self.ui.tableWidget.setColumnCount(len(column_names))
        self.ui.tableWidget.setHorizontalHeaderLabels(column_names)

        for row_idx, student in enumerate(students):
            for col_idx, cell_data in enumerate(student):
                item = QTableWidgetItem(str(cell_data))
                self.ui.tableWidget.setItem(row_idx, col_idx, item)

        # Set the background color of the header row and column to transparent
        header_style = """QHeaderView::section { background-color: lightblue; }"""
        self.ui.tableWidget.horizontalHeader().setStyleSheet(header_style)
        self.ui.tableWidget.verticalHeader().setStyleSheet(header_style)

        self.ui.label_8.setText(f'Total students: {len(students)}')
