#CS_Calculator.py

import PySimpleGUI as sg
import math

sg.theme("Python")
layout = [[sg.Text("How can I help you?")],
 [sg.Text("What number system are you using? (If nothing is input then we will default to decimal)")],
 [sg.Button("Binary"), sg.Button("Decimal"), sg.Button("Hexadecimal"), sg.Button("Octal")],
 [sg.Text("What's the number?")],
 [sg.InputText(key='textbox')],
 #[sg.Button("0"), sg.Button("1"), sg.Button("2"), sg.Button("3")],
 #[sg.Button("4"), sg.Button("5"), sg.Button("6"), sg.Button("7")],
 #[sg.Button("8"), sg.Button("9"), sg.Button("A"), sg.Button("B")],
 #[sg.Button("C"), sg.Button("D"), sg.Button("E"), sg.Button("F")],
 #[sg.Button(".")],
 [sg.Text("What are we doing to the number?")],
 [sg.Button("Binary Logarithm"), sg.Button("Convert to Binary"), sg.Button("Convert to Decimal")],
 [sg.Button("Convert to Hexadecimal"), sg.Button("Convert to Octal")],
 [sg.Output(size=(50,1), key='-OUTPUT-')],
 [sg.Button("Quit")]]

# Create the window
window = sg.Window("Calcator", layout, margins=(100, 50))

continue_calculating = True
while continue_calculating:
    event, values = window.read()
    input = values['textbox'] #grab input from textbox
    num_system = "decimal" #if not specificed will default to decimal
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
        try:
            f = float(input)
            final = math.log(f,2)
            print(final)
        except:
            print("The data you have input is of an invalid type")








    #elif event == "Convert to Binary":
    #elif event == "Convert to Decimal":
    #elif event == "Convert to Hexadecimal":
    #elif event == "Convert to Octal":
