import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

import components.editProfileAndPreference as editPandUi
import components.signUp


_username = ""


def switch_page(path)
    uic.loadUi(path, self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    signup = signUp.SignUpGUI()
    signup.show()
    signup.connect(lambda: switch_page('../assets/signup_ui.ui'))

    editPandUi.main(username)

    sys.exit(app.exec())

