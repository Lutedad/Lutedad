import psutil
import time
import datetime
import requests
import atexit
import requests
import datetime
import sys

# slack 챗 봇
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text})
    print(response)

# slack 토큰
myToken = "비밀"

# message로 받은 인자를 파이썬 쉘과 슬랙 #채널이름 에 동시에 출력한다
def dbgout(message):
    print(message)
    post_message(myToken, "#recording-by-python", message)


Overwatch_exresult = 0
LoL_exresult = 0
Apex_exresult = 0
PUBG_exresult = 0
Discord_exresult = 0
Coding_exresult = 0

Overwatch_a=0
Overwatch_b=0
LoL_b = 0
LoL_a = 0
Apex_b = 0
Apex_a = 0
PUBG_b = 0
PUBG_a = 0
Discord_a = 0
Discord_b = 0
Coding_a=0
Coding_b=0

LoL_text = "Lol 0초"
Apex_text = "Apex 0초"
Over_text = "Overwatch 0초"
PUBG_text = "PUBG 0초"
Discord_text = "Discord 0초"
Coding_text = "Coding 0초"

dt_now = datetime.datetime.now()
findal_dt_now = str(dt_now.date())


def Overwatch():
    if "Overwatch.exe" in (p.name() for p in psutil.process_iter()):
        global begin
        global Overwatch_a
        global Overwatch_b
        if Overwatch_a == Overwatch_b:
            begin = time.time()
            Overwatch_b = Overwatch_b + 1
        time.sleep(3)
    else:
        global Overwatch_exresult
        if Overwatch_a < Overwatch_b:
            end = time.time()
            result = end - begin

            Overwatch_exresult = result + Overwatch_exresult
            plresult = result + Overwatch_exresult 

            plusresult = str(datetime.timedelta(seconds=plresult)).split(".")[0]

            global Over_text
            Over_text = "Overwatch 총 플레이 시간은"+plusresult+"입니다."
            Overwatch_a = Overwatch_a+1
def LoL():
    if "LeagueClient.exe" in (p.name() for p in psutil.process_iter()):
        global begin
        global LoL_a
        global LoL_b
        if LoL_a == LoL_b:
            begin = time.time()
            LoL_b = LoL_b + 1
        time.sleep(3)
    else:
        global LoL_exresult
        if LoL_a < LoL_b:
            end = time.time()
            result = end - begin

            LoL_exresult = result + LoL_exresult
            plresult = result + LoL_exresult 

            plusresult = str(datetime.timedelta(seconds=plresult)).split(".")[0]
            global LoL_text
            LoL_text = "LoL 총 플레이 시간은"+plusresult+"입니다."

            LoL_a = LoL_a+1
def Apex():
    if "r5apex.exe" in (p.name() for p in psutil.process_iter()):
        global begin
        global Apex_a
        global Apex_b
        if Apex_a == Apex_b:
            begin = time.time()
            Apex_b = Apex_b + 1
        time.sleep(3)
    else:
        global Apex_exresult
        if Apex_a < Apex_b:
            end = time.time()
            result = end - begin

            Apex_exresult = result + Apex_exresult
            plresult = result + Apex_exresult 

            plusresult = str(datetime.timedelta(seconds=plresult)).split(".")[0]
            global Apex_text
            Apex_text = "Apex 총 플레이 시간은"+plusresult+"입니다."

            Apex_a = Apex_a+1
def discord():
    if "Discord.exe" in (p.name() for p in psutil.process_iter()):
        global begin
        global Discord_a
        global Discord_b
        if Discord_a == Discord_b:
            begin = time.time()
            Discord_b = Discord_b + 1
        time.sleep(3)
    else:
        global Discord_exresult
        if Discord_a < Discord_b:
            end = time.time()
            result = end - begin

            Discord_exresult = result + Discord_exresult
            plresult = result + Discord_exresult 

            plusresult = str(datetime.timedelta(seconds=plresult)).split(".")[0]
            global Discord_text
            Discord_text = "Discord 총 플레이 시간은"+plusresult+"입니다."

            Discord_a = Discord_a+1
def PUBG():
    if "TslGame.exe" in (p.name() for p in psutil.process_iter()):
        global begin
        global PUBG_a
        global PUBG_b
        if PUBG_a == PUBG_b:
            begin = time.time()
            PUBG_b = PUBG_b + 1
        time.sleep(3)
    else:
        global PUBG_exresult
        if PUBG_a < PUBG_b:
            end = time.time()
            result = end - begin

            PUBG_exresult = result + PUBG_exresult
            plresult = result + PUBG_exresult 

            plusresult = str(datetime.timedelta(seconds=plresult)).split(".")[0]
            global PUBG_text
            PUBG_text = "PUBG 총 플레이 시간은"+plusresult+"입니다."

            PUBG_a = PUBG_a+1
def Coding():
    if "Code.exe" in (p.name() for p in psutil.process_iter()):
        global begin
        global Coding_a
        global Coding_b
        if Coding_a == Coding_b:
            begin = time.time()
            Coding_b = Coding_b + 1
        time.sleep(3)
    else:
        global Coding_exresult
        if Coding_a < Coding_b:
            end = time.time()
            result = end - begin

            Coding_exresult = result + Coding_exresult
            plresult = result + Coding_exresult 

            plusresult = str(datetime.timedelta(seconds=plresult)).split(".")[0]
            global Coding_text
            Coding_text = "열심히 코딩을 한 시간은"+plusresult+"입니다"

            Coding_a = Coding_a+1
def exiting():
    if "killer.exe" in (p.name() for p in psutil.process_iter()):
        sys.exit()
    else:
        pass
def exiting1():
    if "stopper.exe" in (p.name() for p in psutil.process_iter()):
        sys.exit()
    else:
        pass
        


def Last_send():
    Final_text = "오늘"+findal_dt_now+"플레이하신 이력은 다음과 같습니다.\n"+LoL_text+"\n"+Over_text+"\n"+Apex_text+"\n"+Discord_text+"\n"+PUBG_text+"\n수고하셨습니다\n\n이건 좀 많이 해도 됩니다.\n"+Coding_text+"\n그럼 앞으로도 화이팅!"
    dbgout(Final_text)
    time.sleep(5)

atexit.register(Last_send)

while True:
    Overwatch()
    LoL()
    Apex()
    discord()
    PUBG()
    Coding()
    exiting()
    exiting1()
    time.sleep(7)
