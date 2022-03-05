import json
from tkinter import *
from tkinter.tix import Select
from tkinter.ttk import Combobox
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import chromedriver_autoinstaller
from selenium.webdriver.support.select import Select
import datetime
import win32com.client
import os
from selenium.common.exceptions import NoAlertPresentException
import re
from selenium import webdriver 
import chromedriver_autoinstaller 
import webbrowser 

name = "선택안됨"
location = "선택안됨"
grade = "선택안됨"
schoolname = "선택안됨"
Birthday = "선택안됨"
password = "선택안됨"
Time = "00"
minute = "05"


try:
    with open("./inform/information.json", "r", encoding="utf-8") as r:
        info = json.load(r)
except: 
    window = Tk()
    window.title("초기 정보 입력창입니다.")
    window.geometry("540x380")
    window.resizable(False,False)
    window.option_add('*Font',"맑은고딕 20")
    
    def btnpress_name():
        global name
        name = nameE.get()
        insert1()
    def btnpress_location():
        global location
        location = combo_location.get()
        insert1()
    def btnpress_grade():
        global grade
        grade = combo_grade.get()
        insert1()
    def btnpress_schoolname():
        global schoolname
        schoolname = schoolnameE.get()
        insert1()
    def btnpress_Birthday():
        global Birthday
        Birthday = BirthdayE.get()
        insert1()
    def btnpress_password():
        global password
        password = passwordE.get()
        insert1()
    def finish():
        btnpress_name()
        btnpress_location()
        btnpress_grade()
        btnpress_schoolname()
        btnpress_Birthday()
        btnpress_password()
        insert1()
        student_data = {
        "name":name,
        "location":location,
        "grade": grade,
        "school": schoolname, 
        "Birthday": Birthday,
        "password": password,
        "time": Time,
        "minute": minute
        } 
        os.makedirs("inform",exist_ok=True)
        with open("./inform/information.json", "w", encoding="utf-8") as j:
            json.dump(student_data, j, ensure_ascii=False)
        global info
        with open("./inform/information.json", "r", encoding="utf-8") as r:
            info = json.load(r)
    def insert1():
        informE.configure(state='normal')
        informE.delete("1.0","end")
        message = "이름:"+name+"\n지역:"+location+"\n학교급:"+grade+"\n학교명:"+schoolname+"\n생년월일:"+Birthday+"\n비밀번호:"+password+"\n자동으로 실행되는 시간:"+Time+"시"+minute+"분"
        informE.insert(1.0,message)
        informE.configure(state='disabled')
    def close():
        window.destroy()
    def btnpress_Time():
        global Time
        global minute
        Time = combo_time.get()
        minute = combo_minute.get()
        insert1()

    btn1 = Button(window, text="입력",font=("맑은고딕",13), fg = "black",width=7,height=1,command=btnpress_name)
    btn2 = Button(window, text="입력",font=("맑은고딕",13), fg = "black",width=7,height=1,command=btnpress_location)
    btn3 = Button(window, text="입력",font=("맑은고딕",13), fg = "black",width=7,height=1,command=btnpress_grade)
    btn4 = Button(window, text="입력",font=("맑은고딕",13), fg = "black",width=7,height=1,command=btnpress_schoolname)
    btn5 = Button(window, text="입력",font=("맑은고딕",13), fg = "black",width=7,height=1,command=btnpress_Birthday)
    btn6 = Button(window, text="입력",font=("맑은고딕",13), fg = "black",width=7,height=1,command=btnpress_password)
    btn7 = Button(window, text="제출",font=("맑은고딕",13), fg = "black",width=7,height=1,command=finish)
    btn8 = Button(window, text="종료",font=("궁서체",13), fg = "black",width=7,height=1,command=close)
    btn9 = Button(window, text="제출",font=("맑은고딕",11), fg = "black",width=7,height=1,command=btnpress_Time)


    lname=Label(window,text='이름',font=("맑은고딕",13), fg = "black")
    llocation=Label(window,text='지역',font=("맑은고딕",13), fg = "black")
    lgrade = Label(window,text='학교급',font=("맑은고딕",13), fg = "black")
    lschoolname=Label(window,text='학교명',font=("맑은고딕",13), fg = "black")
    lbirthday=Label(window,text='생년월일(6자)',font=("맑은고딕",13), fg = "black")
    lpassword=Label(window,text='비밀번호(4자)',font=("맑은고딕",13), fg = "black")
    ltime=Label(window,text='자동으로 시작할 시간',font=("맑은고딕",13), fg = "black")
    

    nameE = Entry(window,width=12)
    schoolnameE = Entry(window,width=12)
    BirthdayE = Entry(window,width=12)
    passwordE = Entry(window,width=12)

    informE = Text(window,width=10,font=("맑은고딕",15))
    informE.configure(state='disabled')


    combo_location = Combobox(window, width=12, height=18,font=("맑은고딕",15)) 
    combo_location['values']=("필수선택","서울특별시","부산광역시","대구광역시","인천광역시","광주광역시","대전광역시","울산광역시","세종특별자치시","경기도","강원도","충청북도","충청남도","전라북도","전라남도","경상북도","경상남도","제주특별자치도") 
    combo_location.current(0)
    combo_location.config(state="readonly")
    combo_location.option_add('*TCombobox*Listbox.font', ("맑은고딕",15))


    combo_grade = Combobox(window, width=12, height=18,font=("맑은고딕",15)) 
    combo_grade['values']=("필수선택","유치원","초등학교","중학교","고등학교","특수학교 등") 
    combo_grade.current(0)
    combo_grade.config(state="readonly")
    combo_grade.option_add('*TCombobox*Listbox.font', ("맑은고딕",15))

    combo_time = Combobox(window, width=12, height=18,font=("맑은고딕",10)) 
    combo_time['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24") 
    combo_time.current(0)
    combo_time.config(state="readonly")
    combo_time.option_add('*TCombobox*Listbox.font', ("맑은고딕",10))

    combo_minute = Combobox(window, width=12, height=18,font=("맑은고딕",10)) 
    combo_minute['values']=("05","10","15","20","25","30","35","40","45","50","55","60") 
    combo_minute.current(0)
    combo_minute.config(state="readonly")
    combo_minute.option_add('*TCombobox*Listbox.font', ("맑은고딕",10))


    btn1.grid(column=2,row=0)
    btn2.grid(column=2,row=1)
    btn3.grid(column=2, row=2)
    btn4.grid(column=2,row=3)
    btn5.grid(column=2,row=4)
    btn6.grid(column=2,row=5)
    btn7.grid(column=1,row=6)
    btn8.grid(column=2,row=6)
    btn9.place(x=220,y=214)




    lname.grid(column=0,row=0)
    llocation.grid(column=0,row=1)
    lgrade.grid(column=0, row=2)
    lschoolname.grid(column=0,row=3)
    lbirthday.grid(column=0,row=4)
    lpassword.grid(column=0, row=5)
    ltime.place(x=0,y=190)




    nameE.grid(column=1,row=0)
    combo_location.grid(column=1, row=1)
    combo_grade.grid(column=1, row=2)
    combo_time.grid(column=0,row=7)
    schoolnameE.grid(column=1,row=3)
    BirthdayE.grid(column=1,row=4)
    passwordE.grid(column=1,row=5)
    informE.grid(column=1,row=8,ipadx=120)
    combo_minute.place(x=110,y=214)

    
    
    window.mainloop()


name = info["name"]
location = info["location"]
grade = info["grade"]
school = info["school"]
Birthday =info["Birthday"]
password = info["password"]
Time =info["time"]
minute=info["minute"]
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ여기 이후로는 셀레늄


options = webdriver.ChromeOptions() 
#options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("disable-gpu")

try: 
    path = chromedriver_autoinstaller.install(True) 
    driver = webdriver.Chrome(options=options,executable_path=path) 
except FileNotFoundError as err: 
    print("크롬 브라우저를 찾을 수 없습니다. 설치 후 재시도 하시기 바랍니다.")
    webbrowser.open("https://www.google.com/intl/ko/chrome/")



url = 'https://hcs.eduro.go.kr/#/loginHome'
driver.get(url)


main = driver.find_element_by_id('btnConfirm2').click()
school_name_input = driver.find_element_by_id('schul_name_input').click()

Select(driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td/select')).select_by_visible_text(location)
time.sleep(0.5)
Select(driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[2]/td/select')).select_by_visible_text(grade)
time.sleep(0.3)
school_name_input_name = driver.find_element_by_id('orgname').send_keys(school)
school_name_input_name_btn = driver.find_element_by_class_name('searchBtn').click()
wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li'))).click()
school_name_input_btn = driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()


name_input = driver.find_element_by_id('user_name_input').send_keys(name)
date_of_birth_input = driver.find_element_by_id('birthday_input').send_keys(Birthday)
confirm_btn = driver.find_element_by_id('btnConfirm').click()
time.sleep(0.7)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WriteInfoForm"]/table/tbody/tr/td/div/button'))).click()
#wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))).click() 이게 개정되면서 바뀐듯.
time.sleep(0.6)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@aria-label="{password[0]}"]'))).click()
time.sleep(0.3)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@aria-label="{password[1]}"]'))).click()
time.sleep(0.3)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@aria-label="{password[2]}"]'))).click()
time.sleep(0.3)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@aria-label="{password[3]}"]'))).click()
time.sleep(0.3)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnConfirm"]'))).click()
time.sleep(2)


driver.find_element_by_css_selector("#container > div > section.memberWrap > div:nth-child(2) > ul > li > a > em").click()

try:
    alert = driver.switch_to.alert
    message = alert.text
    left_time = re.findall(r'약(\d)분', message)[0]
    alert.accept()
except NoAlertPresentException:
    pass
else:
    time.sleep(int(left_time) * 60)
    driver.find_element_by_css_selector("#container > div > section.memberWrap > div:nth-child(2) > ul > li > a > em").click()
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="survey_q1a1"]'))).click()
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="survey_q2a3"]'))).click()
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="survey_q3a1"]'))).click()
#wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="survey_q4a1"]'))).click()
#wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="survey_q5a1"]'))).click() 이거 2022/03/22 개정되면서 없어짐
last_submit_btn = driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
time.sleep(3)
now = datetime.datetime.now()
nowtime = now.strftime("%Y-%m-%d_%H-%M-%S")
if not os.path.exists("./Self-diagnosis_screenshot"):
    os.makedirs("./Self-diagnosis_screenshot")
    driver.save_screenshot(f"./Self-diagnosis_screenshot/{nowtime}_Self-diagnosis.png")
    time.sleep(2)
    driver.quit()
else:
    driver.save_screenshot(f"./Self-diagnosis_screenshot/{nowtime}_Self-diagnosis.png")
    time.sleep(2)
    driver.quit()


scheduler = win32com.client.Dispatch('Schedule.Service')
scheduler.Connect()
root_folder = scheduler.GetFolder('\\')
task_def = scheduler.NewTask(0)

# Defining the Start time of job
start_time = datetime.datetime(2022,3,5,int(Time),int(minute),0)

# For Daily Trigger set this variable to 2 ; for One time run set this value as 1
TASK_TRIGGER_DAILY = 2
trigger = task_def.Triggers.Create(TASK_TRIGGER_DAILY)
trigger.StartBoundary = start_time.isoformat()

# Create action
TASK_ACTION_EXEC = 0
action = task_def.Actions.Create(TASK_ACTION_EXEC)
action.ID = 'self-diagnosis'
action.Path = "self-diagnosis.exe"
action.Arguments =""
action.WorkingDirectory = os.getcwd()

# Set parameters
task_def.RegistrationInfo.Description = '자가진단 자동화 프로그램입니다.'
task_def.Settings.Enabled = True
task_def.Settings.StopIfGoingOnBatteries = False
task_def.Settings.WakeToRun = True
task_def.Settings.StartWhenAvailable = True
# Register task
# If task already exists, it will be updated
TASK_CREATE_OR_UPDATE = 6
TASK_LOGON_NONE = 0
root_folder.RegisterTaskDefinition(
    'self-diagnosis',  # Task name
    task_def,
    TASK_CREATE_OR_UPDATE,
    '',  # No user
    '',  # No password
    TASK_LOGON_NONE
)