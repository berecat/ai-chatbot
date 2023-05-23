import sys
sys.path.append('/home/ketolumin/Dev/aiven')

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog

import assets.bg_rcs
import assets.icon_rcs
import modules.db_manager as db

from sign_up import SignUpGUI
from main_page import MainPage
import util


class LoginGUI(QDialog):
    def __init__(self):
        super(LoginGUI, self).__init__()
        uic.loadUi('../assets/login_ui.ui', self)
        self.setFixedSize(self.size())

        self.login_button.clicked.connect(self.verify_results)
        self.signup_button.clicked.connect(self.sign_up)

    def verify_results(self):
        username = self.username_field_.text()
        pw = self.password_field_.text()

        rows = db.select_user(username)

        if len(rows) == 0:
            util.show_error_dialog(self, "Username does not exist.")
            return

        if pw not in rows[0]:
            util.show_error_dialog(self, "Incorrect password.")
            return 

        self.main_page = MainPage()
        self.main_page.show()
        self.close()

    def sign_up(self):
        self.sign_up = SignUpGUI()
        self.sign_up.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginGUI()
    login.show()
    sys.exit(app.exec())