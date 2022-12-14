import random
import smtplib
import pandas as pd
import datetime as dt
from time import sleep

my_email = 'mytestoneacc@gmail.com'
password = 'jxvtrzxauoflvciz'

is_on = True
birth_data = {
    'name': [],
    'email': [],
    'year': [],
    'month': [],
    'day': []
}
while is_on:
    now = dt.datetime.now()
    data = pd.read_csv('birthdays.csv')
    data['day'] = data.day == now.day
    data['month'] = data.month == now.month
    data = data.where(data['day'] == True)
    data = data.where(data['month'] == True)
    data.dropna(inplace=True)

    for row in data.values:
        with open(f'letter_templates/letter_{random.randint(1, 3)}.txt', mode='r') as file:
            msg = ''
            letter = file.readlines()
            for line in letter:
                msg += line.replace('[NAME]', row[0])
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                my_email,
                row[1],
                msg=f"Subject:Happy Birthday!\n\n{msg}"
            )

    sleep(86400)

