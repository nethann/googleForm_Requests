import requests
from colorama import Fore
import random

from names import * 


randomGmail_Name = random.choice(name_lst)
randomNum1 = random.randint(0,9)
randomNum2 = random.randint(0,9)
randomNum3 = random.randint(0,9)

class RequestForm : 
    def __init__(self):
        self.ss = requests.Session()
        #url of the target form
        self.url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdRvvKSHrRSgKKnECA9TRTlUuWTRfkB9ZT8VBY0GltUcJ5i-w/formResponse"
    def handleRequest(self): 

        emailFormat = f'{randomGmail_Name}{randomNum1}{randomNum2}{randomNum3}@gmail.com'
        print(emailFormat)
        
        #google forms entries (can be found in console>Network>formResponse>Payload)
        #needs to submit response first
        form_data = { 
            'emailAddress': f'{random.choice(name_lst)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}@gmail.com',
            'entry.1545936664' : f'{random.randint(10,50)}'
        }

        x = 0

        while True: 
            # self.ss.post(self.url, data=form_data)
            # print(form_data)
            x += 1
            # print(f'{x} forms submitted')


p1 = RequestForm()
p1.handleRequest()