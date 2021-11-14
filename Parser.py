#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import json
from text_generator import text_generator

with open("best_results_model.json", "r", encoding="utf-8") as f:
    best_results_model = json.load(f)["best_results_model"]


with open("urls.json", "r", encoding="utf-8") as f:
    base_of_urls_and_prices = json.load(f)["urls"]

urls = len(base_of_urls_and_prices)

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,be;q=0.6",
}


def get_html(url, params=None):
    r = requests.get(url, headers=headers, params=params)
    return r


def get_content_mila(id, params=None):
    r = requests.post(
        "https://api.mila.by/get-all-offer/",
        headers=headers,
        params=params,
        data={"product_id": id},
    )
    return r


def get_content_buslik(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="border-b-block clearfix total_cost")
    for item in items:
        price = item.find("p", class_="total-price blue-text").get_text(strip=True)[0:5]
    try:
        sales = soup.find_all("div", class_="flag-wrapper")
        for i in sales:
            sale = i.find("div", class_="flag flag_vtorup80").get_text(strip=True)
            return price + sale
    except:
        return price
    return price


def get_content_ostrov(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="price font-bold font_mxs", limit=1)
    for item in items:
        price = item.find("span", class_="price_value").get_text(strip=True)
    return price


def get_content_evro(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="right")
    for item in items:
        price = item.find("div", class_="price").get_text(strip=True)
    return price


def price_parsing():
    for i in range(urls):
        if base_of_urls_and_prices[i][2][8:9] == "m":  # Mila.by
            try:
                html_mila = get_content_mila(base_of_urls_and_prices[i][2][-8:-1])
                if html_mila.status_code == 200:
                    try:
                        price_mila = html_mila.json()["offer"]["PRICES"]["PRICE"][
                            "PRICE"
                        ]
                        base_of_urls_and_prices[i][4] = price_mila
                        base_of_urls_and_prices[i][3] = str(
                            float(price_mila) * 100 / int(base_of_urls_and_prices[i][1])
                        )[0:5]
                    except:
                        print("Нет в наличии: ", base_of_urls_and_prices[i][2])
                        base_of_urls_and_prices[i][3] = 0
                else:
                    print("error Mila with url:" + base_of_urls_and_prices[i][2])
            except:
                pass
        elif base_of_urls_and_prices[i][2][8:9] == "o":  # ostrov-shop.by
            try:
                html_ostrov = get_html(base_of_urls_and_prices[i][2])
                if html_ostrov.status_code == 200:
                    try:
                        price_ostrov = get_content_ostrov(html_ostrov.text)
                        base_of_urls_and_prices[i][4] = price_ostrov[0:5]
                        base_of_urls_and_prices[i][3] = str(
                            float(price_ostrov[0:5])
                            * 100
                            / base_of_urls_and_prices[i][1]
                        )[0:5]
                    except:
                        print("Нет в наличии: ", base_of_urls_and_prices[i][2])
                        base_of_urls_and_prices[i][3] = 0
                else:
                    print("error Ostrov with url:" + base_of_urls_and_prices[i][2])
            except:
                pass

        elif base_of_urls_and_prices[i][2][8:9] == "e":  # e-dostavka.by
            try:
                html_evro = get_html(base_of_urls_and_prices[i][2])
                if html_evro.status_code == 200:
                    try:
                        price_evro = get_content_evro(html_evro.text)
                        base_of_urls_and_prices[i][4] = (
                            price_evro[0:2] + price_evro[3:6]
                        )
                        base_of_urls_and_prices[i][3] = str(
                            float(price_evro[0:2] + price_evro[3:6])
                            * 100
                            / base_of_urls_and_prices[i][1]
                        )[0:5]
                    except:
                        print("Нет в наличии: ", base_of_urls_and_prices[i][2])
                        base_of_urls_and_prices[i][3] = 0
                else:
                    print("error Evro with url:" + base_of_urls_and_prices[i][2])
            except:
                pass

        elif base_of_urls_and_prices[i][2][8:9] == "b":  # Buslik.by
            try:
                html_buslik = get_html(base_of_urls_and_prices[i][2])
                if html_buslik.status_code == 200:
                    try:
                        price_buslik = get_content_buslik(html_buslik.text)
                        base_of_urls_and_prices[i][4] = price_buslik.replace(",", ".")[
                            0:5
                        ]
                        if len(price_buslik) > 5:
                            base_of_urls_and_prices[i][3] = str(
                                float(price_buslik.replace(",", ".")[0:5])
                                * (2 - int(price_buslik[6:8]) / 100)
                                * 100
                                / (2 * base_of_urls_and_prices[i][1])
                            )[0:5]
                        else:
                            base_of_urls_and_prices[i][3] = str(
                                float(price_buslik.replace(",", ".")[0:5])
                                * 100
                                / base_of_urls_and_prices[i][1]
                            )[0:5]
                    except:
                        print("Нет в наличии: ", base_of_urls_and_prices[i][2])
                        base_of_urls_and_prices[i][3] = 0
                else:
                    print("error Buslik with url:" + base_of_urls_and_prices[i][2])
            except:
                pass


def find_min(base_of_urls_and_prices):
    best_results = best_results_model
    for i in range(urls):
        if float(base_of_urls_and_prices[i][3]) > 0:
            for j in range(len(best_results)):
                if base_of_urls_and_prices[i][0][0:6] == best_results[j][0] and float(
                    base_of_urls_and_prices[i][3]
                ) < float(best_results[j][1]):
                    best_results[j][1] = base_of_urls_and_prices[i][3]
                    best_results[j][2] = str(base_of_urls_and_prices[i][1])
                    best_results[j][3] = base_of_urls_and_prices[i][2][8:9]
                    best_results[j][4] = base_of_urls_and_prices[i][4]
    return best_results


def renaming(best_results):
    for i in range(len(best_results)):
        if best_results[i][3] == "b":
            best_results[i][3] = "Буслик"
        elif best_results[i][3] == "o":
            best_results[i][3] = "Остров Чистоты"
        elif best_results[i][3] == "e":
            best_results[i][3] = "Е-доставка"
        elif best_results[i][3] == "m":
            best_results[i][3] = "Мила"
    return best_results


def update():
    price_parsing()
    best_results = find_min(base_of_urls_and_prices)
    best_results = renaming(best_results)
    text_generator(best_results)
    print("Done")


if __name__ == "__main__":
    update()
