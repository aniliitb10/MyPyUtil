import ctypes
from datetime import datetime
from time import sleep

half_an_hour = 30*60
logFileName = "ReminderLogFile.txt"


def display_po_up(text, title="Alert"):
    with open(logFileName, 'a') as logFileHandlerInAppendMode:
        logFileHandlerInAppendMode.write("Last alert time: " + datetime.now().time().isoformat() + "\n")
    ctypes.windll.user32.MessageBoxW(0, text, title, 0x00001000)


with open(logFileName, 'w') as logFileHandlerInWriteMode:
    logFileHandlerInWriteMode.write("Started the script at: " + datetime.now().time().isoformat() + "\n")

while datetime.now().time().hour < 21:
    sleep(half_an_hour)
    display_po_up("take a sip of water")
