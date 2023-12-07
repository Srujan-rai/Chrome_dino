import serial
import time
import pyautogui
time.sleep(10)

ser = serial.Serial('COM4', 9600)
while True:
    data = ser.readline().decode().strip()
    print(data)
    
    if data == "YES":
        print("Received YES")
        pyautogui.press('space')

    elif data == "NO":
        print("Received NO")

