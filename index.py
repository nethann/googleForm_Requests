import requests
import random

from names import * 

#requests session
ss = requests.Session()

#url of the google forms
url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdRvvKSHrRSgKKnECA9TRTlUuWTRfkB9ZT8VBY0GltUcJ5i-w/formResponse"

counter = 0

#infinite loop
while True: 
    #random number grabber
            randomNum1 = random.randint(1,9)
            randomNum2 = random.randint(1,9)
            randomNum3 = random.randint(1,9)


    #gmail grabber
            randomGmail_Name = random.choice(name_lst)
            emailFormat = f'{randomGmail_Name}{randomNum1}{randomNum2}{randomNum3}@gmail.com'

    #form Data
            form_data = { 
            'emailAddress': f'{emailFormat}',
            'entry.1545936664' : f'{random.randint(10,50)}'
            }

            #posting the data to google forms
            counter += 1
            ss.post(url, data=form_data)
            print(f'{counter} forms submitted')
