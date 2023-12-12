import tkinter as tk
from tkinter import messagebox

class AdventureGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Adventure Game")
        self.master.geometry("400x300")

        self.story_text = tk.Label(master, text="Welcome to the Adventure Game!", wraplength=300, justify=tk.LEFT)
        self.story_text.pack(pady=20)

        self.choice_buttons = []
        self.create_choice_buttons(["Start"])

    def create_choice_buttons(self, choices):
        for button in self.choice_buttons:
            button.destroy()

        for choice in choices:
            button = tk.Button(self.master, text=choice, command=lambda c=choice: self.make_choice(c))
            button.pack(pady=5)
            self.choice_buttons.append(button)

    def make_choice(self, choice):
        if choice == "Start":
            self.story_text.config(text="You find yourself in a dark forest. What do you want to do?")
            self.create_choice_buttons(["Explore", "Stay put"])

        elif choice == "Explore":
            self.story_text.config(text="You come across a clearing with a mysterious object. What do you want to do?")
            self.create_choice_buttons(["Inspect the object", "Ignore and continue"])

        elif choice == "Stay put":
            self.story_text.config(text="You decide to stay put and rest. Suddenly, you hear a rustling sound.")
            self.create_choice_buttons(["Investigate", "Ignore"])

        elif choice == "Inspect the object":
            self.story_text.config(text="The object is a magical portal. Do you want to enter it?")
            self.create_choice_buttons(["Enter", "Back away"])

        elif choice == "Ignore and continue":
            self.story_text.config(text="You decide to ignore the object and continue exploring.")
            self.create_choice_buttons(["Continue", "Head back"])

        elif choice == "Investigate":
            self.story_text.config(text="You investigate the source of the sound and find a friendly creature.")
            self.create_choice_buttons(["Befriend", "Ignore"])

        elif choice == "Ignore":
            self.story_text.config(text="You choose to ignore the sound and focus on your surroundings.")
            self.create_choice_buttons(["Continue", "Rest"])

        elif choice == "Enter":
            messagebox.showinfo("Congratulations!", "You have successfully completed the adventure!")

        elif choice == "Back away":
            self.story_text.config(text="You decide not to enter the portal and continue exploring.")
            self.create_choice_buttons(["Continue", "Head back"])

        elif choice == "Continue":
            self.story_text.config(text="You press on, eager to see what else the forest holds.")
            self.create_choice_buttons(["Continue", "Rest"])

        elif choice == "Head back":
            self.story_text.config(text="You decide to head back. The forest path looks different now.")
            self.create_choice_buttons(["Explore", "Rest"])

        elif choice == "Befriend":
            self.story_text.config(text="You befriend the creature, and it becomes your loyal companion.")
            self.create_choice_buttons(["Continue with your companion", "Continue alone"])

        elif choice == "Rest":
            self.story_text.config(text="You take a rest and regain your energy.")
            self.create_choice_buttons(["Continue", "Explore"])

        elif choice == "Continue with your companion":
            messagebox.showinfo("Congratulations!", "You and your companion have successfully completed the adventure!")

        elif choice == "Continue alone":
            messagebox.showinfo("Congratulations!", "You have successfully completed the adventure!")

if __name__ == "__main__":
    root = tk.Tk()
    game = AdventureGame(root)
    root.mainloop()



