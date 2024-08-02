from machine import I2C, Pin
from DIYables_LCD_I2C import DIYables_LCD_I2C
import utime

# The I2C address of your LCD (Update if different)
I2C_ADDR = 0x27  # Use the address found using the I2C scanner

# Define the number of rows and columns on your LCD
LCD_ROWS = 2
LCD_COLS = 16

# Initialize I2C
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

# Initialize LCD
lcd = DIYables_LCD_I2C(i2c, I2C_ADDR, LCD_ROWS, LCD_COLS)

# Setup function
lcd.backlight_on()
lcd.clear()

# Main loop function
while True:
    lcd.clear()
    lcd.set_cursor(3, 0) # Move the cursor to column 3, row 0 (first row)
    lcd.print("DIYables")
    lcd.set_cursor(0, 1) # Move the cursor to column 0, row 1 (second row)
    lcd.print("www.diyables.io")
    utime.sleep(2)
    
    lcd.clear()
    lcd.set_cursor(0, 0) # Move to the beginning of the first row
    lcd.print("Int: ")
    lcd.print(str(1234))  # Print integer
    lcd.set_cursor(0, 1)  # Move to the beginning of the second row
    lcd.print("Float: ")
    lcd.print(str(56.78))  # Print float
    utime.sleep(2)

