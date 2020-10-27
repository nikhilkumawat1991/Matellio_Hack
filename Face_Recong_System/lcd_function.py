import pandas as pd
import time
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
lcd_columns = 16
lcd_rows = 2
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)
lcd.clear()
#lcd.backlight = True
def welcome():
    lcd.color=[100,100,100]
    time.sleep(.5)
    lcd.cursor_position(4,0)
    lcd.message="Welcome!!\n To Matellio"
    time.sleep(1)
    lcd.display=False
    time.sleep(1)
    lcd.clear()
    time.sleep(.2)
    lcd.display=True
    lcd.color = [0,100,100]
    time.sleep(1)
    #lcd.cursor_position(0,1)
    time.sleep(1)
    #lcd.blink = True
    lcd.text_direction=lcd.LEFT_TO_RIGHT
    msg="Please\nEnter Employee ID "
    lcd.message=msg
    for i in range(len(msg)+3):
        time.sleep(.3)
        lcd.move_left()
    time.sleep(.1)
    #lcd.blink = False
    lcd.clear()
    time.sleep(.2)
def inputMsg():
    lcd.color = [0,100,100]
    time.sleep(1)
    #lcd.cursor_position(0,1)
    time.sleep(1)
    #lcd.blink = True
    lcd.text_direction=lcd.LEFT_TO_RIGHT
    msg="Please\nEnter Employee ID "
    lcd.message=msg
    for i in range(len(msg)+4):
        time.sleep(.5)
        lcd.move_left()
    time.sleep(.1)
    #lcd.blink = False
    lcd.clear()
    time.sleep(.5)
def msg_door_open():
    lcd.color=[0,100,0]
    time.sleep(1)
    lcd.cursor_position(4,0)
    lcd.text_direction=lcd.LEFT_TO_RIGHT
    lcd.message="Thanks!!\n Have a nice Day"
    time.sleep(5)
    lcd.clear()
def authentication_failed():
    lcd.color=[100,0,0]
    time.sleep(1)
    lcd.cursor_position(4,0)
    lcd.text_direction=lcd.LEFT_TO_RIGHT
    lcd.message="Sorry!!\nNot Vaild ID"
    time.sleep(5)
    lcd.clear()
def msg_wait():
    lcd.color=[0,100,0]
    time.sleep(1)
    lcd.cursor_position(4,0)
    lcd.text_direction=lcd.LEFT_TO_RIGHT
    lcd.message="Please!!\nWait.."
    time.sleep(5)
    lcd.clear()
def key_input(input_key):
    lcd.color=[0,100,0]
    time.sleep(1)
    lcd.cursor_position(4,0)
    lcd.text_direction=lcd.LEFT_TO_RIGHT
    lcd.message=input_key
    time.sleep(5)
    lcd.clear()
def idFormat():
    lcd.color=[100,0,0]
    time.sleep(1)
    lcd.cursor_position(0,1)
    lcd.text_direction=lcd.LEFT_TO_RIGHT
    lcd.message="WrongIdFormat!!"
    time.sleep(5)
    lcd.clear()
    
#while True:
    #inputMsg()
    #msg_door_open()
    #authentication_failed()
    
    
#inputMsg()
#idFormat()

    

