import sys
from PyQt5 import QtWidgets, QtGui, QtCore

from action_sets import ActionSets
from game_automator import GameAutomator
import pygetwindow as gw

from window_handler import WindowHandler

class UI(QtWidgets.QWidget):
    def __init__(self, window_title, delay=0):
        super().__init__()
        self.game_automator = GameAutomator(window_title, delay)
        self.action_sets = ActionSets(game_automator=self.game_automator)
        self.target_title = window_title
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_position)
        self.timer.start(10)
        # Colors and styles
        self.setStyleSheet("""
    QWidget {
        background-color: #2a2a2a;
    }
    QPushButton {
        background-color: #3a3a3a; 
        color: #f5f5f5;             
        border: 2px solid #4a90e2;  
        border-radius: 8px;
        padding: 5px;
        font-size: auto;
        font-weight: bold;
        min-width: 100px;
        min-height: 30px;
    }
    QPushButton:hover {
        background-color: #4a4a4a;  
        border: 2px solid #357ab2;  
    }
    QLabel {
        font-size: 18px;
        color: #f5f5f5;
    }
    QComboBox {
        font-size: 16px;
        border: 1px solid #4a4a4a;
        border-radius: 8px;
        padding: 5px;
        background-color: #3a3a3a;
        color: #f5f5f5;
        selection-background-color: #4a90e2;
        selection-color: white;
    }
    QCheckBox {
        font-size: 16px;
        color: #f5f5f5;
    }
""")

        # Title Bar
        self.title_bar = QtWidgets.QWidget()
        self.title_bar.setStyleSheet("""
            background-color: #3a3a3a;
            border: none;
        """)
        title_bar_layout = QtWidgets.QHBoxLayout(self.title_bar)
        title_bar_layout.setContentsMargins(0, 0, 0, 0)
        title_bar_layout.setSpacing(0)

        # Title Label
        self.title_label = QtWidgets.QLabel('OSROKBOT')
        self.title_label.setStyleSheet("""
            color: #f5f5f5;
            font-size: 14px;
            font-weight: bold;
            padding-left: 10px;
        """)
        title_bar_layout.addWidget(self.title_label)
        title_bar_layout.addStretch()

        # Close Button
        self.close_button = QtWidgets.QPushButton('X')
        self.close_button.clicked.connect(self.close)
        self.close_button.setStyleSheet("""
            background-color: #3a3a3a;
            color: #f5f5f5;
            border: none;
            font-weight: bold;
            font-size: 20px;
            
            padding: 0px !important;
            padding-right: 10px !important;                            
            margin: 0px !important;
            text-align: right;
        """)
        #make title_bar_layout height 30
        self.title_bar.setFixedHeight(30)
        title_bar_layout.addWidget(self.close_button)

        # Status label
        self.status_label = QtWidgets.QLabel('Status: Ready')
        self.status_label.setStyleSheet("color: blue; font-weight: bold; text-align: center;")
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        # Button Layout
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.start_button = QtWidgets.QPushButton('Start')
        self.start_button.clicked.connect(self.start_automation)
        button_layout.addWidget(self.start_button)

        self.stop_button = QtWidgets.QPushButton('Stop')
        self.stop_button.clicked.connect(self.stop_automation)
        button_layout.addWidget(self.stop_button)

        self.pause_button = QtWidgets.QPushButton('Toggle Pause')
        self.pause_button.clicked.connect(self.toggle_pause)
        button_layout.addWidget(self.pause_button)


        # Title for Action Sets
        action_set_title = QtWidgets.QLabel("Action Sets:")
        action_set_title.setStyleSheet("font-size: 16px; font-weight: bold;")

        # Action sets dropdown
        self.action_set_combo_box = QtWidgets.QComboBox()
        self.action_set_names = ["farm_rss", "farm_barb", "lyceum", "lyceumMid"]
        self.action_set_combo_box.addItems(self.action_set_names)

        # Checkbutton for captcha
        self.check_captcha_checkbutton = QtWidgets.QCheckBox("Check for Captcha")
        self.check_captcha_checkbutton.setChecked(True)

        # Content Layout
        content_layout = QtWidgets.QVBoxLayout()
        content_layout.setContentsMargins(20, 20, 20, 20)
        
        content_layout.addWidget(self.status_label)
        content_layout.addLayout(button_layout)
        content_layout.addWidget(action_set_title)
        content_layout.addWidget(self.action_set_combo_box)
        content_layout.addWidget(self.check_captcha_checkbutton)

        # Main Layout
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.title_bar)
        layout.addLayout(content_layout)

        # Set main layout
        self.setLayout(layout)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle('OSROKBOT')

        self.start_button.show()
        self.stop_button.hide()
        self.pause_button.hide()
        self.setFixedSize(300, 300)
        
        self.show()
        WindowHandler().activate_window()

    def update_position(self):
        target_window = gw.getWindowsWithTitle(self.target_title)
        #check if target window is active
        if target_window:
            target_window = target_window[0]
            self.move(target_window.left - self.width(), target_window.top)


    def start_automation(self):
        if self.game_automator.is_paused():
            self.toggle_pause()
        selected_index = self.action_set_combo_box.currentIndex()
        if selected_index != -1:
            action_group = getattr(self.action_sets, self.action_set_names[selected_index])()
            actions_groups = [action_group]
            if self.check_captcha_checkbutton.isChecked():
                actions_groups.append(self.action_sets.emailtest())
            self.game_automator.start(actions_groups)
            self.status_label.setText('Status: Running')
            self.status_label.setStyleSheet("color: green;font-weight: bold;")
        self.start_button.hide()
        self.stop_button.show()
        self.pause_button.show()

    def stop_automation(self):
        self.game_automator.stop()
        self.status_label.setText('Status: Stopped')
        self.status_label.setStyleSheet("color: red;font-weight: bold;")
        self.start_button.show()
        self.stop_button.hide()
        self.pause_button.hide()

    def toggle_pause(self):
        self.game_automator.toggle_pause()
        if self.game_automator.is_paused():
            self.status_label.setText('Status: Paused')
            self.status_label.setStyleSheet("color: orange;")  # Change yellow to orange
            # If paused, hide the pause button and show the start button
            self.stop_button.show()
            self.pause_button.show()
            self.start_button.hide()
        else:
            self.status_label.setText('Status: Running')
            self.status_label.setStyleSheet("color: green;")
            # If resumed, show the pause button and hide the start button
            self.start_button.hide()
            self.pause_button.show()
            self.pause_button.show()

    def closeEvent(self, event):
        self.stop_automation()
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = UI('Rise of Kingdoms')
    sys.exit(app.exec_())
