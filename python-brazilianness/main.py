from datetime import datetime, timedelta
from dates import Dates
from dates import Register

# today = Dates()
# print(today.registration_time())

today = Register()
print(today.registered_days())


'''
today = datetime.today()
today_formated = today.strftime("%d/%m/%Y %H:%M")

print(today)
print(today_formated)
print(type(today_formated))
'''

<<<<<<< HEAD
=======
phone = "552126481234"
new_phone = PhonesBr(phone)

print(new_phone)
>>>>>>> b3c9b1a7492bdfb44ffb7c7aa7a2f668fc7db097
