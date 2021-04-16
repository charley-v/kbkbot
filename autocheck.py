import requests
import time

from bs4 import BeautifulSoup
from twilio.rest import Client

account_sid = "" 
aut_token = ""
url = ''
headers = {""}

def check_in_stock():
    webpage_response = requests.get(url, headers=headers)
    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, "html.parser")

    for i in soup.find_all('button', {'class': 'btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button'}):
        return i.text.strip()

def notification():
    client = Client(account_sid, aut_token)
    message = client.messages.create(
    to="",
    from_="",
    body= ""
    )
    return message.sid


def main():
    while True:
        status = check_in_stock()
        if status:
            print(notification)
            break
        else:
            print("Not in stock")
            time.sleep(900)


