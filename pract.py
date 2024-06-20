from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_price(text: str):
    return float(
        text.get_text().replace("$", "").replace("", "") .replace("\n", "").replace(",", "")
    )


html_code = urlopen("https://coinranking.com/")
bs4 = BeautifulSoup(html_code.read(), "lxml")
table = bs4.find_all("div", {"class": "valuta"})
valuefor= 50

count = 0
total: float = 0
batch_for = 0

for i in range(0, valuefor, 2):
    count = count + 1
    price = get_price(table[i])
    print(price)
    total = total + price

    if count == 5:
        batch = batch_for+ 1
        print(f"avg [{batch_for}] : { total / 5}")
        print("-------------------------")
        total = 0
        count = 0