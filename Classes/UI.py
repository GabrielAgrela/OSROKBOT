import sys
from PyQt5 import QtWidgets, QtGui, QtCore

from action_sets import ActionSets
from game_automator import GameAutomator
import pygetwindow as gw

from window_handler import WindowHandler

class UI(QtWidgets.QWidget):
    def __init__(self, window_title, delay=0.2):
        super().__init__()
        self.game_automator = GameAutomator(window_title, delay)
        self.game_automator.signal_emitter.pause_toggled.connect(self.on_pause_toggled) # Connect the signal to the slot
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
        margin-left: 5px;
        margin-right: 5px;
        font-size: auto;
        font-weight: bold;
        min-width: 50px;
        min-height: 50px;
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
        border: 1px solid #4a4a4a !important;
        border-radius: 8px;
        padding: 5px;
        background-color: #3a3a3a !important;
        color: white !important; /* This sets the text color of non-selected items to white */
    }
    QComboBox::drop-down {
        background-color: #2a2a2a !important;
        border: 2px solid #4a90e2 !important;
        min-width: 22px;
        border-radius: 8px;
    }
    QComboBox::down-arrow {
        image: url(Media/UI/down_arrow.svg);
        padding-top: 2px;
        width: 13px;
        height: 13px;           
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
        self.close_button = QtWidgets.QPushButton('x')
        self.close_button.clicked.connect(self.close)
        self.close_button.setStyleSheet("""
            background-color: #3a3a3a;
            color: #f5f5f5;
            border: none;
            font-size: 24px;
            min-width: 5px !important;
            min-height: 5px !important;
            padding: 0px !important;
            padding-right: 10px !important;                            
            margin: 0px !important;
        """)
        #make title_bar_layout height 30
        self.title_bar.setFixedHeight(30)
        title_bar_layout.addWidget(self.close_button)

        # Status label
        self.status_label = QtWidgets.QLabel(' Ready')
        self.status_label.setStyleSheet("color: #4a90e2; font-weight: bold; text-align: center;")
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        # Button Layout
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setAlignment(QtCore.Qt.AlignCenter)
        # Create the Play Button
        self.play_button = QtWidgets.QPushButton()
        self.play_icon = QtGui.QIcon("Media/UI/play_icon.svg")
        self.play_button.setIcon(self.play_icon)
        self.play_button.setIconSize(QtCore.QSize(24, 24))
        self.play_button.clicked.connect(self.start_automation)
        button_layout.addWidget(self.play_button)

        # Create the Stop Button
        self.stop_button = QtWidgets.QPushButton()
        self.stop_icon = QtGui.QIcon("Media/UI/stop_icon.svg")
        self.stop_button.setIcon(self.stop_icon)
        self.stop_button.setIconSize(QtCore.QSize(24, 24))
        self.stop_button.clicked.connect(self.stop_automation)
        button_layout.addWidget(self.stop_button)

        # Create the Pause/Unpause Button
        self.pause_button = QtWidgets.QPushButton()
        self.pause_icon = QtGui.QIcon("Media/UI/pause_icon.svg")
        self.unpause_icon = QtGui.QIcon("Media/UI/play_icon.svg")
        self.pause_button.setIcon(self.pause_icon)
        self.pause_button.setIconSize(QtCore.QSize(24, 24))
        self.pause_button.clicked.connect(self.toggle_pause)
        button_layout.addWidget(self.pause_button)


        # Title for Action Sets
        action_set_title = QtWidgets.QLabel("Action Sets:")
        action_set_title.setStyleSheet("""
            color: #4a90e2;
            font-size: 16px;    
            font-weight: bold;                                                                              
            margin-top: 10px;
            margin-bottom: 0px !important;
        """)

        # Action sets dropdown
        self.action_set_combo_box = QtWidgets.QComboBox()
        self.action_set_combo_box.setStyleSheet("""
            color: #fff;
        """)
        self.action_set_names = ["farm_rss","farm_food","farm_wood","farm_stone","farm_gold", "farm_barb", "lyceum", "lyceumMid", "train_troops"]
        self.action_set_combo_box.addItems(self.action_set_names)

        # Checkbutton for captcha
        self.check_captcha_checkbutton = QtWidgets.QCheckBox("Check for Captcha")
        self.check_captcha_checkbutton.setStyleSheet("""
            font-size: 14px;
            margin-top: 10px;
        """)
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

        self.play_button.show()
        self.stop_button.hide()
        self.pause_button.hide()
        self.setFixedSize(180, 300)



        self.show()
        WindowHandler().activate_window()

    def update_position(self):
        target_window = gw.getWindowsWithTitle(self.target_title)
        #check if target window is active
        if target_window:
            target_window = target_window[0]
            self.move(target_window.left - self.width(), target_window.top)

    def on_pause_toggled(self, is_paused): # This is the slot
        if is_paused:
            self.status_label.setText(' Paused')
            self.status_label.setStyleSheet("color: orange;")
            self.pause_button.setIcon(self.unpause_icon) # Update the button icon
            self.stop_button.show()
            self.pause_button.show()
            self.play_button.hide()
        else:
            self.status_label.setText(' Running')
            self.status_label.setStyleSheet("color: green;")
            self.pause_button.setIcon(self.pause_icon) # Update the button icon
            self.play_button.hide()
            self.pause_button.show()
            self.pause_button.show()



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
            self.status_label.setText(' Running')
            self.status_label.setStyleSheet("color: green;font-weight: bold;")
        self.play_button.hide()
        self.stop_button.show()
        self.pause_button.show()

    def stop_automation(self):
        self.game_automator.stop()
        self.status_label.setText(' Ready')
        self.status_label.setStyleSheet("color: red;font-weight: bold;")
        self.play_button.show()
        self.stop_button.hide()
        self.pause_button.hide()

    def toggle_pause(self):
        self.game_automator.toggle_pause()

    def closeEvent(self, event):
        self.stop_automation()
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = UI('Rise of Kingdoms')
    sys.exit(app.exec_())
