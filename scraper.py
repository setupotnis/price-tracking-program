import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.ca/Sony-Full-Frame-Interchangeable-Digital-28-70mm/dp/B00FRDV06I/ref=sr_1_4?keywords=sony+a7+camera&qid=1562387270&s=gateway&sr=8-4'

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = int(price[5] + price[7:10]) 

    if converted_price < 1200:
        send_mail()

    print(converted_price)
    print(title.strip())

    def send_email():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('setupotnis@gmail.com', GOOGLE_PASS)

        subject = 'Price fell down!!'
        body = 'Check the amazon link https://www.amazon.ca/Sony-Full-Frame-Interchangeable-Digital-28-70mm/dp/B00FRDV06I/ref=sr_1_4?keywords=sony+a7+camera&qid=1562387270&s=gateway&sr=8-4'
        msg = ("Subject: %s\n\n %s" % subject, body) 
            
        server.sendmail(
            'setupotnis@gmail.com',
            'setupotnis@gmail.com',
            msg
        )
        print('HEY EMAIL HAS BEEN SENT!')

        server.quit()
check_price()
