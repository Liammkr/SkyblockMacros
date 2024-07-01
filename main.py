from colorama import Fore
from colorama import init
import os
from time import sleep
import random
import pyautogui
import threading
from datetime import datetime

init()

def log_money(amount):
    total_money = 0
    file_path = 'money_log.txt'

    # Read existing total from the file, if it exists
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()
            if first_line.startswith("Total Money: $"):
                total_money = int(first_line.split('$')[1].replace(',', ''))

    # Update the total money
    total_money += amount

    # Write the updated total back to the file
    with open(file_path, 'w') as file:
        file.write(f"Total Money: ${total_money:,}\n")
def output():
    while True:
        global money
        money += farmprofit
        clear_console()
        logo()
        print(Fore.CYAN + "Profit From Session: $" + f'{money:,}')
        sleep(0.1)

def log_key_press(key, duration):
    now = datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    with open('movements.txt', 'a') as file:
        file.write(f"[{date_time_str}] Key '{key}' was pressed for {duration:.2f} seconds\n")

def melon():
    times = 0
    pyautogui.mouseDown()
    while True:
        while times < 6:
            duration = random.uniform(72, 73)
            pyautogui.keyDown('a')
            sleep(duration)
            pyautogui.keyUp('a')
            log_key_press('a', duration)
            log_money(round(((farmprofit * 10) * duration)))
            
            duration = random.uniform(0.4, 0.75)
            pyautogui.keyDown('w')
            sleep(duration)
            pyautogui.keyUp('w')
            log_key_press('w', duration)
            log_money(round(((farmprofit * 10) * duration)))
            
            duration = random.uniform(72, 73)
            pyautogui.keyDown('d')
            sleep(duration)
            pyautogui.keyUp('d')
            log_key_press('d', duration)
            log_money(round(((farmprofit * 10) * duration)))
            
            duration = random.uniform(0.4, 0.75)
            pyautogui.keyDown('w')
            sleep(duration)
            pyautogui.keyUp('w')
            log_key_press('w', duration)
            log_money(round(((farmprofit * 10) * duration)))
            
            times += 1
        else:
            sleep_duration = random.uniform(5, 10)
            log_key_press('sleep', sleep_duration)
            sleep(sleep_duration)
            times = 0
def wcnp():
    pyautogui.mouseDown()
    pyautogui.keyDown('w')
    while True:
        duration = random.uniform(120, 123)
        pyautogui.keyDown('d')
        sleep(duration)
        pyautogui.keyUp('d')
        log_key_press('d', duration)
        log_money(round(((farmprofit * 10) * duration)))
        
        
        duration = random.uniform(120, 123)
        pyautogui.keyDown('a')
        sleep(duration)
        pyautogui.keyUp('a')
        log_key_press('a', duration)
        log_money(round(((farmprofit * 10) * duration)))
        
        duration = random.uniform(120, 123)
        pyautogui.keyDown('d')
        sleep(duration)
        pyautogui.keyUp('d')
        log_key_press('d', duration)
        log_money(round(((farmprofit * 10) * duration)))
        
        sleep_duration = random.uniform(5, 10)
        log_key_press('sleep', sleep_duration)
        sleep(sleep_duration)
def left():
    pyautogui.mouseDown()
    pyautogui.keyDown('w')
    while True:
        duration = random.uniform(120, 123)
        pyautogui.keyDown('a')
        sleep(duration)
        pyautogui.keyUp('a')
        log_key_press('a', duration)
        log_money(round(((farmprofit * 10) * duration)))
        
        
        duration = random.uniform(120, 123)
        pyautogui.keyDown('d')
        sleep(duration)
        pyautogui.keyUp('d')
        log_key_press('d', duration)
        log_money(round(((farmprofit * 10) * duration)))
        
        duration = random.uniform(120, 123)
        pyautogui.keyDown('a')
        sleep(duration)
        pyautogui.keyUp('a')
        log_key_press('a', duration)
        log_money(round(((farmprofit * 10) * duration)))
        
        sleep_duration = random.uniform(5, 10)
        log_key_press('sleep', sleep_duration)
        sleep(sleep_duration)
def cane():
    times = 0
    pyautogui.mouseDown()
    while True:
        while times < 3:
            duration = random.uniform(48, 50)
            pyautogui.keyDown('d')
            sleep(duration)
            pyautogui.keyUp('d')
            log_key_press('d', duration)
            log_money(round(((farmprofit * 10) * duration)))
            
            duration = random.uniform(48, 50)
            pyautogui.keyDown('s')
            sleep(duration)
            pyautogui.keyUp('s')
            log_key_press('s', duration)
            log_money(round(((farmprofit * 10) * duration)))
            times += 1
        else:
            duration = random.uniform(48, 50)
            pyautogui.keyDown('d')
            sleep(duration)
            pyautogui.keyUp('d')
            log_key_press('d', duration)
            log_money(round(((farmprofit * 10) * duration)))
            sleep_duration = random.uniform(5, 10)
            log_key_press('sleep', sleep_duration)
            sleep(sleep_duration)
            times = 0
def clear_console():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Mac and Linux
        os.system('clear')

def logo():
    logo = Fore.MAGENTA + """                                                                                        
                                                                                           
                          .                .,                                ., G:        
                         ;W               ,Wt j.                            ,Wt E#,    :
            ;           f#E GEEEEEEEL    i#D. EW,                   ..     i#D. E#t  .GE
          .DL         .E#f  ,;;L#K;;.   f#f   E##j                 ;W,    f#f   E#t j#K;
  f.     :K#L     LWLiWW;      t#E    .D#i    E###D.              j##,  .D#i    E#GK#f  
  EW:   ;W##L   .E#fL##Lffi    t#E   :KW,     E#jG#W;            G###, :KW,     E##D.   
  E#t  t#KE#L  ,W#;tLLG##L     t#E   t#f      E#t t##f         :E####, t#f      E##Wi   
  E#t f#D.L#L t#K:   ,W#i      t#E    ;#G     E#t  :K#E:      ;W#DG##,  ;#G     E#jL#D: 
  E#jG#f  L#LL#G    j#E.       t#E     :KE.   E#KDDDD###i    j###DW##,   :KE.   E#t ,K#j
  E###;   L###j   .D#j         t#E      .DW:  E#f,t#Wi,,,   G##i,,G##,    .DW:  E#t   jD
  E#K:    L#W;   ,WK,          t#E        L#, E#t  ;#W:   :K#K:   L##,      L#, j#t     
  EG      LE.    EG.            fE         jt DWi   ,KK: ;##D.    L##,       jt  ,;     
  ;       ;@     ,               :                       ,,,      .,,                   
                           
                                                                                        """
    print(logo)
logo()
print(Fore.CYAN + "Hypixel Skyblock Garden Macros Made By WST\n")

farmpicked = input(Fore.CYAN + " 1 | MELON / PUMPKIN\n 2 | WHEAT / CARROT / NETHER WART / POTATOES\n 3 | CANE\n 4 | LEFT\n")
print(farmpicked)

if int(farmpicked) == 1:
    farmprofit = 252
    clear_console()
    logo()
    print(Fore.CYAN + "Farm Picked: MELON / PUMPKIN")
    start = input(Fore.GREEN + "\nPress ENTER To Start Then Tab Back To Minecraft")
    if start == '':
        sleep(3)
        money = 0
        thread1 = threading.Thread(target=melon)
        thread2 = threading.Thread(target=output)
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
if int(farmpicked) == 2:
    farmprofit = 289
    clear_console()
    logo()
    print(Fore.CYAN + "Farm Picked: WHEAT / CARROT / NETHER WART / POTATOES")
    start = input(Fore.GREEN + "\nPress ENTER To Start Then Tab Back To Minecraft")
    if start == '':
        sleep(3)
        money = 0
        thread1 = threading.Thread(target=wcnp)
        thread2 = threading.Thread(target=output)
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
if int(farmpicked) == 3:
    farmprofit = 289
    clear_console()
    logo()
    print(Fore.CYAN + "Farm Picked: CANE")
    start = input(Fore.GREEN + "\nPress ENTER To Start Then Tab Back To Minecraft")
    if start == '':
        sleep(3)
        money = 0
        thread1 = threading.Thread(target=cane)
        thread2 = threading.Thread(target=output)
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
if int(farmpicked) == 4:
    farmprofit = 289
    clear_console()
    logo()
    print(Fore.CYAN + "Farm Picked: LEFT")
    start = input(Fore.GREEN + "\nPress ENTER To Start Then Tab Back To Minecraft")
    if start == '':
        sleep(3)
        money = 0
        thread1 = threading.Thread(target=left)
        thread2 = threading.Thread(target=output)
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()