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
        input("modデータのフルパスがありません。\n続行するにはなにかキーを押してください…")
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
            direct = int(input("instだけなら1、voiceだけなら2、フォルダごと持ってく場合は3、instとvoiceを一つのファイルにするなら4を押してください"))
        except:
            continue
        if(direct == 1 or direct == 2 or direct == 3 or direct == 4):
            break
        else:
            continue
    replace = input("フォルダ名に入っていたらスペースに置き換える文字は？\n（なければそのままenterキーを押してください）")
    temp2 = "いいえ"
    if(direct == 1):
        temp2 = "instのみ抽出"
    elif(direct == 2):
        temp2 = "voiceのみ抽出"
    elif(direct == 3):
        temp2 = "フォルダごと持っていく"
    elif(direct == 4):
        temp2 = "instとvoiceを一つのファイルにする"
    ok = input(f"ーーーーーーーー\nmodデータのフルパス:{datapath}\n移動先のフルパス:{musicpass}\もってきかた:{temp2}\nフォルダ名に入っていたらスペースに置き換える文字:{replace}\n取り消す場合はNキーを押してください。")
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
        fpname = fp.name
        if(replace):
            pattern = f"{re.escape(replace)}(?!(side))"
            nom = re.sub(pattern, " ", fpname, flags=re.IGNORECASE)
        else :
            nom = fp.name
        if(nom == s):
            if(direct == 3):
                shutil.copytree(fp,musicpass / f"---{songcounter}-{fpname}")
                return
            else:
                temp3 = "inst.ogg"
                if(direct == 2 and os.path.isfile(fp / "voices.ogg")):
                    temp3 = "voices.ogg"
                if(direct == 4 and os.path.isfile(fp / "voices.ogg") and os.path.isfile(fp / "inst.ogg")):
                    "temp"
                mp = fp / temp3
                shutil.copy(mp,musicpass / f"---{songcounter}-{fpname}.ogg")
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