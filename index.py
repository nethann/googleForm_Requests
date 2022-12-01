import requests
from colorama import Fore
import random

from names import * 

class RequestForm : 
    def __init__(self):
        #url of the target form
        self.url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSf6-S4sKf0VaDRPiw_XbgZGm8BMxEIN5H1-qboagX806I7Smw/formResponse"
    def handleRequest(self): 

        #form data values
        randomGmail_Name = random.choice(name_lst)
        randomNum1 = random.randint(0,9)
        randomNum2 = random.randint(0,9)
        randomNum3 = random.randint(0,9)

        emailFormat = f'{randomGmail_Name}{randomNum1}{randomNum2}{randomNum3}@gmail.com'
        
        #google forms entries (can be found in console>Network>formResponse>Payload)
        #needs to submit response first
        form_data = { 
            'entry.508160737': '2039',
            'entry.1610205995' : '23093'
        }

        while True: 
            r = requests.post(self.url, data=form_data)


p1 = RequestForm()
p1.handleRequest()


# for i in range(0, 5): 
#     r = requests.post(url, data= form_data, )

