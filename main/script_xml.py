import requests
from bs4 import BeautifulSoup
import json


source = requests.get('http://open.api.ebay.com/shopping?callname=GetSingleItem&responseencoding=XML&appid=MarcusEh-MyKey-PRD-6c230b90b-02352ef8&siteid=0&version=1027&ItemID=192718849942&IncludeSelector=ItemSpecifics,Details').text
soup = BeautifulSoup(source, 'xml')
# print(soup.prettify())

for item in soup.find_all('Item'):

    # Item Title
    title = item.Title.text
    print(title)

    # Item Subtitle
    try:
        subtitle = item.Subtitle.text
    except Exception as e:
        subtitle = None
    print(subtitle)

    # Price
    price = item.CurrentPrice.text
    print(price)

    # Currency Code
    currency = item.CurrentPrice
    print(currency['currencyID'])

    # Ratting
    rating = item.Seller.FeedbackScore.text
    print(rating)

    # Seller User Id
    seller = item.Seller.UserID.text
    print(seller)

# Error -> TypeError: Object of type 'Tag' is not JSON serializable
# Solution -> after currency put text

context = {
    "title": title,
    "subtitle": subtitle,
    "price": price,
    "currency": currency.text,
    "rating": rating,
    "seller": seller,
}

print(context)
json_data = json.dumps(context)
print(json_data)