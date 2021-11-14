import json


def text_generator(best_results):
    text_1 = (
        f"Pampers Premium Care: \n{str(best_results[0][1])} руб. за 100 штук при покупке упаковки {best_results[0][2]} шт. ({best_results[0][4]} руб.) в магазине {best_results[0][3]}"
        + "\n"
        + "\n"
        + f"Pampers New Baby-Dry: \n{str(best_results[1][1])} руб. за 100 штук при покупке упаковки {best_results[1][2]} шт. ({best_results[1][4]} руб.) в магазине {best_results[1][3]}"
        + "\n"
        + "\n"
        + f"Huggies Elite Soft: \n{str(best_results[2][1])} руб. за 100 штук при покупке упаковки {best_results[2][2]} шт. ({best_results[2][4]} руб.) в магазине {best_results[2][3]}"
        + "\n"
        + "\n"
        + f"YokoSun: \n{str(best_results[30][1])} руб. за 100 штук при покупке упаковки {best_results[30][2]} шт. ({best_results[30][4]} руб.) в магазине {best_results[30][3]}"
        + "\n"
        + "\n"
        + f"YokoSun Premium: \n{str(best_results[31][1])} руб. за 100 штук при покупке упаковки {best_results[31][2]} шт. ({best_results[31][4]} руб.) в магазине {best_results[31][3]}"
        + "\n"
        + "\n"
        + f"YokoSun ECO: \n{str(best_results[32][1])} руб. за 100 штук при покупке упаковки {best_results[32][2]} шт. ({best_results[32][4]} руб.) в магазине {best_results[32][3]}"
    )

    text_2 = (
        f"Pampers Premium Care: \n{str(best_results[3][1])} руб. за 100 штук при покупке упаковки {best_results[3][2]} шт. ({best_results[3][4]} руб.) в магазине {best_results[3][3]}"
        + "\n"
        + "\n"
        + f"Pampers New Baby-Dry: \n{str(best_results[4][1])} руб. за 100 штук при покупке упаковки {best_results[4][2]} шт. ({best_results[4][4]} руб.) в магазине {best_results[4][3]}"
        + "\n"
        + "\n"
        + f"Huggies Elite Soft: \n{str(best_results[5][1])} руб. за 100 штук при покупке упаковки {best_results[5][2]} шт. ({best_results[5][4]} руб.) в магазине {best_results[5][3]}"
        + "\n"
        + "\n"
        + f"YokoSun: \n{str(best_results[33][1])} руб. за 100 штук при покупке упаковки {best_results[33][2]} шт. ({best_results[33][4]} руб.) в магазине {best_results[33][3]}"
        + "\n"
        + "\n"
        + f"YokoSun Premium: \n{str(best_results[34][1])} руб. за 100 штук при покупке упаковки {best_results[34][2]} шт. ({best_results[34][4]} руб.) в магазине {best_results[34][3]}"
        + "\n"
        + "\n"
        + f"YokoSun ECO: \n{str(best_results[35][1])} руб. за 100 штук при покупке упаковки {best_results[35][2]} шт. ({best_results[35][4]} руб.) в магазине {best_results[35][3]}"
    )

    text_3 = (
        f"Pampers Premium Care: \n{str(best_results[6][1])} руб. за 100 штук при покупке упаковки {best_results[6][2]} шт. ({best_results[6][4]} руб.) в магазине {best_results[6][3]}"
        + "\n"
        + "\n"
        + f"Pampers Active Baby-Dry: \n{str(best_results[7][1])} руб. за 100 штук при покупке упаковки {best_results[7][2]} шт. ({best_results[7][4]} руб.) в магазине {best_results[7][3]}"
        + "\n"
        + "\n"
        + f"Huggies Elite Soft: \n{str(best_results[8][1])} руб. за 100 штук при покупке упаковки {best_results[8][2]} шт. ({best_results[8][4]} руб.) в магазине {best_results[8][3]}"
        + "\n"
        + "\n"
        + f"Huggies Ultra Comfort: \n{str(best_results[9][1])} руб. за 100 штук при покупке упаковки {best_results[9][2]} шт. ({best_results[9][4]} руб.) в магазине {best_results[9][3]}"
        + "\n"
        + "\n"
        + f"YokoSun: \n{str(best_results[36][1])} руб. за 100 штук при покупке упаковки {best_results[36][2]} шт. ({best_results[36][4]} руб.) в магазине {best_results[36][3]}"
    )

    text_4 = (
        f"Pampers Premium Care: \n{str(best_results[10][1])} руб. за 100 штук при покупке упаковки {best_results[10][2]} шт. ({best_results[10][4]} руб.) в магазине {best_results[10][3]}"
        + "\n"
        + "\n"
        + f"Pampers Active Baby-Dry: \n{str(best_results[11][1])} руб. за 100 штук при покупке упаковки {best_results[11][2]} шт. ({best_results[11][4]} руб.) в магазине {best_results[11][3]}"
        + "\n"
        + "\n"
        + f"Huggies Elite Soft: \n{str(best_results[12][1])} руб. за 100 штук при покупке упаковки {best_results[12][2]} шт. ({best_results[12][4]} руб.) в магазине {best_results[12][3]}"
        + "\n"
        + "\n"
        + f"Huggies Ultra Comfort: \n{str(best_results[13][1])} руб. за 100 штук при покупке упаковки {best_results[13][2]} шт. ({best_results[13][4]} руб.) в магазине {best_results[13][3]}"
        + "\n"
        + "\n"
        + f"YokoSun: \n{str(best_results[37][1])} руб. за 100 штук при покупке упаковки {best_results[37][2]} шт. ({best_results[37][4]} руб.) в магазине {best_results[37][3]}"
    )

    text_5 = (
        f"Pampers Premium Care: \n{str(best_results[14][1])} руб. за 100 штук при покупке упаковки {best_results[14][2]} шт. ({best_results[14][4]} руб.) в магазине {best_results[14][3]}"
        + "\n"
        + "\n"
        + f"Pampers Active Baby-Dry: \n{str(best_results[15][1])} руб. за 100 штук при покупке упаковки {best_results[15][2]} шт. ({best_results[15][4]} руб.) в магазине {best_results[15][3]}"
        + "\n"
        + "\n"
        + f"Huggies Elite Soft: \n{str(best_results[16][1])} руб. за 100 штук при покупке упаковки {best_results[16][2]} шт. ({best_results[16][4]} руб.) в магазине {best_results[16][3]}"
        + "\n"
        + "\n"
        + f"Huggies Ultra Comfort: \n{str(best_results[17][1])} руб. за 100 штук при покупке упаковки {best_results[17][2]} шт. ({best_results[17][4]} руб.) в магазине {best_results[17][3]}"
        + "\n"
        + "\n"
        + f"YokoSun Econom: \n{str(best_results[38][1])} руб. за 100 штук при покупке упаковки {best_results[38][2]} шт. ({best_results[38][4]} руб.) в магазине {best_results[38][3]}"
        + "\n"
        + "\n"
        + f"YokoSun: \n{str(best_results[39][1])} руб. за 100 штук при покупке упаковки {best_results[39][2]} шт. ({best_results[39][4]} руб.) в магазине {best_results[39][3]}"
    )

    text_6 = (
        f"Pampers Premium Care: \n{str(best_results[18][1])} руб. за 100 штук при покупке упаковки {best_results[18][2]} шт. ({best_results[18][4]} руб.) в магазине {best_results[18][3]}"
        + "\n"
        + "\n"
        + f"Pampers Active Baby-Dry: \n{str(best_results[19][1])} руб. за 100 штук при покупке упаковки {best_results[19][2]} шт. ({best_results[19][4]} руб.) в магазине {best_results[19][3]}"
        + "\n"
        + "\n"
        + f"Huggies Elite Soft: \n{str(best_results[20][1])} руб. за 100 штук при покупке упаковки {best_results[20][2]} шт. ({best_results[20][4]} руб.) в магазине {best_results[20][3]}"
        + "\n"
        + "\n"
        + f"Huggies Ultra Comfort: \n{str(best_results[21][1])} руб. за 100 штук при покупке упаковки {best_results[21][2]} шт. ({best_results[21][4]} руб.) в магазине {best_results[21][3]}"
        + "\n"
        + "\n"
        + f"YokoSun Econom: \n{str(best_results[40][1])} руб. за 100 штук при покупке упаковки {best_results[40][2]} шт. ({best_results[40][4]} руб.) в магазине {best_results[40][3]}"
        + "\n"
        + "\n"
        + f"YokoSun: \n{str(best_results[41][1])} руб. за 100 штук при покупке упаковки {best_results[41][2]} шт. ({best_results[41][4]} руб.) в магазине {best_results[41][3]}"
        + "\n"
        + "\n"
        + f"YokoSun Premium: \n{str(best_results[42][1])} руб. за 100 штук при покупке упаковки {best_results[42][2]} шт. ({best_results[42][4]} руб.) в магазине {best_results[42][3]}"
        + "\n"
        + "\n"
        + f"YokoSun ECO: \n{str(best_results[43][1])} руб. за 100 штук при покупке упаковки {best_results[43][2]} шт. ({best_results[43][4]} руб.) в магазине {best_results[43][3]}"
    )

    text_7 = (
        f"Pampers Premium Care: \n{str(best_results[22][1])} руб. за 100 штук при покупке упаковки {best_results[22][2]} шт. ({best_results[22][4]} руб.) в магазине {best_results[22][3]}"
        + "\n"
        + "\n"
        + f"Pampers Active Baby-Dry: \n{str(best_results[23][1])} руб. за 100 штук при покупке упаковки {best_results[23][2]} шт. ({best_results[23][4]} руб.) в магазине {best_results[23][3]}"
        + "\n"
        + "\n"
        + f"Huggies Elite Soft: \n{str(best_results[24][1])} руб. за 100 штук при покупке упаковки {best_results[24][2]} шт. ({best_results[24][4]} руб.) в магазине {best_results[24][3]}"
        + "\n"
        + "\n"
        + f"Huggies Ultra Comfort: \n{str(best_results[25][1])} руб. за 100 штук при покупке упаковки {best_results[25][2]} шт. ({best_results[25][4]} руб.) в магазине {best_results[25][3]}"
        + "\n"
        + "\n"
        + f"YokoSun Econom: \n{str(best_results[44][1])} руб. за 100 штук при покупке упаковки {best_results[44][2]} шт. ({best_results[44][4]} руб.) в магазине {best_results[44][3]}"
        + "\n"
        + "\n"
        + f"YokoSun: \n{str(best_results[45][1])} руб. за 100 штук при покупке упаковки {best_results[45][2]} шт. ({best_results[45][4]} руб.) в магазине {best_results[45][3]}"
        + "\n"
        + "\n"
        + f"YokoSun Premium: \n{str(best_results[46][1])} руб. за 100 штук при покупке упаковки {best_results[46][2]} шт. ({best_results[46][4]} руб.) в магазине {best_results[46][3]}"
    )

    text_8 = (
        f"Pampers Premium Care: \n{str(best_results[26][1])} руб. за 100 штук при покупке упаковки {best_results[26][2]} шт. ({best_results[26][4]} руб.) в магазине {best_results[26][3]}"
        + "\n"
        + "\n"
        + f"Pampers Active Baby-Dry: \n{str(best_results[27][1])} руб. за 100 штук при покупке упаковки {best_results[27][2]} шт. ({best_results[27][4]} руб.) в магазине {best_results[27][3]}"
        + "\n"
        + "\n"
        + f"Huggies Elite Soft: \n{str(best_results[28][1])} руб. за 100 штук при покупке упаковки {best_results[28][2]} шт. ({best_results[28][4]} руб.) в магазине {best_results[28][3]}"
        + "\n"
        + "\n"
        + f"Huggies Ultra Comfort: \n{str(best_results[29][1])} руб. за 100 штук при покупке упаковки {best_results[29][2]} шт. ({best_results[29][4]} руб.) в магазине {best_results[29][3]}"
        + "\n"
        + "\n"
        + f"YokoSun Econom: \n{str(best_results[47][1])} руб. за 100 штук при покупке упаковки {best_results[47][2]} шт. ({best_results[47][4]} руб.) в магазине {best_results[47][3]}"
        + "\n"
        + "\n"
        + f"YokoSun: \n{str(best_results[48][1])} руб. за 100 штук при покупке упаковки {best_results[48][2]} шт. ({best_results[48][4]} руб.) в магазине {best_results[48][3]}"
        + "\n"
        + "\n"
        + f"YokoSun ECO: \n{str(best_results[49][1])} руб. за 100 штук при покупке упаковки {best_results[49][2]} шт. ({best_results[49][4]} руб.) в магазине {best_results[49][3]}"
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
    with open("answers.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
