from tkinter import *
from functools import partial
import re


class Converter:
    def __init__(self, parent):
        # Formatting Variables
        background_color = "light blue"

        # Initialise list to hold calculation history
        self.all_calc_list = []

        # Converter Frame
        self.converter_frame = Frame(bg=background_color, pady=10)  # No width/height = auto-resize to fit content
        self.converter_frame.grid()

        # Temperature Converter Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter", font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10, justify="center")
        self.temp_converter_label.grid(row=0)

        # User instructions (row 1)
        self.instructions_label = Label(self.converter_frame,
                                        text="Type a temperature in the box below.\nThen press \"To "
                                             "Celsius\" or\n\"To Fahrenheit\" to convert it.",
                                        font=("Arial", "12", "italic"),
                                        wrap=350,
                                        bg=background_color,
                                        padx=10, pady=10, justify="center")
        self.instructions_label.grid(row=1)

        # Temperature entry box (row 2)
        self.temp_entry = Entry(self.converter_frame, width=20,
                                font=("Arial", "14", "bold"), justify="center")
        self.temp_entry.grid(row=2)

        # Conversion buttons frame (row 3)
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=15)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Celsius", font=("Arial", "10", "bold"),
                                  bg="lightsalmon1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        # This label only exists to add space between the buttons
        self.button_spacer = Label(self.conversion_buttons_frame,
                                   text="  ", fg=background_color, bg=background_color,
                                   padx=1, pady=15)
        self.button_spacer.grid(row=0, column=1)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font=("Arial", "10", "bold"),
                                  bg="mediumorchid1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=2)

        # Answer label (row 4)
        self.answer_label = Label(self.converter_frame,
                                  text="", font=("Arial", "16", "bold"),
                                  fg="black", bg=background_color, padx=10, pady=10)
        self.answer_label.grid(row=4)

        # History + Help button frame (row 5)
        self.history_help_frame = Frame(self.converter_frame)
        self.history_help_frame.grid(row=5, pady=15)

        self.history_button = Button(self.history_help_frame,
                                     text="Calculation History", font=("Arial", "10", "bold"),
                                     bg="goldenrod1", padx=10, pady=10,
                                     command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=0, column=0)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)

        # Another button spacer label
        self.button_spacer = Label(self.history_help_frame,
                                   text="  ", fg=background_color, bg=background_color,
                                   padx=1, pady=15)
        self.button_spacer.grid(row=0, column=1)

        self.help_button = Button(self.history_help_frame,
                                  text="Help", font=("Arial", "10", "bold"),
                                  bg="goldenrod3", padx=10, pady=10, command=self.help)
        self.help_button.grid(row=0, column=2)

    def temp_convert(self, low):
        error = "#ffafaf"  # Pale pink for errors

        # Get user input from Entry field
        to_convert = self.temp_entry.get()
        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Check and convert to F
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9 / 5) + 32

                # Round temperature
                fahrenheit = self.round_num(fahrenheit)
                to_convert = self.round_num(to_convert)

                # Generate answer
                answer = f"{to_convert} C is {fahrenheit} F"

            # Check and convert to C
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5 / 9

                # Round temperature
                celsius = self.round_num(celsius)
                to_convert = self.round_num(to_convert)

                # Generate answer
                answer = f"{to_convert} F is {celsius} C"

            else:
                # Input is invalid (too cold)
                answer = "Too Cold!"
                has_errors = "yes"

            # Display new temperature
            if has_errors == "no":
                self.answer_label.configure(text=answer, fg="blue")
                self.temp_entry.configure(bg="white")

            else:
                self.answer_label.configure(text=answer, fg="red")
                self.temp_entry.configure(bg=error)

            # Add Answer to history list
            if has_errors != "yes":
                self.all_calc_list.append(answer)
                self.history_button.config(state=NORMAL)

            # Add temperature to calculation history
        except ValueError:
            self.answer_label.configure(text="Please enter a number!", fg="red")
            self.temp_entry.configure(bg=error)

    def round_num(self, num):
        if num % 1 == 0:
            rounded = int(num)
        else:
            rounded = round(num, 1)

        return rounded

    def history(self, calc_history):
        History(self, calc_history)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="To use the converter, type the temperature that you would like to convert, "
                                          "then press the button you would like the convert the temperature to.\n\n"
                                          "For example, to convert 1F to C, you would type 1 into the grey box,"
                                          " then press the \"To Celsius\" button.", font="Arial 10 bold")


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
                                     font=("Arial", "20", "bold"))
        self.history_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent calculations. Use the export button to create a text "
                                       "file of all your calculations for this session.",
                                  wrap=250,
                                  bg=background, width=40,
                                  font="arial 10 bold", fg="maroon")
        self.history_text.grid(row=1)

        # History output goes here (row 2)
        # Generate string from list of calculations
        history_string = ""

        if len(calc_history) > 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history) - item - 1] + "\n"

                self.history_text.config(text="Here is your 7 most recent calculations. Use the export button to "
                                              "create a text file of all your calculations for this session.")

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) - calc_history.index(item) - 1] + "\n"

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
                                    font=("Arial", "12", "bold"),
                                    command=lambda: self.export(calc_history))
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
                                    font=("Arial", "20", "bold"))
        self.export_heading.grid(row=0)

        # export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="Here are your most recent calculations. Use the export button to create a text "
                                      "file of all your calculations for this session.",
                                 wrap=300, justify=LEFT,
                                 bg=background, width=40,
                                 font="arial 10 bold", fg="maroon")
        self.export_text.grid(row=1)

        # Warning label (row 2)
        self.export_text = Label(self.export_frame,
                                 text="If the filename you enter below already exists, its contents will be replaced "
                                      "with your calculation history", wrap=275, bg="#ffcccb", fg="black",
                                 justify=CENTER, font="Arial 9 bold")
        self.export_text.grid(row=2)

        # Filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3)

        # Error message labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background, font="Arial 14 bold")
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
            self.save_error_label.config(text=f"Invalid filename - {problem}")

        else:
            filename = filename + ".txt"
            self.save_error_label.config(text=f"Saved your history as {filename}")

            # Create new file to store data
            f = open(filename, "w+")

            # Add data to file
            for item in calc_history:
                f.write(item + "\n")

    def close_export(self, partner):
        # Re-enable export button
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


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
                                  text="Dismiss", width=10, font="Arial 10 bold",
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
