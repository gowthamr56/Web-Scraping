# FREECODECAMP ARTICLE SCRAPER USING PYTHON

# for HTTP requests
import requests

# for scrape the website using HTML parser
from bs4 import BeautifulSoup

# to send mail
import smtplib  # SMTP -> SIMPLE MAIL TRANSFER PROTOCOL

# for email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

# to get current date
date = str(datetime.datetime.now()).split(' ')[0]
# print(date)

url = 'https://www.freecodecamp.org/news/'
http_response = requests.get(url)

content = http_response.content

soup = BeautifulSoup(content, "html.parser")

# finding title of the articles
content = ''
for i, j in enumerate(soup.find_all('h2', attrs={'class':'post-card-title'})):
    txt = j.text
    # print(f'-> {txt.strip()}')
    content += f"{i+1} :: {txt.strip()}\n"

content += f"\nWebsite: {url}"
# print(content)

print("Composing Mail...")

SERVER = 'smtp.gmail.com'  # for gmail server
PORT = 587  # port number for gmail
FROM = 'abc@gmail.com'  # FROM email address
TO = 'xyz@gmail.com'  # TO email address(can be list)
PWD = '********'  # PASSWORD

msg = MIMEMultipart()

msg['From'] = FROM
msg['To'] = TO
msg['Subject'] = f"FREECODECAMP ARTICLES: {date}"
msg.attach(MIMEText(content))

# for server initialization
print("Initiating Server...")
server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(0)  # can give 1 as a parameter to know the details
server.ehlo()
server.starttls()
server.login(FROM, PWD)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')
server.quit()
