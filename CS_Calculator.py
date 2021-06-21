#CS_Calculator.py

import PySimpleGUI as sg
import math

sg.theme("Python")
layout = [[sg.Text("How can I help you?")], 
 [sg.Output(size=(50,1), key='-OUTPUT-')], 
 [sg.Text("What number system are you using? (If nothing is input then we will default to decimal)")],
 [sg.Button("Binary"), sg.Button("Decimal"), sg.Button("Hexadecimal"), sg.Button("Octal")],
 [sg.Text("What's the number?")],
 [sg.Button("0"), sg.Button("1"), sg.Button("2"), sg.Button("3")],
 [sg.Button("4"), sg.Button("5"), sg.Button("6"), sg.Button("7")],
 [sg.Button("8"), sg.Button("9"), sg.Button("A"), sg.Button("B")],
 [sg.Button("C"), sg.Button("D"), sg.Button("E"), sg.Button("F")],
 [sg.Text("What are we doing to the number?")],
 [sg.Button("Binary Log"), sg.Button("Convert to Binary"), sg.Button("Convert to Decimal")], 
 [sg.Button("Convert to Hexadecimal"), sg.Button("Convert to Octal"), sg.Button("Quit")]]

# Create the window
window = sg.Window("Calcator", layout, margins=(100, 50))

while True:
    event = window.read()
    num_system = decimal #if not specificed will default to decimal
    number = ""
    if event == sg.WIN_CLOSED or event == "Quit":
        break
    else:
        noop