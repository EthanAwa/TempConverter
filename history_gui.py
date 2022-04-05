from tkinter import *
from functools import partial
import random


class Converter:
    def __init__(self, parent):
        # Formatting Variables
        background_color = "light blue"

        # In actual program this is blank and filled from user input
        self.all_calc_list = ['1 F is -17.2 C', '2 F is -16.7 C', '3 F is -16.1 C',
                              '4 F is -15.6 C', '5 F is -15 C']
    # '6 F is -14.4 C','7 F is -13.9 C', '8 F is -13.3 C', '9 F is -12.8 C'

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

        self.history_button = Button(self.converter_frame,
                                     text="History",
                                     font=("Arial", "14"),
                                     padx=10, pady=10,
                                     command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

    def history(self, calc_history):
        History(self, calc_history)


class History:
    def __init__(self, partner, calc_history):
        # Formatting Variables
        background = "#a9ef99"  # Pale Green

        # Disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (eg: history window)
        self.history_box = Toplevel()

        # If user closes via cross button, close history and re-enable history button
        self.history_box.protocol("WM_DELETE_WINDOW", partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background,
                                   pady=10)  # No width/height = auto-resize to fit content
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.history_heading = Label(self.history_frame,
                                     text="Calculation History",
                                     bg=background,
                                     font=("Arial", "10", "bold"))
        self.history_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent calculations. Use the export button to create a text "
                                       "file of all your calculations for this session.",
                                  wrap=250,
                                  bg=background, width=40,
                                  font="arial 10 italic", fg="maroon")
        self.history_text.grid(row=1)

        # History output goes here (row 2)

        # Generate string from list of calculations
        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history) - item - 1]+"\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) - calc_history.index(item) - 1]+"\n"

                self.history_text.config(text="Here is your calculation history. Use the export button to create a text"
                                              "file of all your calculations for this session.")

        # Label to display calculation history
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background, font="Arial 14", justify=LEFT)
        self.calc_label.grid(row=2)

        # Export / Dismiss Buttons Frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=9)

        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font=("Arial", "12", "bold"))
        self.export_button.grid(row=0, column=0)

        # This label only exists to add space between the buttons
        self.button_spacer = Label(self.export_dismiss_frame,
                                   text="  ", fg=background, bg=background,
                                   padx=1, pady=10)
        self.button_spacer.grid(row=0, column=1)

        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold", command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=2)

    def close_history(self, partner):
        # Re-enable history button
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    window = Converter(root)
    root.mainloop()
