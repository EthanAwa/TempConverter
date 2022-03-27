from tkinter import *
from functools import partial
import random
import math


class Converter:
    def __init__(self, parent):
        # Formatting Variables
        background_color = "light blue"

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
                                  text="Placeholder text (conversion)", font=("Arial", "16", "bold"),
                                  fg="black", bg=background_color, padx=10, pady=10)
        self.answer_label.grid(row=4)

        # History + Help button frame (row 5)
        self.history_help_frame = Frame(self.converter_frame)
        self.history_help_frame.grid(row=5, pady=15)

        self.history_button = Button(self.history_help_frame,
                                     text="Calculation History", font=("Arial", "10", "bold"),
                                     bg="goldenrod1", padx=10, pady=10)
        self.history_button.grid(row=0, column=0)

        # Another button spacer label
        self.button_spacer = Label(self.history_help_frame,
                                   text="  ", fg=background_color, bg=background_color,
                                   padx=1, pady=15)
        self.button_spacer.grid(row=0, column=1)

        self.help_button = Button(self.history_help_frame,
                                  text="Help", font=("Arial", "10", "bold"),
                                  bg="goldenrod3", padx=10, pady=10)
        self.help_button.grid(row=0, column=2)

    def temp_convert(self, low):
        print(low)
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
                print(answer)

            # Check and convert to C
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5 / 9

                # Round temperature
                celsius = self.round_num(celsius)
                to_convert= self.round_num(to_convert)

                # Generate answer
                answer = f"{to_convert} F is {celsius} C"
                print(answer)

            else:
                # Input is invalid (too cold)
                answer = "Too Cold!"
                has_errors = "yes"
                print(answer)

            # Display new temperature
            if has_errors == "no":
                self.answer_label.configure(text=answer, fg="blue")
                self.temp_entry.configure(bg="white")

            else:
                self.answer_label.configure(text=answer, fg="red")
                self.temp_entry.configure(bg=error)

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


if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    window = Converter(root)
    root.mainloop()
