from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
import assets.bg_rcs
import assets.icon_rcs


class SignUpGUI(QDialog):
    def __init__(self):
        super(SignUpGUI, self).__init__()
        uic.loadUi('../assets/signup_ui.ui', self)
        self.setFixedSize(self.size())
        self.show()

        self.login_button.clicked.connect(self.verify_results)

    def verify_results(self):
        password = self.password_field.text()
        re_enter_password = self.reenterpassword_field.text()

        # check if not empty
        if password == "" or re_enter_password == "":
            show_error_dialog(self, "Please fill in all fields.")
            return

        # check if password is the same
        if password != re_enter_password:
            show_error_dialog(self, "Passwords do not match.")
            return


def show_error_dialog(parent, message):
    error_dialog = QMessageBox(parent)
    error_dialog.setIcon(QMessageBox.Critical)
    error_dialog.setWindowTitle("Error")
    error_dialog.setText(message)
    error_dialog.exec_()


def main():
    app = QApplication([])
    window = SignUpGUI()
    app.exec_()


main()
