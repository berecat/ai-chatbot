import assets.bg_rcs
import assets.icon_rcs
import modules.db_manager as db
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow

_username = ""


class EditProfileAndPreferenceGUI(QMainWindow):
    def __init__(self):
        super(EditProfileAndPreferenceGUI, self).__init__()
        uic.loadUi('../assets/editpand_ui.ui', self)
        self.setFixedSize(self.size())
        self.show()

        self.login_button.clicked.connect(self.verify_results)

    def verify_results(self):
        global _username
        age = self.age_field.text()
        likes = self.likes_field.text()
        dislikes = self.dislikes_field.text()

        if age == "" or likes == "" or dislikes == "":
            show_error_dialog(self, "Please fill in all fields.")
            return

        db.edit_user_profile(_username, int(age), likes, dislikes)


def show_error_dialog(parent, message):
    error_dialog = QMessageBox(parent)
    error_dialog.setIcon(QMessageBox.Critical)
    error_dialog.setWindowTitle("Error")
    error_dialog.setText(message)
    error_dialog.exec_()


def main(username):
    global _username
    _username = username

    app = QApplication([])
    window = EditProfileAndPreferenceGUI()
    app.exec_()

main("CliGan")
