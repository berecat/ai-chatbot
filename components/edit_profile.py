from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

import assets.bg_rcs
import assets.icon_rcs
import modules.db_manager as db

from main_page import MainPage
import util


class ProfileGUI(QMainWindow):
    def __init__(self, username):
        super(ProfileGUI, self).__init__()
        uic.loadUi('../assets/editpand_ui.ui', self)
        self.setFixedSize(self.size())
        self.username = username

        self.login_button.clicked.connect(self.verify_results)

    def verify_results(self):
        gender = self.gender_field.text()
        personality = self.personality_field.text()
        likes = self.gender_field.text()
        dislikes = self.dislikes_field.text()

        if gender == "" or likes == "" or dislikes == "" or personality == "":
            util.show_error_dialog(self, "Please fill in all fields.")
            return

        db.edit_user_profile(self.username, gender, personality, likes, dislikes)

        self.main_page = MainPage()
        self.main_page.show()
        self.close()

