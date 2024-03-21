import sys
from modules.guy import Academy
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Academy()

    window.setWindowTitle("TBC Academy")
    window.setWindowIcon(QIcon("assets/academy.png"))
    window.show()

    sys.exit(app.exec_())
