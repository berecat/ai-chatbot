from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog
import assets.bg_rcs
import assets.icon_rcs


class SignUpGUI(QDialog):
    def __init__(self):
        super(SignUpGUI, self).__init__()
        uic.loadUi('../assets/signup_ui.ui', self)
        self.setFixedSize(self.size())
        self.show()


def main():
    app = QApplication([])
    window = SignUpGUI()
    app.exec()


main()
