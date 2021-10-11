import requests  # for HTTP requests
from bs4 import BeautifulSoup  # for scrape the website using HTML parser

url = 'https://www.freecodecamp.org/news/'
http_response = requests.get(url)

content = http_response.content

soup = BeautifulSoup(content, "html.parser")

# finding title of the articles
for i in soup.find_all('h2', attrs={'class':'post-card-title'}):
    txt = i.text
    print(f'-> {txt.strip()}')

print(f'******************** Website: {"https://www.freecodecamp.org/news/"} ********************')