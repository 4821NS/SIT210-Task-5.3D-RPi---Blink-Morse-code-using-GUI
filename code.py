import RPi.GPIO as GPIO
import tkinter as tk
from tkinter import ttk
import time

# Define Morse code representations for characters
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'  # Space
}

# GPIO setup
LED_PIN = 10  # Replace with your GPIO pin number
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

# Function for blinking the LED in Morse code
def blink_morse_code(name):
    for char in name.upper():
        if char in morse_code_dict:
            morse_code = morse_code_dict[char]
            for symbol in morse_code:
                if symbol == '.':
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    time.sleep(0.2)  # Duration for a dot
                    GPIO.output(LED_PIN, GPIO.LOW)
                    time.sleep(0.2)  # Gap between dots and dashes
                elif symbol == '-':
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    time.sleep(0.6)  # Duration for a dash
                    GPIO.output(LED_PIN, GPIO.LOW)
                    time.sleep(0.2)  # Gap between dots and dashes
            time.sleep(0.4)  # Gap between characters
        else:
            # Handle spaces and unknown characters
            time.sleep(0.8)  # Gap between words

# GUI setup
root = tk.Tk()
root.title("LED Morse Code Blinker")

# Function to handle button click
def start_blinking():
    name = entry.get()
    blink_morse_code(name)

# Create a styled frame for the GUI with a colorful background
frame = ttk.Frame(root, padding=(20, 20), style="My.TFrame")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Create and style a label with a colorful font
label = ttk.Label(frame, text="Enter a Name: ", font=("Courier", 20), foreground="purple")
label.grid(column=0, row=0, columnspan=2, pady=(0, 40))

# Create and style an entry widget with a colorful background
entry = ttk.Entry(frame, width=20, font=("Courier", 20), background="lightblue")
entry.grid(column=0, row=1, columnspan=2, pady=(0, 40))

# Create and style a button with a colorful background
button = ttk.Button(frame, text="Start Blinking", command=start_blinking, style="TButton")
button.grid(column=0, row=2, columnspan=2, pady=(0, 40))

# Style configurations for the button and frame
style = ttk.Style()
style.configure("TButton", background="blue", foreground="white", font=("Times New Roman", 20))
style.configure("My.TFrame", background="#F0F0F0")  # Light gray background

root.mainloop()

# Clean up GPIO resources
GPIO.cleanup()
write a script explaning this code