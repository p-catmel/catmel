import json
import shutil
import re
import os
import sys
from pathlib import Path
while True:
    modpass = Path(input("modのフルパスを入力してください"))
    if(not os.path.isdir(modpass)):
        input("modのフォルダがありません。\n続行するにはなにかキーを押してください…")
        continue
    while True:
        musicpass = Path(input("移動先フォルダのフルパスを入力してください"))
        if(not os.path.isdir(musicpass)):
            input("移動先フォルダがありません。作成してください。\n続行するにはなにかキーを押してください…")
            continue
        else:
            break
    while True:
        try:
            modasset = int(input("modsにあるなら0、assetsにあるなら1と入力してください。"))
        except:
            continue
        if(modasset == 0 or modasset == 1):
            break
        else:
            continue
    temp = "mods"
    if(modasset == 1):
        temp = "assets"
    ok = input(f"modのフルパス:{modpass}\n移動先のフルパス:{musicpass}\nデータの場所:{temp}\n取り消す場合はNキーを押してください。")
    if(ok == "N" or ok == "n"):
        continue
    else:
        break
datapath = modpass / temp
weekspath = datapath / "weeks"
songspath = datapath / "songs"
def weeksfor(weekspath,songspath,musicpass):
    list = []
    later = []
    for fp in weekspath.iterdir():
        if(fp.suffix == ".json"):
            list.append(fp)
    list.sort()
    for l in list:
        if(not l.stem.startswith("week")):
            later.append(l)
    for la in later:
        while True:
            try:
                howins = int(input(f"{la}という名前のweekが見つかりました。これは何番目のウィークですか?"))
                howins -= 1
                list.insert(howins,la)
                break
            except:
                continue
    #ここからやる
def songsfor(s,songspath,musicpass):
    print("temp")
def noweeksfor(musicpass):
    print("temp")
if(not os.path.isdir(weekspath)):
    ok = input("weeksフォルダがありません。振り分けせずに移動しますがよろしいですか？\n中止する場合はNキーを押してください")
    if(ok == "N" or ok == "n"):
        sys.exit('weeksフォルダが見つかりませんでした。')
    else:
        noweeksfor(musicpass)
else:
    weeksfor(weekspath,songspath,musicpass)