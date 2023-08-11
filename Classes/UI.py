import tkinter as tk
from action_sets import ActionSets
from game_automator import GameAutomator

class UI:
    def __init__(self, window_title, delay=0):
        self.game_automator = GameAutomator(window_title, delay)
        self.root = tk.Tk()
        self.root.title('Game Automator Controller')

        self.start_button = tk.Button(self.root, text='Start', command=self.start_automation)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text='Stop', command=self.stop_automation)
        self.stop_button.pack()

        self.pause_button = tk.Button(self.root, text='Toggle Pause', command=self.toggle_pause)
        self.pause_button.pack()

        self.status_label = tk.Label(self.root, text='Status: Stopped')
        self.status_label.pack()

        # Add a Listbox to let the user select an action set (only one at a time)
        self.action_set_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.action_set_listbox.pack()
        self.action_sets = ActionSets(game_automator=self.game_automator)

        # Assuming action sets are methods of ActionSets, and they can be listed here
        self.action_set_names = ["farm_rss", "farm_barb","lyceum","lyceumMid"] # Add the names of the action sets here
        for action_set_name in self.action_set_names:
            self.action_set_listbox.insert(tk.END, action_set_name)

        # Check button for captcha
        self.check_captcha_var = tk.IntVar(value=1)
        self.check_captcha_checkbutton = tk.Checkbutton(self.root, text="Check for Captcha", variable=self.check_captcha_var)
        self.check_captcha_checkbutton.pack()
        self.check_captcha_checkbutton.select()  # Check the checkbutton by default
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.stop_automation()
        self.root.quit()
        self.root.destroy()
        exit()


    def start_automation(self):
        selected_index = self.action_set_listbox.curselection()
        if selected_index:
            action_group = getattr(self.action_sets, self.action_set_names[selected_index[0]])()
            actions_groups = [action_group]

            # If captcha check is selected, add it to the action groups
            if self.check_captcha_var.get():
                actions_groups.append(self.action_sets.emailtest())

            self.game_automator.start(actions_groups)
        self.status_label.config(text='Status: Running')

    def stop_automation(self):
        self.game_automator.stop()
        self.status_label.config(text='Status: Stopped')

    def toggle_pause(self):
        self.game_automator.toggle_pause()
        if self.game_automator.is_paused(): # Assuming you have an is_paused() method in GameAutomator
            self.status_label.config(text='Status: Paused')
        else:
            self.status_label.config(text='Status: Running')


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = UI('Rise of Kingdoms')
    gui.run()
