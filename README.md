# Daily News API to Email
This is a Python application that fetches news articles using the NewsAPI and sends them to an email address every day. It allows you to stay updated with the latest news conveniently in your inbox.

### Prerequisites
Before running the application, make sure you have the following:

Python 3.x installed on your system
NewsAPI API key. You can obtain it from NewsAPI.org
Gmail account credentials (username and password)
### Installation
##### Clone the repository: 
git clone <repository_url>
##### Install the required dependencies:
pip install -r requirements.txt
Set up the configuration:

Open main.py and send_email.py file.
Update the NEWS_API_KEY variable with your NewsAPI API key.
Update the GMAIL_USERNAME and GMAIL_PASSWORD variables with your Gmail account credentials.

### Usage
Run the application:
python app.py

The application will fetch the latest news articles from the NewsAPI.

It will send email to the specified email address with the news articles as the content.

Customization
You can modify the email subject and content in the app.py file to suit your preferences.