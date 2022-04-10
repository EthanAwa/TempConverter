from tkinter import *
from functools import partial
import re
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

        self.export_button = Button(self.converter_frame,
                                    text="Export",
                                    font=("Arial", "14"),
                                    padx=10, pady=10,
                                    command=lambda: self.export(self.all_calc_list))
        self.export_button.grid(row=1)

    def export(self, calc_export):
        Export(self, calc_export)


class Export:
    def __init__(self, partner, calc_history):
        # Formatting Variables
        background = "#a9ef99"  # Pale Green

        # Disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (eg: export window)
        self.export_box = Toplevel()

        # If user closes via cross button, close export and re-enable export button
        self.export_box.protocol("WM_DELETE_WINDOW", partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, bg=background,
                                  pady=10)  # No width/height = auto-resize to fit content
        self.export_frame.grid()

        # Set up export heading (row 0)
        self.export_heading = Label(self.export_frame,
                                    text="Calculation Export",
                                    bg=background,
                                    font=("Arial", "10", "bold"))
        self.export_heading.grid(row=0)

        # export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="Here are your most recent calculations. Use the export button to create a text "
                                      "file of all your calculations for this session.",
                                 wrap=250, justify=LEFT,
                                 bg=background, width=40,
                                 font="arial 10 italic", fg="maroon", )
        self.export_text.grid(row=1)

        # Warning label (row 2)
        self.export_text = Label(self.export_frame,
                                 text="If the filename you enter below already exists, its contents will be replaced "
                                      "with your calculation history", wrap=225, bg=background, fg="maroon",
                                 justify=LEFT, font="Arial 10 italic")
        self.export_text.grid(row=2)

        # Filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3)

        # Error message labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel Buttons Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=9)

        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font=("Arial", "12", "bold"),
                                  command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        # This label only exists to add space between the buttons
        self.button_spacer = Label(self.save_cancel_frame,
                                   text="  ", fg=background, bg=background,
                                   padx=1, pady=10)
        self.button_spacer.grid(row=0, column=1)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="Arial 12 bold", command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=2)

    def save_history(self, partner, calc_history):
        valid_chars = "[A-Za-z0-9_]"
        has_errors = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_chars, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = f"(no {letter}'s allowed)"
            has_errors = "yes"
            break

        if filename == "":
            problem = "(can't be blank)"
            has_errors = "yes"

        if has_errors == "yes":
            print(f"Invalid filename - {problem}")
            print()

        else:
            filename = filename + ".txt"
            print(filename)

            # Create new file to store data
            f = open(filename, "w+")

            # Add data to file
            for item in calc_history:
                f.write(item + "\n")

    def close_export(self, partner):
        # Re-enable export button
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    window = Converter(root)
    root.mainloop()
