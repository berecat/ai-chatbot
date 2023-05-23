import sys
sys.path.append('/home/ketolumin/Dev/aiven')

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog

import assets.bg_rcs
import assets.icon_rcs
import modules.db_manager as db

from edit_profile import ProfileGUI
import util

class SignUpGUI(QDialog):
    def __init__(self):
        super(SignUpGUI, self).__init__()
        uic.loadUi('../assets/signup_ui.ui', self)
        self.setFixedSize(self.size())
        self.login_button_.clicked.connect(self.verify_results)

    def verify_results(self):
        username = self.username_field_.text()
        password = self.password_field_.text()
        re_enter_password = self.repassword_field.text()

        # check if not empty
        if password == "" or re_enter_password == "":
            util.show_error_dialog(self, "Please fill in all fields.")
            return

        # check if password is the same
        if password != re_enter_password:
            util.show_error_dialog(self, "Passwords do not match.")
            return

        if not db.create_user(username, password):
            util.show_error_dialog(self, "Username already exists.")
            return

        self.edit_profile = ProfileGUI(username)
        self.edit_profile.show()
        self.close()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     signup = SignUpGUI()
#     signup.show()
#     sys.exit(app.exec())