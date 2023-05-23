from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

import assets.bg_rcs
import assets.icon_rcs
import modules.db_manager as db

import util


class ProfileGUI(QMainWindow):
    def __init__(self, username):
        super(ProfileGUI, self).__init__()
        uic.loadUi('../assets/editpand_ui.ui', self)
        self.setFixedSize(self.size())
        self.username = username

        self.login_button.clicked.connect(self.verify_results)

    def verify_results(self):
        age = self.age_field.text()
        likes = self.likes_field.text()
        dislikes = self.dislikes_field.text()

        if age == "" or likes == "" or dislikes == "":
            util.show_error_dialog(self, "Please fill in all fields.")
            return

        db.edit_user_profile(self.username, int(age), likes, dislikes)

