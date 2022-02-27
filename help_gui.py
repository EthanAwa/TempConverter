from tkinter import *
from functools import partial
import random


class Converter:
    def __init__(self, parent):
        # Formatting Variables
        background_color = "light blue"

        # Create main screen GUI
        self.converter_frame = Frame(bg=background_color, pady=10)  # No width/height = auto-resize to fit content
        self.converter_frame.grid()

        # Temperature Converter Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        self.help_button = Button(self.converter_frame,
                                  text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("help console debug")
        get_help = Help(self)
        get_help.help_text.configure(text="Here is some help text. Blah blah blah")


class Help:
    def __init__(self, partner):

        # Formatting Variables
        background = "bisque"

        # Disable Help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (eg: help window)
        self.help_box = Toplevel()

        # If user closes via cross button, close help and re-enable help button
        self.help_box.protocol("WM_DELETE_WINDOW", partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background, pady=10)  # No width/height = auto-resize to fit content
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.help_heading = Label(self.help_frame,
                                  text="Help/Instructions",
                                  bg=background,
                                  font=("Arial", "10", "bold"))
        self.help_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame,
                               text="",
                               justify=LEFT, wrap=250,
                               bg=background, width=40)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame,
                                  text="Dismiss", width=10,
                                  bg="light salmon",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):

        # Re-enable help button
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    window = Converter(root)
    root.mainloop()
