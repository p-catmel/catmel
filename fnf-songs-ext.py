import json
import shutil
import re
import os
import sys
from pathlib import Path
songcounter = 0
while True:
    datapath = Path(input("modのデータのフルパスを入力してください"))
    if(not os.path.isdir(datapath)):
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
            direct = int(input("フォルダごと持ってく場合は1を押してください"))
        except:
            continue
        if(direct == 0 or direct == 1):
            break
        else:
            continue
    temp2 = "いいえ"
    if(direct == 1):
        temp2 = "はい"
    ok = input(f"ーーーーーーーー\nmodのフルパス:{datapath}\n移動先のフルパス:{musicpass}\nフォルダごと持ってく:{temp2}\n取り消す場合はNキーを押してください。")
    if(ok == "N" or ok == "n"):
        continue
    else:
        break
weekspath = datapath / "weeks"
songspath = datapath / "songs"
def weeksfor(weekspath,songspath,musicpass):
    global songcounter
    list = []
    later = []
    for fp in weekspath.iterdir():
        if(fp.suffix == ".json" and fp.is_file()):
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
    for l in list:
        with open(l,'r',encoding="utf-8") as f:
            data = json.load(f)
            for song in data['songs']:
                s = song[0]
                songcounter += 1
                songsfor(s,songspath,musicpass)
def songsfor(s,songspath,musicpass):
    global direct
    for fp in songspath.iterdir():
        if(fp.name == s):
            if(direct == 1):
                shutil.copytree(fp,musicpass / f"---{songcounter}-{fp.name}")
                return
            else:
                mp = fp / "inst.ogg"
                shutil.copy(mp,musicpass / f"---{songcounter}-{fp.name}.ogg")
                return
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