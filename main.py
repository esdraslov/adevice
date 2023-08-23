import PySimpleGUI as sg
import themes
import os

menu = [
    ["power", [
        "restart",
        "flash",
        "bootloader"
    ]],
    ["debug", [
        "logcat"
    ]],
    ["packages", [
        "install package"
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

    if event == "restart":
        os.system(".\\bin\\adb.exe reboot")
    if event == "recovery" or event == "flash":
        os.system(".\\bin\\adb.exe reboot recovery")
    if event == "root device":
        os.system(".\\bin\\adb.exe root")
    if event == "unroot device":
        os.system(".\\bin\\adb.exe unroot")
    if event == "bootloader":
        os.system(".\\bin\\adb.exe reboot bootloader")
    if event == "install package":
        pack = sg.popup_get_file("please, select your apk file", file_types = (('android package', '*.apk *.apk')))
        os.system(f".\\bin\\adb.exe install {pack}")

window.close()