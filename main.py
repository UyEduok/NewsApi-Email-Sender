import requests
import os
from send_email import send_email

topics = 'crypto AND tesla AND (ethereum OR litecoin)'

API_KEY = os.environ['API_KEY']
url = f'https://newsapi.org/v2/everything?q={topics}&' \
      'from=2023-06-02&' \
      'sortBy=publishedAt&' \
      'apiKey=f46b85bf55714f9ebfdcb0e60cf1a2c0&' \
      'language=en'


# make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
body = ''
for article in content['articles'][:10]:
    if article['title'] is not None:
        body = "Subject: Today's news" + '\n' + body + article['title'].title() \
               + '\n' + article['description'] + '\n' + article['url'] + 2*'\n'

message = body.encode('utf-8')
send_email(message)



