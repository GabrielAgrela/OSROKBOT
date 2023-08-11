import tkinter as tk
from tkinter import ttk
from action_sets import ActionSets
from game_automator import GameAutomator

class UI:
    def __init__(self, window_title, delay=0):
        self.game_automator = GameAutomator(window_title, delay)
        self.root = tk.Tk()
        self.root.title('Game Automator Controller')

        # Define some custom fonts
        button_font = ("Verdana", 10)
        label_font = ("Verdana", 12, "bold")

        # Custom style for the buttons
        style = ttk.Style()
        style.configure("TButton", font=button_font)
        style.configure("TLabel", font=label_font)
        
        # Buttons with custom fonts
        self.start_button = ttk.Button(self.root, text='Start', command=self.start_automation)
        self.start_button.pack(pady=5)
        self.stop_button = ttk.Button(self.root, text='Stop', command=self.stop_automation)
        self.stop_button.pack(pady=5)
        self.pause_button = ttk.Button(self.root, text='Toggle Pause', command=self.toggle_pause)
        self.pause_button.pack(pady=5)

        # Action sets listbox
        self.action_set_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, font=button_font)
        self.action_set_listbox.pack(pady=5)
        self.action_sets = ActionSets(game_automator=self.game_automator)
        self.action_set_names = ["farm_rss", "farm_barb","lyceum","lyceumMid"] # Add the names of the action sets here
        for action_set_name in self.action_set_names:
            self.action_set_listbox.insert(tk.END, action_set_name)

        # Checkbutton for captcha
        self.check_captcha_var = tk.IntVar(value=1)
        self.check_captcha_checkbutton = ttk.Checkbutton(self.root, text="Check for Captcha", variable=self.check_captcha_var)
        self.check_captcha_checkbutton.pack(pady=5)

        # Status label with custom font
        self.status_label = ttk.Label(self.root, text='Status: Stopped', style="TLabel")
        self.status_label.pack(pady=5)

        # Handle closing event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def start_automation(self):
        selected_index = self.action_set_listbox.curselection()
        if selected_index:
            action_group = getattr(self.action_sets, self.action_set_names[selected_index[0]])()
            actions_groups = [action_group]
            if self.check_captcha_var.get():
                actions_groups.append(self.action_sets.emailtest())
            self.game_automator.start(actions_groups)
            self.status_label.config(text='Status: Running')

    def stop_automation(self):
        self.game_automator.stop()
        self.status_label.config(text='Status: Stopped')

    def toggle_pause(self):
        self.game_automator.toggle_pause()
        if self.game_automator.is_paused():
            self.status_label.config(text='Status: Paused')
        else:
            self.status_label.config(text='Status: Running')

    def on_closing(self):
        self.game_automator.stop()
        self.stop_automation()
        self.root.quit()
        self.root.destroy()
        exit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = UI('Rise of Kingdoms')
    gui.run()
