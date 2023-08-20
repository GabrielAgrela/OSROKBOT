import sys
from PyQt5 import QtWidgets, QtGui, QtCore

from action_sets import ActionSets
from game_automator import GameAutomator
import pygetwindow as gw
import time
from window_handler import WindowHandler
from global_vars import GlobalVars, GLOBAL_VARS

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
        width: 22px;
        height: 22px;
    }
    QPushButton:hover {
        background-color: #4a4a4a;  
        border: 2px solid #357ab2;  
    }
    QLabel {
        font-size: 16px;
        color: #f5f5f5;
        background-color: transparent;
        text-align: left !important;                
        
        
    }
    QComboBox {
        
        border: 2px solid #4a90e2; 
        border-radius: 8px;
        
        padding: 3px;
        font-size: Auto;
        background-color: #3a3a3a !important;
        color: white !important; /* This sets the text color of non-selected items to white */
    }
    QComboBox::drop-down {
        background-color: #2a2a2a !important;
        border: 2px solid #4a90e2 !important;
        width: 10px;
        border-radius: 5px;
    }
    QComboBox::down-arrow {
        image: url(Media/UI/down_arrow.svg);
        padding-top: 2px;
        width: 10px;
        height: 10px;           
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
            margin: 0px !important;
        """)
        #make title_bar_layout height 30
        self.title_bar.setFixedHeight(30)
        title_bar_layout.addWidget(self.close_button)

        # Status label
        self.status_label = QtWidgets.QLabel(' Ready')
        self.status_label.setStyleSheet("color: #4a90e2; font-weight: bold; text-align: left !important;")
        self.status_label.setAlignment(QtCore.Qt.AlignLeft)
        # Button Layout
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setAlignment(QtCore.Qt.AlignLeft)
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


        # Action sets dropdown
        self.action_set_combo_box = QtWidgets.QComboBox()
        self.action_set_combo_box.setStyleSheet("""
            color: #fff;
        """)
        self.action_set_names = ["farm_rss","farm_food","farm_wood","farm_stone","farm_gold", "farm_barb", "lyceum", "lyceumMid", "train_troops"]
        self.action_set_combo_box.addItems(self.action_set_names)

        # Checkbutton for captcha
        self.check_captcha_checkbutton = QtWidgets.QCheckBox("captcha")
        self.check_captcha_checkbutton.setStyleSheet("""
            font-size: 11px;
            background-color: #3a3a3a; 
            color: #fff;             
            border: 2px solid #4a90e2;  
            border-radius: 8px;
            padding: 2px;
        """)
        self.check_captcha_checkbutton.setChecked(True)

        

        # Content Layout
        debug_layout = QtWidgets.QVBoxLayout()
        debug_layout.setContentsMargins(0, 0, 0, 0)

        # Background label
        self.current_state_label_BG = QtWidgets.QLabel() 
        self.current_state_label_BG.setFixedWidth(77)
        self.current_state_label_BG.setFixedHeight(80)
        self.current_state_label_BG.setStyleSheet("""
            text-align: center;
            font-size: 10px;
            border: 2px solid #4a90e2; 
            border-radius: 8px;
            padding: 0px;
            background-color: #3a3a3a;
        """)
        self.current_state_label_BG.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        debug_layout.addWidget(self.current_state_label_BG)
        debug_layout.setSpacing(0)
        # Text label
        self.current_state_label_title = QtWidgets.QLabel('Debug')
        self.current_state_label_title.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.current_state_label_title.setStyleSheet("""
            text-align: center;
            font-size: 12px;
            font-weight: bold;
            border: 2px solid #4a90e2; 
            border-radius: 6px;
            margin: 0px !important;                                         
            padding: 0px !important;
            background-color: transparent;
        """)
        self.current_state_label = QtWidgets.QLabel()
        self.current_state_label.setFixedWidth(77)
        self.current_state_label.setFixedHeight(70)
        self.current_state_label.setStyleSheet("""
            text-align: center;
            font-size: 10px;
            border: 0px solid #4a90e2; 
            margin: 0px !important;
            padding: 0px !important;
            border-radius: 2px;
            background-color: transparent;
        """)
        self.current_state_label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.current_state_label.setContentsMargins(0, 0, 0, 0)
        

        # Create a layout for the text label and add it to the background label
        text_layout = QtWidgets.QVBoxLayout(self.current_state_label_BG)
        text_layout.setSpacing(2)

        text_layout.addWidget(self.current_state_label_title)
        text_layout.addWidget(self.current_state_label)
        text_layout.setContentsMargins(0, 0, 0, 0) # Adjust margins as needed

        content_layout = QtWidgets.QVBoxLayout()
        content_layout.setSpacing(2)
        content_layout.setContentsMargins(0, 0, 0, 0)
        #content_layout.addWidget(self.status_label)
        button_layout.setSpacing(2)
        content_layout.addLayout(button_layout)
        content_layout.addWidget(self.action_set_combo_box)
        content_layout.addWidget(self.check_captcha_checkbutton)
        content_layout.addLayout(debug_layout) # Add it to the layout

        # Main Layout
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(3, 0, 0, 0)
        layout.setSpacing(5)
        #layout.addWidget(self.title_bar)
        layout.addLayout(content_layout)

        # Set main layout
        self.setLayout(layout)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle('OSROKBOT')

        self.play_button.show()
        self.stop_button.hide()
        self.pause_button.hide()
        #self.setFixedSize(100, 150)
        #fix horizontal size
        self.setFixedWidth(80)

        #transparent backgourd
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        

        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowOpacity(0.75)
        self.show()
        WindowHandler().activate_window("OSROKBOT")
        GLOBAL_VARS.UI = self

    def currentState(self, state_text):
        self.current_state_label.setText(state_text)
        self.current_state_label.adjustSize() # Optional, to adjust the size of the label to fit the new text



    def update_position(self):
        target_windows = gw.getWindowsWithTitle(self.target_title)
        active_window = gw.getActiveWindow()

        if target_windows and (target_windows[0].title == self.target_title or target_windows[0].title == "OSROKBOT"):
            target_window = target_windows[0]
            self.move(target_window.left + 5, target_window.top + int(target_window.height / 1.85))
            if active_window and (active_window.title == self.target_title or active_window.title == "OSROKBOT" or active_window.title == "python3"):
                self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
            else:
                self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
            if not self.isVisible():
                self.show()



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
        self.status_label.setStyleSheet("color: #4a90e2; font-weight: bold; text-align: left;")
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