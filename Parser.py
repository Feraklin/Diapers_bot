#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import json

res = [
    ["PPCP_1", "200", "0", "0", "0"],
    ["PNBP_1", "200", "0", "0", "0"],
    ["HESP_1", "200", "0", "0", "0"],
    ["PPCP_2", "200", "0", "0", "0"],
    ["PNBP_2", "200", "0", "0", "0"],
    ["HESP_2", "200", "0", "0", "0"],
    ["PPCP_3", "200", "0", "0", "0"],
    ["PABP_3", "200", "0", "0", "0"],
    ["HESP_3", "200", "0", "0", "0"],
    ["HUCP_3", "200", "0", "0", "0"],
    ["PPCP_4", "200", "0", "0", "0"],
    ["PABP_4", "200", "0", "0", "0"],
    ["HESP_4", "200", "0", "0", "0"],
    ["HUCP_4", "200", "0", "0", "0"],
    ["PPCT_3", "200", "0", "0", "0"],
    ["PABT_3", "200", "0", "0", "0"],
    ["HEST_3", "200", "0", "0", "0"],
    ["HUCT_3", "200", "0", "0", "0"],
    ["PPCT_4", "200", "0", "0", "0"],
    ["PABT_4", "200", "0", "0", "0"],
    ["HEST_4", "200", "0", "0", "0"],
    ["HUCT_4", "200", "0", "0", "0"],
    ["PPCT_5", "200", "0", "0", "0"],
    ["PABT_5", "200", "0", "0", "0"],
    ["HEST_5", "200", "0", "0", "0"],
    ["HUCT_5", "200", "0", "0", "0"],
    ["PPCT_6", "200", "0", "0", "0"],
    ["PABT_6", "200", "0", "0", "0"],
    ["HEST_6", "200", "0", "0", "0"],
    ["HUCT_6", "200", "0", "0", "0"],
    ["YSNP_1", "200", "0", "0", "0"],
    ["YSPP_1", "200", "0", "0", "0"],
    ["YECP_1", "200", "0", "0", "0"],
    ["YSNP_2", "200", "0", "0", "0"],
    ["YSPP_2", "200", "0", "0", "0"],
    ["YECP_2", "200", "0", "0", "0"],
    ["YSNP_3", "200", "0", "0", "0"],
    ["YSNP_4", "200", "0", "0", "0"],
    ["YSET_3", "200", "0", "0", "0"],
    ["YSNT_3", "200", "0", "0", "0"],
    ["YSET_4", "200", "0", "0", "0"],
    ["YSNT_4", "200", "0", "0", "0"],
    ["YSPT_4", "200", "0", "0", "0"],
    ["YECT_4", "200", "0", "0", "0"],
    ["YSET_5", "200", "0", "0", "0"],
    ["YSNT_5", "200", "0", "0", "0"],
    ["YSPT_5", "200", "0", "0", "0"],
    ["YSET_6", "200", "0", "0", "0"],
    ["YSNT_6", "200", "0", "0", "0"],
    ["YECT_6", "200", "0", "0", "0"],
]

models = len(res)
with open(r"D:\Программирование\1\PodgyzBot\urls.json", "r", encoding="utf-8") as f:
    # with open("/home/feraklin1/bot1/urls.json", "r", encoding="utf-8") as f:
    baseForCalc = json.load(f)["urls"]

URLS = len(baseForCalc)

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,be;q=0.6",
}


def get_html(url, params=None):
    r = requests.get(url, headers=headers, params=params)
    return r


def get_content_mila(id, params=None):
    r = requests.post("https://api.mila.by/get-all-offer/", headers=headers, params=params,
                      data={'product_id': id})
    return r


def get_content_buslik(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="border-b-block clearfix total_cost")
    for item in items:
        price = item.find(
            "p", class_="total-price blue-text").get_text(strip=True)[0:5]
    try:
        sales = soup.find_all("div", class_="flag-wrapper")
        for i in sales:
            sale = i.find("div", class_="flag flag_vtorup80").get_text(
                strip=True)
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


# def get_content_mila(html):
#     soup = BeautifulSoup(html, "html.parser")
#     items = soup.find_all("div", class_="card-price", limit=1)
#     print(items)
#     for item in items:
#         price = item.find("div", class_="price").get_text()
#     return price


def price_parsing():
    for i in range(URLS):
        # print("step:" + str(i + 1) + " of " + str(URLS))
        if baseForCalc[i][2][8:9] == "m":  # Мила
            try:
                html_mila = get_content_mila(baseForCalc[i][2][-8:-1])
                if html_mila.status_code == 200:
                    try:
                        price_mila = html_mila.json(
                        )["offer"]["PRICES"]["PRICE"]["PRICE"]
                        baseForCalc[i][4] = price_mila
                        baseForCalc[i][3] = str(
                            float(price_mila) * 100 / int(baseForCalc[i][1])
                        )[0:5]
                    except:
                        print("Нет в наличии: ", baseForCalc[i][2])
                        baseForCalc[i][3] = 0
                else:
                    print("error Mila with url:" + baseForCalc[i][2])
            except:
                pass
        elif baseForCalc[i][2][8:9] == "o":  # Остров чистоты
            try:
                html_ostrov = get_html(baseForCalc[i][2])
                if html_ostrov.status_code == 200:
                    try:
                        price_ostrov = get_content_ostrov(html_ostrov.text)
                        baseForCalc[i][4] = price_ostrov[0:5]
                        baseForCalc[i][3] = str(
                            float(price_ostrov[0:5]) * 100 / baseForCalc[i][1]
                        )[0:5]
                    except:
                        print("Нет в наличии: ", baseForCalc[i][2])
                        baseForCalc[i][3] = 0
                else:
                    print("error Ostrov with url:" + baseForCalc[i][2])
            except:
                pass

        elif baseForCalc[i][2][8:9] == "e":  # Е-доставка
            try:
                html_evro = get_html(baseForCalc[i][2])
                if html_evro.status_code == 200:
                    try:
                        price_evro = get_content_evro(html_evro.text)
                        baseForCalc[i][4] = price_evro[0:2] + price_evro[3:6]
                        baseForCalc[i][3] = str(
                            float(price_evro[0:2] + price_evro[3:6])
                            * 100
                            / baseForCalc[i][1]
                        )[0:5]
                    except:
                        print("Нет в наличии: ", baseForCalc[i][2])
                        baseForCalc[i][3] = 0
                else:
                    print("error Evro with url:" + baseForCalc[i][2])
            except:
                pass

        elif baseForCalc[i][2][8:9] == "b":  # Буслик
            try:
                html_buslik = get_html(baseForCalc[i][2])
                if html_buslik.status_code == 200:
                    try:
                        price_buslik = get_content_buslik(html_buslik.text)
                        baseForCalc[i][4] = price_buslik.replace(",", ".")[0:5]
                        if len(price_buslik) > 5:
                            baseForCalc[i][3] = str(
                                float(price_buslik.replace(",", ".")[0:5])
                                * (2 - int(price_buslik[6:8]) / 100)
                                * 100
                                / (2 * baseForCalc[i][1])
                            )[0:5]
                        else:
                            baseForCalc[i][3] = str(
                                float(price_buslik.replace(",", ".")[0:5])
                                * 100
                                / baseForCalc[i][1]
                            )[0:5]
                    except:
                        print("Нет в наличии: ", baseForCalc[i][2])
                        baseForCalc[i][3] = 0
                else:
                    print("error Buslik with url:" + baseForCalc[i][2])
            except:
                pass


def calc_min():
    for i in range(URLS):
        if float(baseForCalc[i][3]) > 0:
            for j in range(models):
                if baseForCalc[i][0][0:6] == res[j][0] and float(
                    baseForCalc[i][3]
                ) < float(res[j][1]):
                    res[j][1] = baseForCalc[i][3]
                    res[j][2] = str(baseForCalc[i][1])
                    res[j][3] = baseForCalc[i][2][8:9]
                    res[j][4] = baseForCalc[i][4]


def renaming():
    for i in range(models):
        if res[i][3] == "b":
            res[i][3] = "Буслик"
        elif res[i][3] == "o":
            res[i][3] = "Остров Чистоты"
        elif res[i][3] == "e":
            res[i][3] = "Е-доставка"
        elif res[i][3] == "m":
            res[i][3] = "Мила"


def text():
    text_1 = (
        f"Pampers Premium Care: \n{str(res[0][1])} руб. за 100 штук при покупке упаковки {res[0][2]} шт. ({res[0][4]} руб.) в магазине {res[0][3]}"
        + "\n"
        + "\n"
        + f"Pampers New Baby-Dry: \n{str(res[1][1])} руб. за 100 штук при покупке упаковки {res[1][2]} шт. ({res[1][4]} руб.) в магазине {res[1][3]}"
        + "\n"
        + "\n"
        + f"Huggies Elite Soft: \n{str(res[2][1])} руб. за 100 штук при покупке упаковки {res[2][2]} шт. ({res[2][4]} руб.) в магазине {res[2][3]}"
        + "\n"
        + "\n"
        + f"YokoSun: \n{str(res[30][1])} руб. за 100 штук при покупке упаковки {res[30][2]} шт. ({res[30][4]} руб.) в магазине {res[30][3]}"
        + "\n"
        + "\n"
        + f"YokoSun Premium: \n{str(res[31][1])} руб. за 100 штук при покупке упаковки {res[31][2]} шт. ({res[31][4]} руб.) в магазине {res[31][3]}"
        + "\n"
        + "\n"
        + f"YokoSun ECO: \n{str(res[32][1])} руб. за 100 штук при покупке упаковки {res[32][2]} шт. ({res[32][4]} руб.) в магазине {res[32][3]}"
    )

    text_2 = (
        f"Pampers Premium Care: \n{str(res[3][1])} руб. за 100 штук при покупке упаковки {res[3][2]} шт. ({res[3][4]} руб.) в магазине {res[3][3]}"
        + "\n"
        + "\n"
        + f"Pampers New Baby-Dry: \n{str(res[4][1])} руб. за 100 штук при покупке упаковки {res[4][2]} шт. ({res[4][4]} руб.) в магазине {res[4][3]}"
        + "\n"
        + "\n"
        + f"Huggies Elite Soft: \n{str(res[5][1])} руб. за 100 штук при покупке упаковки {res[5][2]} шт. ({res[5][4]} руб.) в магазине {res[5][3]}"
        + "\n"
        + "\n"
        + f"YokoSun: \n{str(res[33][1])} руб. за 100 штук при покупке упаковки {res[33][2]} шт. ({res[33][4]} руб.) в магазине {res[33][3]}"
        + "\n"
        + "\n"
        + f"YokoSun Premium: \n{str(res[34][1])} руб. за 100 штук при покупке упаковки {res[34][2]} шт. ({res[34][4]} руб.) в магазине {res[34][3]}"
        + "\n"
        + "\n"
        + f"YokoSun ECO: \n{str(res[35][1])} руб. за 100 штук при покупке упаковки {res[35][2]} шт. ({res[35][4]} руб.) в магазине {res[35][3]}"
    )

    text_3 = (
        f"Pampers Premium Care: \n{str(res[6][1])} руб. за 100 штук при покупке упаковки {res[6][2]} шт. ({res[6][4]} руб.) в магазине {res[6][3]}"
        + "\n"
        + "\n"
        + f"Pampers Active Baby-Dry: \n{str(res[7][1])} руб. за 100 штук при покупке упаковки {res[7][2]} шт. ({res[7][4]} руб.) в магазине {res[7][3]}"
        + "\n"
        + "\n"
        + f"Huggies Elite Soft: \n{str(res[8][1])} руб. за 100 штук при покупке упаковки {res[8][2]} шт. ({res[8][4]} руб.) в магазине {res[8][3]}"
        + "\n"
        + "\n"
        + f"Huggies Ultra Comfort: \n{str(res[9][1])} руб. за 100 штук при покупке упаковки {res[9][2]} шт. ({res[9][4]} руб.) в магазине {res[9][3]}"
        + "\n"
        + "\n"
        + f"YokoSun: \n{str(res[36][1])} руб. за 100 штук при покупке упаковки {res[36][2]} шт. ({res[36][4]} руб.) в магазине {res[36][3]}"
    )

    text_4 = (
        f"Pampers Premium Care: \n{str(res[10][1])} руб. за 100 штук при покупке упаковки {res[10][2]} шт. ({res[10][4]} руб.) в магазине {res[10][3]}"
        + "\n"
        + "\n"
        + f"Pampers Active Baby-Dry: \n{str(res[11][1])} руб. за 100 штук при покупке упаковки {res[11][2]} шт. ({res[11][4]} руб.) в магазине {res[11][3]}"
        + "\n"
        + "\n"
        + f"Huggies Elite Soft: \n{str(res[12][1])} руб. за 100 штук при покупке упаковки {res[12][2]} шт. ({res[12][4]} руб.) в магазине {res[12][3]}"
        + "\n"
        + "\n"
        + f"Huggies Ultra Comfort: \n{str(res[13][1])} руб. за 100 штук при покупке упаковки {res[13][2]} шт. ({res[13][4]} руб.) в магазине {res[13][3]}"
        + "\n"
        + "\n"
        + f"YokoSun: \n{str(res[37][1])} руб. за 100 штук при покупке упаковки {res[37][2]} шт. ({res[37][4]} руб.) в магазине {res[37][3]}"
    )

    text_5 = (
        f"Pampers Premium Care: \n{str(res[14][1])} руб. за 100 штук при покупке упаковки {res[14][2]} шт. ({res[14][4]} руб.) в магазине {res[14][3]}"
        + "\n"
        + "\n"
        + f"Pampers Active Baby-Dry: \n{str(res[15][1])} руб. за 100 штук при покупке упаковки {res[15][2]} шт. ({res[15][4]} руб.) в магазине {res[15][3]}"
        + "\n"
        + "\n"
        + f"Huggies Elite Soft: \n{str(res[16][1])} руб. за 100 штук при покупке упаковки {res[16][2]} шт. ({res[16][4]} руб.) в магазине {res[16][3]}"
        + "\n"
        + "\n"
        + f"Huggies Ultra Comfort: \n{str(res[17][1])} руб. за 100 штук при покупке упаковки {res[17][2]} шт. ({res[17][4]} руб.) в магазине {res[17][3]}"
        + "\n"
        + "\n"
        + f"YokoSun Econom: \n{str(res[38][1])} руб. за 100 штук при покупке упаковки {res[38][2]} шт. ({res[38][4]} руб.) в магазине {res[38][3]}"
        + "\n"
        + "\n"
        + f"YokoSun: \n{str(res[39][1])} руб. за 100 штук при покупке упаковки {res[39][2]} шт. ({res[39][4]} руб.) в магазине {res[39][3]}"
    )

    text_6 = (
        f"Pampers Premium Care: \n{str(res[18][1])} руб. за 100 штук при покупке упаковки {res[18][2]} шт. ({res[18][4]} руб.) в магазине {res[18][3]}"
        + "\n"
        + "\n"
        + f"Pampers Active Baby-Dry: \n{str(res[19][1])} руб. за 100 штук при покупке упаковки {res[19][2]} шт. ({res[19][4]} руб.) в магазине {res[19][3]}"
        + "\n"
        + "\n"
        + f"Huggies Elite Soft: \n{str(res[20][1])} руб. за 100 штук при покупке упаковки {res[20][2]} шт. ({res[20][4]} руб.) в магазине {res[20][3]}"
        + "\n"
        + "\n"
        + f"Huggies Ultra Comfort: \n{str(res[21][1])} руб. за 100 штук при покупке упаковки {res[21][2]} шт. ({res[21][4]} руб.) в магазине {res[21][3]}"
        + "\n"
        + "\n"
        + f"YokoSun Econom: \n{str(res[40][1])} руб. за 100 штук при покупке упаковки {res[40][2]} шт. ({res[40][4]} руб.) в магазине {res[40][3]}"
        + "\n"
        + "\n"
        + f"YokoSun: \n{str(res[41][1])} руб. за 100 штук при покупке упаковки {res[41][2]} шт. ({res[41][4]} руб.) в магазине {res[41][3]}"
        + "\n"
        + "\n"
        + f"YokoSun Premium: \n{str(res[42][1])} руб. за 100 штук при покупке упаковки {res[42][2]} шт. ({res[42][4]} руб.) в магазине {res[42][3]}"
        + "\n"
        + "\n"
        + f"YokoSun ECO: \n{str(res[43][1])} руб. за 100 штук при покупке упаковки {res[43][2]} шт. ({res[43][4]} руб.) в магазине {res[43][3]}"
    )

    text_7 = (
        f"Pampers Premium Care: \n{str(res[22][1])} руб. за 100 штук при покупке упаковки {res[22][2]} шт. ({res[22][4]} руб.) в магазине {res[22][3]}"
        + "\n"
        + "\n"
        + f"Pampers Active Baby-Dry: \n{str(res[23][1])} руб. за 100 штук при покупке упаковки {res[23][2]} шт. ({res[23][4]} руб.) в магазине {res[23][3]}"
        + "\n"
        + "\n"
        + f"Huggies Elite Soft: \n{str(res[24][1])} руб. за 100 штук при покупке упаковки {res[24][2]} шт. ({res[24][4]} руб.) в магазине {res[24][3]}"
        + "\n"
        + "\n"
        + f"Huggies Ultra Comfort: \n{str(res[25][1])} руб. за 100 штук при покупке упаковки {res[25][2]} шт. ({res[25][4]} руб.) в магазине {res[25][3]}"
        + "\n"
        + "\n"
        + f"YokoSun Econom: \n{str(res[44][1])} руб. за 100 штук при покупке упаковки {res[44][2]} шт. ({res[44][4]} руб.) в магазине {res[44][3]}"
        + "\n"
        + "\n"
        + f"YokoSun: \n{str(res[45][1])} руб. за 100 штук при покупке упаковки {res[45][2]} шт. ({res[45][4]} руб.) в магазине {res[45][3]}"
        + "\n"
        + "\n"
        + f"YokoSun Premium: \n{str(res[46][1])} руб. за 100 штук при покупке упаковки {res[46][2]} шт. ({res[46][4]} руб.) в магазине {res[46][3]}"
    )

    text_8 = (
        f"Pampers Premium Care: \n{str(res[26][1])} руб. за 100 штук при покупке упаковки {res[26][2]} шт. ({res[26][4]} руб.) в магазине {res[26][3]}"
        + "\n"
        + "\n"
        + f"Pampers Active Baby-Dry: \n{str(res[27][1])} руб. за 100 штук при покупке упаковки {res[27][2]} шт. ({res[27][4]} руб.) в магазине {res[27][3]}"
        + "\n"
        + "\n"
        + f"Huggies Elite Soft: \n{str(res[28][1])} руб. за 100 штук при покупке упаковки {res[28][2]} шт. ({res[28][4]} руб.) в магазине {res[28][3]}"
        + "\n"
        + "\n"
        + f"Huggies Ultra Comfort: \n{str(res[29][1])} руб. за 100 штук при покупке упаковки {res[29][2]} шт. ({res[29][4]} руб.) в магазине {res[29][3]}"
        + "\n"
        + "\n"
        + f"YokoSun Econom: \n{str(res[47][1])} руб. за 100 штук при покупке упаковки {res[47][2]} шт. ({res[47][4]} руб.) в магазине {res[47][3]}"
        + "\n"
        + "\n"
        + f"YokoSun: \n{str(res[48][1])} руб. за 100 штук при покупке упаковки {res[48][2]} шт. ({res[48][4]} руб.) в магазине {res[48][3]}"
        + "\n"
        + "\n"
        + f"YokoSun ECO: \n{str(res[49][1])} руб. за 100 штук при покупке упаковки {res[49][2]} шт. ({res[49][4]} руб.) в магазине {res[49][3]}"
    )

    data = {
        "p_size1": text_1,
        "p_size2": text_2,
        "p_size3": text_3,
        "p_size4": text_4,
        "t_size3": text_5,
        "t_size4": text_6,
        "t_size5": text_7,
        "t_size6": text_8,
    }
    with open(r"D:\Программирование\1\PodgyzBot\answers.json", "w", encoding="utf-8") as f:
        # with open("/home/feraklin1/bot1/answers.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def update():
    price_parsing()
    calc_min()
    print("calc pass")
    renaming()
    print("renaming pass")
    text()
    print("texting pass")


if __name__ == "__main__":
    update()
