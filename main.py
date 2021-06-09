##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import random
import pandas as pd
import datetime as dt

email_address = "REPLACE WITH YOUR GMAIL ADDRESS"
password = "REPLACE WITH YOUR PASSWORD"
now = dt.datetime.now()
month = now.month
day = now.day


def get_random_letter():
    """Gets a random letter form the template directory and returns it"""
    letter_templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    template = random.choice(letter_templates)

    with open(f"./letter_templates/{template}") as letter:
        return letter.read()


def send_mail(destination, content):
    """Sends an email to the selected recipient with the provided content as an email body"""
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_address, password=password)
        connection.sendmail(
            from_addr=email_address,
            to_addrs=destination,
            msg=f"Subject:Happy birthday!\n\n{content}",
        )


df = pd.read_csv("./birthdays.csv")

for i in range(len(df.name)):
    if df.month[i] == month and df.day[i] == day:
        letter = get_random_letter().replace("[NAME]", df.name[i])
        send_mail(df.email[i], letter)
