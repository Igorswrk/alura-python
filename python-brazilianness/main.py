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

