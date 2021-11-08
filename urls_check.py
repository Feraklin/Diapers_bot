#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import json
import re


def main():
    with open(r'D:\Программирование\1\PodgyzBot\urlsCheck.json', "r", encoding="utf-8") as f:
        data = json.load(f)

    urlsEvro = data["urlsEvro"]
    urlsEvroCheck = []
    urlsOstrov = data["urlsOstrov"]
    urlsOstrovCheck = []
    urlsBuslik = data["urlsBuslik"]
    urlsBuslikCheck = []
    urlsMila = data["urlsMila"]
    urlsMilaCheck = []
    urlsForCheck = data["urlsForCheck"]

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "accept": "*/*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,be;q=0.6",
    }

    def get_html(url, params=None):
        r = requests.get(url, headers=headers, params=params)
        return r

    def get_content_buslik(html):
        urls = []
        soup = BeautifulSoup(html, "html.parser")
        items = soup.find_all("div", class_="col-sm-4 col-md-3 col-xs-6")
        for item in items:
            urls.append(
                item.find("a", class_="border-block__fast-preview hidden-xs").get(
                    "href"
                )
            )
        return urls

    def get_content_ostrov(html):
        urls = []
        soup = BeautifulSoup(html, "html.parser")
        items = soup.find_all(
            "div",
            class_="col-lg-3 col-md-4 col-sm-6 col-xs-6 col-xxs-12 item item-parent item_block",
        )
        for item in items:
            urls.append(
                item.find(
                    "a", class_="dark_link option-font-bold font_sm").get("href")
            )
        return urls

    def get_content_evro(html):
        urls = []
        soup = BeautifulSoup(html, "html.parser")
        items = soup.find_all("div", class_=re.compile(
            "^products_card products_card"))
        for item in items:
            urls.append(item.find("a", class_="fancy_ajax").get("href"))
        return urls

    def get_content_mila(html):
        urls = []
        soup = BeautifulSoup(html, "html.parser")
        items = soup.find_all("a", class_="showcase-element")
        for item in items:
            urls.append(item.get("href"))
        return urls

    # Парсинг списка URLов E-dostavka
    temp = -1
    i = 1
    while temp != len(urlsEvroCheck):
        temp = len(urlsEvroCheck)
        urlsEvroCheck += get_content_evro(
            get_html(
                "https://e-dostavka.by/catalog/3324.html?orderby=actions_products_top&brand%5BHuggies%5D=Huggies&price_from=&price_to=&_=1620996611428&lazy_steep="
                + str(i)
            ).text
        )
        i += 1

    temp = -1
    i = 1
    while temp != len(urlsEvroCheck):
        temp = len(urlsEvroCheck)
        urlsEvroCheck += get_content_evro(
            get_html(
                "https://e-dostavka.by/catalog/3324.html?orderby=actions_products_top&brand%5BPampers%5D=Pampers&brand%5BYokoSun%5D=YokoSun&price_from=&price_to=&utm_source=admitad&utm_medium=cpc&utm_campaign=admitad_glavnaya&admitad_uid=0feb18dc3c1cae3008f626e311efc2bf&target=admitad&tagtag_uid=0feb18dc3c1cae3008f626e311efc2bf&_=1620996980324&lazy_steep="
                + str(i)
            ).text
        )
        i += 1

    # Парсинг списка URLов Острова чистоты
    temp = -1
    i = 1
    while temp != len(urlsOstrovCheck):
        temp = len(urlsOstrovCheck)
        a = get_content_ostrov(
            get_html(
                "https://ostrov-shop.by/catalog/tovary-dlya-detey/gigiena-i-ukhod-za-detmi/podguzniki/filter/trademark-is-huggies-or-pampers/count_pack-from-37/apply/?ajax_get=Y&ajax_get_filter=Y&PAGEN_1="
                + str(i)
            ).text
        )
        for item in a:
            urlsOstrovCheck.append("https://ostrov-shop.by" + item)
        urlsOstrovCheck = list(set(urlsOstrovCheck))
        i += 1

    temp = -1
    i = 1
    while temp != len(urlsOstrovCheck):
        temp = len(urlsOstrovCheck)
        a = get_content_ostrov(
            get_html(
                "https://ostrov-shop.by/catalog/tovary-dlya-detey/gigiena-i-ukhod-za-detmi/podguzniki-trusiki/filter/trademark-is-huggies-or-pampers/count_pack-from-30/apply/?ajax_get=Y&ajax_get_filter=Y&PAGEN_1="
                + str(i)
            ).text
        )
        for item in a:
            urlsOstrovCheck.append("https://ostrov-shop.by" + item)
        urlsOstrovCheck = list(set(urlsOstrovCheck))
        i += 1

    # Парсинг списка URLов Буслика
    temp = -1
    i = 1
    while temp != len(urlsBuslikCheck):
        temp = len(urlsBuslikCheck)
        a = get_content_buslik(
            get_html(
                "https://buslik.by/catalog/podguzniki/podguzniki_1/filter/brand-is-active_baby-or-elite_soft-or-premium_care-or-sleep_play-or-ultra_comfort-or-yokosun/kolichestvo_v_upakovke-from-38/apply/?PAGEN_1="
                + str(i)
            ).text
        )
        for item in a:
            urlsBuslikCheck.append("https://buslik.by" + item)
        i += 1

    temp = -1
    i = 1
    while temp != len(urlsBuslikCheck):
        temp = len(urlsBuslikCheck)
        a = get_content_buslik(
            get_html(
                "https://buslik.by/catalog/podguzniki/trusiki_podguzniki/filter/brand-is-active_baby-or-elite_soft-or-premium_care-or-ultra_comfort-or-yokosun/kolichestvo_v_upakovke-from-28/apply/?PAGEN_1="
                + str(i)
            ).text
        )
        for item in a:
            urlsBuslikCheck.append("https://buslik.by" + item)
        i += 1

    # Парсинг списка URLов Мила
    temp = -1
    i = 1
    while temp != len(urlsMilaCheck):
        temp = len(urlsMilaCheck)
        a = get_content_mila(
            get_html(
                "https://mila.by/catalog/dlya-detey-i-mam/podguzniki-i-pelenki/podguzniki/?arrFilter_7629_2606433189=Y&arrFilter_7629_322782530=Y&set_filter=%D0%9F%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C&page=" +
                str(i)
            ).text
        )
        for item in a:
            urlsMilaCheck.append("https://mila.by" + item)
        urlsMilaCheck = list(set(urlsMilaCheck))
        i += 1

    temp = -1
    i = 1
    while temp != len(urlsMilaCheck):
        temp = len(urlsMilaCheck)
        a = get_content_mila(
            get_html(
                "https://mila.by/catalog/dlya-detey-i-mam/podguzniki-i-pelenki/podguzniki-trusiki/?arrFilter_7629_2606433189=Y&arrFilter_7629_322782530=Y&set_filter=%D0%9F%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C&page=" +
                str(i)
            ).text
        )
        for item in a:
            urlsMilaCheck.append("https://mila.by" + item)
        urlsMilaCheck = list(set(urlsMilaCheck))
        i += 1

    for item in urlsEvroCheck:
        if urlsEvro.count(item) == 0:
            urlsForCheck.append(item)

    for item in urlsBuslikCheck:
        if urlsBuslik.count(item) == 0:
            urlsForCheck.append(item)

    for item in urlsOstrovCheck:
        if urlsOstrov.count(item) == 0:
            urlsForCheck.append(item)

    for item in urlsMilaCheck:
        if urlsMila.count(item) == 0:
            urlsForCheck.append(item)

    urlsForCheck = list(set(urlsForCheck))
    print(len(urlsForCheck))

    data = {
        "urlsForCheck": urlsForCheck,
        "urlsEvro": urlsEvro,
        "urlsOstrov": urlsOstrov,
        "urlsBuslik": urlsBuslik,
        "urlsMila": urlsMila,
    }

    with open(r"D:\Программирование\1\PodgyzBot\urlsCheck.json", "w", encoding="utf-8") as f:
        # with open(r"/home/feraklin1/bot1/answers.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Updated")


if __name__ == "__main__":
    main()
