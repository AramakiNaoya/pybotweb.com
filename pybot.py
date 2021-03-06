from module import *

# 長さコマンド
def len_command(command):
    cmd, text = command.split()
    length = len(text)
    response = "文字列ノ長サハ {} 文字デス".format(length)
    return response

# 文字コードをutf-8指定でpybot.txtファイルを開く
command_file = open("pybot.txt", encoding="utf-8")
raw_data = command_file.read()
command_file.close()
lines = raw_data.splitlines()

# 挨拶の辞書データを作成する
bot_dict = {}
for line in lines:
    word_list = line.split(",")
    key = word_list[0]
    response = word_list[1]
    bot_dict[key] = response

def pybot(command):
    # command = input("pybot> ")
    response = ""
    try:
        # 辞書の中の文字列と照合
        for key in bot_dict:
            if key in command:
                response = bot_dict[key]
                break
        
        if "平成" in command:
            response = heisei_command(command)

        if "長さ" in command:
            response = len_command(command)

        if "干支" in command:
            response = eto_command(command)
        
        if "選ぶ" in command:
            response = choice_command(command)

        if "さいころ" in command:
            response = dice_command()

        if "今日" in command:
            response = today_command()
        
        if "現在" in command:
            response = now_command()
        
        if "曜日" in command:
            response = weekday_command(command)

        if "天気" in command:
            response = weather_command()

        if "平方根" in command:
            response = sqrt_command(command)
        
        if "辞典" in command:
            response = wikipedia_command(command)

        if not response:
            response = "何ヲ言ッテイルカ、ワカラナイ"
        
        return response
        
        # if "さようなら" in command:
        #     break
        
    except Exception as e:
        print("予期セヌ エラーガ 発生シマシタ")
        print("* 種類:", type(e))
        print("* 内容:", e)