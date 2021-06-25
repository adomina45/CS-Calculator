#CS_Calculator.py

import PySimpleGUI as sg
import math

sg.theme("Python")
layout = [[sg.Text("How can I help you?")],
 [sg.Text("What number system are you using? (If nothing is input then we will default to decimal)")],
 [sg.Button("Binary"), sg.Button("Decimal"), sg.Button("Hexadecimal"), sg.Button("Octal")],
 [sg.Text("What's the number?")],
 [sg.InputText(key='textbox')],
 [sg.Text("What are we doing to the number?")],
 [sg.Button("Binary Logarithm"), sg.Button("Convert to Binary"), sg.Button("Convert to Decimal")],
 [sg.Button("Convert to Hexadecimal"), sg.Button("Convert to Octal")],
 [sg.Output(size=(50,1), key='-OUTPUT-')],
 [sg.Button("Quit")]]

# Create the window
window = sg.Window("Computer Science Calculator", layout, margins=(100, 50))

continue_calculating = True
num_system = "decimal" #if not specificed will default to decimal
while continue_calculating:
    event, values = window.read()
    input = values['textbox'] #grab input from textbox
    if event == sg.WIN_CLOSED or event == "Quit":
        continue_calculating = False
    elif event == "Binary":
        num_system = "binary"
    elif event == "Hexadecimal":
        num_system = "hexadecimal"
    elif event == "Octal":
        num_system = "octal"
    elif event == "Decimal":
        num_system = "decimal"
    elif event == "Binary Logarithm":
        if num_system == "decimal":
            try:
                f = float(input)
                final = math.log(f,2)
                print(final)
            except:
                print("The data you have input is not a real number")
                
    elif event == "Convert to Binary":
        if num_system == "decimal":
            try:
                num = int(input)
                b = bin(num)
                print(b)
            except:
                print("The data you have input is not an integer")
    elif event == "Convert to Decimal":
        if num_system == "decimal":
            print("You already have decimal selected. You need to change to another number system in order to convert to decimal.")
    elif event == "Convert to Hexadecimal":
        if num_system == "decimal":
            try:
                num = int(input)
                h = hex(num)
                print(h)
            except:
                print("The data you have input is not an integer")
    elif event == "Convert to Octal":
        if num_system == "decimal":
            try:
                num = int(input)
                o = oct(num)
                print(o)
            except:
                print("The data you have input is not an integer")
    print("The current number system is " + num_system)