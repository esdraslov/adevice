import PySimpleGUI as sg
import themes
import os

menu = [
    ["power", [
        "restart",
        "recovery",
        "bootloader"
    ]],
    ["debug", [
        "logcat"
    ]]
]

sg.theme(themes.themes["DG1"])
layout = [
    [sg.Menu(menu)],
    [sg.Text("adevice"), sg.Text("verify if client or your phone is connected for use (this is undetectable)")],
    [sg.Button("restart"), sg.Button("root device"), sg.Button("unroot device"), sg.Button("recovery")]
]

window = sg.Window("adevice", layout)
run = True
while run:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        run = False

window.close()