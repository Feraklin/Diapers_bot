#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import json
import re


def main():
    with open("urls_for_check_base.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    urls_evro = data["urls_evro"]
    urls_evro_check = []
    urls_ostrov = data["urls_ostrov"]
    urls_ostrov_check = []
    urls_buslik = data["urls_buslik"]
    urls_buslik_check = []
    urls_mila = data["urls_mila"]
    urls_mila_check = []
    urls_for_check = data["urls_for_check"]

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
                item.find("a", class_="dark_link option-font-bold font_sm").get("href")
            )
        return urls

    def get_content_evro(html):
        urls = []
        soup = BeautifulSoup(html, "html.parser")
        items = soup.find_all("div", class_=re.compile("^products_card products_card"))
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

    # E-dostavka
    temp = -1
    i = 1
    while temp != len(urls_evro_check):
        temp = len(urls_evro_check)
        urls_evro_check += get_content_evro(
            get_html(
                "https://e-dostavka.by/catalog/3324.html?orderby=actions_products_top&brand%5BHuggies%5D=Huggies&price_from=&price_to=&_=1620996611428&lazy_steep="
                + str(i)
            ).text
        )
        i += 1

    temp = -1
    i = 1
    while temp != len(urls_evro_check):
        temp = len(urls_evro_check)
        urls_evro_check += get_content_evro(
            get_html(
                "https://e-dostavka.by/catalog/3324.html?orderby=actions_products_top&brand%5BPampers%5D=Pampers&brand%5BYokoSun%5D=YokoSun&price_from=&price_to=&utm_source=admitad&utm_medium=cpc&utm_campaign=admitad_glavnaya&admitad_uid=0feb18dc3c1cae3008f626e311efc2bf&target=admitad&tagtag_uid=0feb18dc3c1cae3008f626e311efc2bf&_=1620996980324&lazy_steep="
                + str(i)
            ).text
        )
        i += 1

    # Ostrov.by
    temp = -1
    i = 1
    while temp != len(urls_ostrov_check):
        temp = len(urls_ostrov_check)
        a = get_content_ostrov(
            get_html(
                "https://ostrov-shop.by/catalog/tovary-dlya-detey/gigiena-i-ukhod-za-detmi/podguzniki/filter/trademark-is-huggies-or-pampers/count_pack-from-37/apply/?ajax_get=Y&ajax_get_filter=Y&PAGEN_1="
                + str(i)
            ).text
        )
        for item in a:
            urls_ostrov_check.append("https://ostrov-shop.by" + item)
        urls_ostrov_check = list(set(urls_ostrov_check))
        i += 1

    temp = -1
    i = 1
    while temp != len(urls_ostrov_check):
        temp = len(urls_ostrov_check)
        a = get_content_ostrov(
            get_html(
                "https://ostrov-shop.by/catalog/tovary-dlya-detey/gigiena-i-ukhod-za-detmi/podguzniki-trusiki/filter/trademark-is-huggies-or-pampers/count_pack-from-30/apply/?ajax_get=Y&ajax_get_filter=Y&PAGEN_1="
                + str(i)
            ).text
        )
        for item in a:
            urls_ostrov_check.append("https://ostrov-shop.by" + item)
        urls_ostrov_check = list(set(urls_ostrov_check))
        i += 1

    # Buslik.by
    temp = -1
    i = 1
    while temp != len(urls_buslik_check):
        temp = len(urls_buslik_check)
        a = get_content_buslik(
            get_html(
                "https://buslik.by/catalog/podguzniki/podguzniki_1/filter/brand-is-active_baby-or-elite_soft-or-premium_care-or-sleep_play-or-ultra_comfort-or-yokosun/kolichestvo_v_upakovke-from-38/apply/?PAGEN_1="
                + str(i)
            ).text
        )
        for item in a:
            urls_buslik_check.append("https://buslik.by" + item)
        i += 1

    temp = -1
    i = 1
    while temp != len(urls_buslik_check):
        temp = len(urls_buslik_check)
        a = get_content_buslik(
            get_html(
                "https://buslik.by/catalog/podguzniki/trusiki_podguzniki/filter/brand-is-active_baby-or-elite_soft-or-premium_care-or-ultra_comfort-or-yokosun/kolichestvo_v_upakovke-from-28/apply/?PAGEN_1="
                + str(i)
            ).text
        )
        for item in a:
            urls_buslik_check.append("https://buslik.by" + item)
        i += 1

    # Mila.by
    temp = -1
    i = 1
    while temp != len(urls_mila_check):
        temp = len(urls_mila_check)
        a = get_content_mila(
            get_html(
                "https://mila.by/catalog/dlya-detey-i-mam/podguzniki-i-pelenki/podguzniki/?arrFilter_7629_2606433189=Y&arrFilter_7629_322782530=Y&set_filter=%D0%9F%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C&page="
                + str(i)
            ).text
        )
        for item in a:
            urls_mila_check.append("https://mila.by" + item)
        urls_mila_check = list(set(urls_mila_check))
        i += 1

    temp = -1
    i = 1
    while temp != len(urls_mila_check):
        temp = len(urls_mila_check)
        a = get_content_mila(
            get_html(
                "https://mila.by/catalog/dlya-detey-i-mam/podguzniki-i-pelenki/podguzniki-trusiki/?arrFilter_7629_2606433189=Y&arrFilter_7629_322782530=Y&set_filter=%D0%9F%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C&page="
                + str(i)
            ).text
        )
        for item in a:
            urls_mila_check.append("https://mila.by" + item)
        urls_mila_check = list(set(urls_mila_check))
        i += 1

    for item in urls_evro_check:
        if urls_evro.count(item) == 0:
            urls_for_check.append(item)

    for item in urls_buslik_check:
        if urls_buslik.count(item) == 0:
            urls_for_check.append(item)

    for item in urls_ostrov_check:
        if urls_ostrov.count(item) == 0:
            urls_for_check.append(item)

    for item in urls_mila_check:
        if urls_mila.count(item) == 0:
            urls_for_check.append(item)

    urls_for_check = list(set(urls_for_check))
    print(len(urls_for_check))

    data = {
        "urls_for_check": urls_for_check,
        "urls_evro": urls_evro,
        "urls_ostrov": urls_ostrov,
        "urls_buslik": urls_buslik,
        "urls_mila": urls_mila,
    }

    with open("urls_for_check_base.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Updated")


if __name__ == "__main__":
    main()
