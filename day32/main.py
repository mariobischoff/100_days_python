import smtplib
import pandas as pd 
import datetime as dt
import random
import os

sender = "mario@dev.com"

path_templates = os.path.abspath("letter_templates")
num_templates = len(os.listdir(path_templates))

birthdays_df = pd.read_csv("birthdays.csv")
now = dt.datetime.now()

birthdays = birthdays_df[(birthdays_df["month"] == now.month) & (birthdays_df["day"] == now.day)]

for index, birthday in birthdays.iterrows():

    num_template = random.randint(1, num_templates)
    with open(f"letter_templates/letter_{num_template}.txt") as file:
        template = file.read()

    message = template.replace("[NAME]", birthday["name"])

    with smtplib.SMTP("localhost", 1025) as connection:
        connection.sendmail(sender, birthday["email"], f"Subject:Happy Birthday!\n\n{message}")
