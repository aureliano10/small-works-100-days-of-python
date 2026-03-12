import smtplib
import datetime
import random

my_email = "eichhornaureliano.gmz@gmail.com"
password = "fvdl xpfe nvlm usyz"

def what_day(num):

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[num]

    if num == 0:
        return "Monday"
    elif num == 1:
        return "Tuesday"
    elif num == 2:
        return "Wednesday"
    elif num == 3:
        return "Thursday"
    elif num == 4:
        return "Friday"
    elif num == 5:
        return "Saturday"
    elif num == 6:
        return "Sunday"

with open("quotes.txt") as file:
    lines_list = file.readlines()

#quitar los saltos de linea en cada oracion
lines_list = [line.strip() for line in lines_list]

day_info = datetime.datetime.now()
day = day_info.weekday()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= my_email,
                     password= password
                     )
    connection.sendmail(from_addr= my_email,
                        to_addrs= my_email,
                        msg=f"Subject:{what_day(day)}"
                            f"\n\n{random.choice(lines_list)}"
                        )

