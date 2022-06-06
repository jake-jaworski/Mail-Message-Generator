import smtplib
import datetime as dt
import random

email = "etest5469@gmail.com"
password = "12pass34"

# select random quote
with open(file="quotes.txt") as quotes:
    quote_list = quotes.readlines()
    random_quote = random.choice(quote_list)

# send email if monday
timestamp = dt.datetime.now()
if timestamp.weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=email,
                            msg=f"Subject:Test\n\n{random_quote}")
        connection.close()
