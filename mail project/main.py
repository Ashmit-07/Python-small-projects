import smtplib
import datetime as dt
import random

my_email = 'ashmit.testing@gmail.com'
password = 'vfxl baiy yuyo ojoq'


now = dt.datetime.now() 
weekday = now.weekday()


with open(r"small projects medium\mail project\quotes.txt") as quote_files:
    all_quotes = quote_files.readlines()
    quote = random.choice (all_quotes)
print (quote)

with smtplib.SMTP ("smtp.gmail.com") as connection: 
    connection.starttls ()                          #! secures the connection
    connection.login (user = my_email, password = password )
    connection.sendmail(from_addr= my_email, to_addrs= "ashmit79pradhan@gmail.com", msg = f"Subject:Daily Motivation\n\n {quote}")   


