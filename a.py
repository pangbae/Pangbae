import urllib.request
import ast, sys
quest = urllib.request.urlopen('https://api.lootbox.eu/pc/kr/Pangbae-3151/quick-play/allHeroes/')
kittens = quest.read()
str_data = kittens.decode("utf-8")
data = ast.literal_eval(str_data)
print(data["SoloKills"])
