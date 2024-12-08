#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas as pd
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"
SMTP_SERVER = "YOUR EMAIL PROVIDER SMTP SERVER ADDRESS"

today = datetime.now()
today_tuple = (today.month, today.day)

birthdays_data = pd.read_csv("birthdays.csv")
birthdays_dict = {
    (row["month"], row["day"]): row for _, row in birthdays_data.iterrows()
}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    letter_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(letter_path) as letter_file:
        letter_contents = letter_file.read()
        personalized_letter = letter_contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
        )

