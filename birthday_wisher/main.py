##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import smtplib
import datetime
import random
import pandas

MY_EMAIL = "eichhornaureliano.gmz@gmail.com"
MY_PASSWORD = "fvdl xpfe nvlm usyz"

LETTERS = ["letter_templates/letter_1.txt",
           "letter_templates/letter_2.txt",
           "letter_templates/letter_3.txt"
           ]

def letter(name):
    """Create a letter"""
    with open(random.choice(LETTERS), "r") as file:
        content_letter = file.read()

        content_letter = content_letter.replace("[NAME]", f"{name}")

        return content_letter

def send_email(email, name):
    """send email automatically"""
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= MY_EMAIL,
                         password= MY_PASSWORD
                         )
        connection.sendmail(from_addr= MY_EMAIL,
                            to_addrs=email,
                            msg=f"Subject: Happy Birthday\n\n"
                                f"{letter(name)}")



#comprobar la fecha de hoy
date = datetime.datetime.now()

day_now = date.day
month_now = date.month

df = pandas.read_csv("birthdays.csv")
for index, row in df.iterrows():
    if row["month"] == month_now and row["day"] == day_now:
        send_email(email=row["email"], name= row["name"])
