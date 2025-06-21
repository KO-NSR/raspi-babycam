# # ./LCD1602I2C/LCD.pyのインポート
# import sys
# sys.path.append('/home/nsrns50f/projects')
# from LCD1602I2C.LCD import LCD
# import time
 
# lcd = LCD(2,0x27,True)
 
# lcd.message("Hello World!", 1)
# lcd.message("test2", 2)
 
# time.sleep(5)
# lcd.clear()


# from LCD1602I2Cmod.LCD import LCD
import sys
sys.path.append('/home/nsrns50f/projects')
from LCD1602I2C.JLCD import JLCD as LCD
import time

lcd = LCD(2,0x27,True)
lcd.message("temp:",1)
lcd.message("23:00$$%",2)

time.sleep(5)
lcd.clear()