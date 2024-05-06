import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2024, 11, 1)

days_away = next_birthday - today

if today == next_birthday:
  print(bday_messages.random_message) #to call the function from bday_messages
else:
  print(f'My next birthday is {days_away.days} days away!') #include .days to only show days instead of days + time