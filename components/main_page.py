import sys
sys.path.append('/home/ketolumin/Dev/aiven')
import typing

import assets.bg_rcs
import assets.icon_rcs

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream


class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        uic.loadUi('../assets/app_ui.ui', self)
        self.setFixedSize(self.size())
        
        self.sidebar_full_shown.hide()
        self.content_pane.setCurrentIndex(0)
        self.db_icon_button.setChecked(True)
    
    def on_content_pane_currentChanged(self, index):
        btn_list = self.sidebar_icon_only.findChildren(QPushButton) \
        + self.sidebar_full_shown.findChildren(QPushButton)

        for btn in btn_list:
            if index in [2,3]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)
            
    def on_db_icon_button_toggled(self):
        self.content_pane.setCurrentIndex(0)

    def on_db_fullshown_button_toggled(self):
        self.content_pane.setCurrentIndex(0)
        
    def on_c_icon_button_toggled(self):
        self.content_pane.setCurrentIndex(1)
        
    def on_c_fullshown_button_toggled(self):
        self.content_pane.setCurrentIndex(1)

