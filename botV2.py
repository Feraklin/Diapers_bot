import requests
from pprint import pprint
from bottle import run, post, response, request as bottle_request
import json
import time
import datetime


BOT_URL = "TOKEN"
CHAT_ID = "CHAT ID"
message = "message"


def checkWebhook():
    with open("ngrok_f/ip.txt", "r") as myfile:
        ip = myfile.read().replace("\n", "")
        ipcheck = requests.get(
            BOT_URL + "getWebhookInfo").json()["result"]["url"]
        # print (ip)
        # print (ipcheck)
        if ip != ipcheck:
            requests.post(BOT_URL + "setWebHook?url=" + ip)
            print("Webhook was changed!")
        else:
            print("OK!")


def send_message(answer, chatid):
    json_data = {"chat_id": chatid, "text": answer}
    message_url = BOT_URL + "sendMessage"
    requests.post(
        message_url, json=json_data
    )  # don't forget to make import requests lib


def reply_message(chatid, answer, messid):
    json_data = {"chat_id": chatid, "text": answer,
                 "reply_to_message_id": messid}
    message_url = BOT_URL + "sendMessage"
    requests.post(message_url, json=json_data)


def main_keyboard(chatid):
    json_keyboard = json.dumps(
        {
            "keyboard": [
                # 1-я строка клавиатуры и тд
                ["Подгузы 1 р-р", "Подгузы 2 р-р"],
                ["Подгузы 3 р-р", "Подгузы 4 р-р"],
                ["Трусы 3 р-р", "Трусы 4 р-р"],
                ["Трусы 5 р-р", "Трусы 6 р-р"],
            ],
            "one_time_keyboard": False,
            "resize_keyboard": True,
        }
    )
    json_data = {
        "chat_id": chatid,
        # этот текст нужен если у тебя несколько разных клавиатур (если тебе это не надо удаляй)
        "text": "Что угодно?",
        "reply_markup": json_keyboard,
    }
    requests.post(BOT_URL + "sendMessage", data=json_data)


def log_message(date, chatid, message_text):
    newLogLine = [
        datetime.datetime.fromtimestamp(date).strftime("%Y-%m-%d %H:%M:%S"),
        chatid,
        message_text,
    ]
    with open("/home/feraklin1/bot1/bot_log.json", "r", encoding="utf-8") as f:
        log = json.load(f)["log"]

    log.append(newLogLine)
    logLines = {"log": log}

    with open("/home/feraklin1/bot1/bot_log.json", "w", encoding="utf-8") as f:
        json.dump(logLines, f, ensure_ascii=False, indent=4)


@post("/")
def main():
    data = bottle_request.json
    if "message" in data.keys():
        message_text = data["message"]["text"]
        # print(message_text)
        chatid = data["message"]["chat"]["id"]
        messid = data["message"]["message_id"]
        date = data["message"]["date"]

        if (
            message_text != "check"
            and message_text != "Check"
            and message_text != "Стат"
            and message_text != "стат"
        ):
            log_message(date, chatid, message_text)

        if message_text == "/start":
            try:
                main_keyboard(chatid)
            except:
                pass

        if (
            message_text == "1 размер"
            or message_text == "2 размер"
            or message_text == "3 размер"
            or message_text == "4 размер"
        ):
            try:
                main_keyboard(chatid)
            except:
                pass

        if message_text == "ok":
            try:
                reply_message(chatid, "Ok", messid)
            except:
                pass

        if message_text == "Подгузы 1 р-р":
            try:
                with open("answers.json", "r", encoding="utf-8") as f:
                    reply_message(chatid, json.load(f)["p_size1"], messid)
            except:
                reply_message(
                    chatid, "Ошибка запроса: Подгузники 1 р-р", messid)

        if message_text == "Подгузы 2 р-р":
            try:
                with open("answers.json", "r", encoding="utf-8") as f:
                    reply_message(chatid, json.load(f)["p_size2"], messid)
            except:
                reply_message(
                    chatid, "Ошибка запроса: Подгузники 2 р-р", messid)

        if message_text == "Подгузы 3 р-р":
            try:
                with open("answers.json", "r", encoding="utf-8") as f:
                    reply_message(chatid, json.load(f)["p_size3"], messid)
            except:
                reply_message(
                    chatid, "Ошибка запроса: Подгузники 3 р-р", messid)

        if message_text == "Подгузы 4 р-р":
            try:
                with open("answers.json", "r", encoding="utf-8") as f:
                    reply_message(chatid, json.load(f)["p_size4"], messid)
            except:
                reply_message(
                    chatid, "Ошибка запроса: Подгузники 4 р-р", messid)

        if message_text == "Трусы 3 р-р":
            try:
                with open("answers.json", "r", encoding="utf-8") as f:
                    reply_message(chatid, json.load(f)["t_size3"], messid)
            except:
                reply_message(chatid, "Ошибка запроса: Трусы 3 р-р", messid)

        if message_text == "Трусы 4 р-р":
            try:
                with open("answers.json", "r", encoding="utf-8") as f:
                    reply_message(chatid, json.load(f)["t_size4"], messid)
            except:
                reply_message(chatid, "Ошибка запроса: Трусы 4 р-р", messid)

        if message_text == "Трусы 5 р-р":
            try:
                with open("answers.json", "r", encoding="utf-8") as f:
                    reply_message(chatid, json.load(f)["t_size5"], messid)
            except:
                reply_message(chatid, "Ошибка запроса: Трусы 5 р-р", messid)

        if message_text == "Трусы 6 р-р":
            try:
                with open("answers.json", "r", encoding="utf-8") as f:
                    reply_message(chatid, json.load(f)["t_size6"], messid)
            except:
                reply_message(chatid, "Ошибка запроса: Трусы 6 р-р", messid)

        if message_text == "стат" or message_text == "Cтат":
            try:
                with open("bot_log.json", "r", encoding="utf-8") as f:
                    log = json.load(f)["log"]

                ids = []
                for line in log:
                    ids.append(line[1])

                reply_message(
                    chatid, "Уникальных пользователей: " +
                    str(len(set(ids))), messid
                )
            except:
                reply_message(chatid, "Ошибка запроса: Статистика", messid)

        if message_text == "Check" or message_text == "check":
            try:
                with open("urlsCheck.json", "r", encoding="utf-8") as f:
                    reply_message(chatid, json.load(f)["urlsForCheck"], messid)
            except:
                reply_message(chatid, "Ошибка запроса: Check", messid)


if __name__ == "__main__":
    checkWebhook()
    run(host="localhost", port=8080, debug=True)
