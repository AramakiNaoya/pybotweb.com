from datetime import date, datetime
import math
import random
import requests
import wikipedia

def heisei_command(command):
    heisei, year_str = command.split()
    if year_str.isdigit():
        year = int(year_str)
        if year >= 1989:
            heisei_year = year - 1988
            response = "西暦{}年ハ、平成{}年デス".format(year, heisei_year)
        else:
            response = "西暦{}年ハ、平成デハアリマセン".format(year)
    else:
        response = "数値ヲ指定シテクダサイ"
    
    return response

def today_command():
    today = date.today()
    response = "今日ノ日付ハ {} デス".format(today)
    return response

def now_command():
    now = datetime.now()
    response = "現在ノ日時ハ {} デス".format(now)
    return response

def weekday_command(command):
    try:
        data = command.split()
        year = int(data[1])
        month = int(data[2])
        day = int(data[3])
        one_day = date(year, month, day)
        
        weekday_str = "月火水木金土日"
        weekday = weekday_str[one_day.weekday()]

        response = "{} ハ {}曜日デス".format(one_day, weekday)
    except IndexError:
        response = "3ツノ値(年月日)ヲ指定シテクダサイ"
    except ValueError:
        response = "正シイ日付ヲ指定シテクダサイ"
    return response

def eto_command(command):
    eto, year = command.split()
    eto_list = ["子", "丑", "寅", "卯", "辰", "巳",\
                 "午", "未", "申", "酉", "戌", "亥"]
    eto_number = (int(year) + 8) % 12
    eto_name = eto_list[eto_number]
    response = "{}年生マレノ干支ハ「{}」デス。"\
        .format(year, eto_name)
    return response

def sqrt_command(command):
    sqrt, number_str = command.split()
    x = int(number_str)
    sqrt_x = math.sqrt(x)
    response = "{} ノ平方根ハ {} デス".format(x, sqrt_x)
    return response

def choice_command(command):
    data = command.split()
    choiced = random.choice(data[1:])
    response = "[{}]ガ選バレマシタ".format(choiced)
    return response

def dice_command():
    num = random.randrange(1, 7)
    response = "[{}] ガ出マシタ".format(num)
    return response

def weather_command():
    base_url = "http://weather.livedoor.com/forecast/webservice/json/v1"
    city_code = "130010"
    url = "{}?city={}".format(base_url, city_code)
    r = requests.get(url)
    weather_data = r.json()
    city = weather_data["location"]["city"]
    label = weather_data["forecast"][0]["datelabel"]
    telop = weather_data["forecast"][0]["telop"]

    response = "{}ノ{}ノ天気ハ「{}」デス".format(city, label, telop)
    return response

def wikipedia_command(command):
    cmd, keyword = command.split(maxsplit=1)
    wikipedia.set_lang("ja")
    try:
        page = wikipedia.page(keyword)
        title = page.title
        summary = page.summary
        response = "タイトル： {}\n{}".format(title, summary)
    except wikipedia.exceptions.PageError:
        response = "「{}」ノ意味ガ見ツカリマセンデシタ"\
            .format(keyword)
    return response