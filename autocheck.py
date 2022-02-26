from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import chromedriver_autoinstaller



chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]


options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
try:
    driver = webdriver.Chrome(options=options, executable_path=f'./{chrome_ver}/chromedriver.exe')   
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(options=options, executable_path=f'./{chrome_ver}/chromedriver.exe')

url = 'https://hcs.eduro.go.kr/#/loginHome'
driver.get(url)


main = driver.find_element_by_id('btnConfirm2').click()
school_name_input = driver.find_element_by_id('schul_name_input').click()
school_name_input_city = driver.find_element_by_xpath('//*[@id="sidolabel"]/option[10]').click()
school_name_input_level = driver.find_element_by_xpath('//*[@id="crseScCode"]/option[5]').click()
time.sleep(0.3)
school_name_input_name = driver.find_element_by_id('orgname').send_keys('고등학교 입력')
school_name_input_name_btn = driver.find_element_by_class_name('searchBtn').click()
wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li'))).click()
school_name_input_btn = driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()


name_input = driver.find_element_by_id('user_name_input').send_keys('이름')
date_of_birth_input = driver.find_element_by_id('birthday_input').send_keys('생년월일6자리')
confirm_btn = driver.find_element_by_id('btnConfirm').click()

time.sleep(0.7)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WriteInfoForm"]/table/tbody/tr/td/div/button'))).click()
#wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))).click() 이게 개정되면서 바뀐듯.
time.sleep(0.3)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="비밀번호 첫번째 수"]'))).click()
time.sleep(0.3)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="비밀번호 두번째 수"]'))).click()
time.sleep(0.3)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="비밀번호 세번째 수"]'))).click()
time.sleep(0.3)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="비밀번호 네번째 수"]'))).click()
time.sleep(0.3)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnConfirm"]'))).click()

time.sleep(1)
check_btn = driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a/em').click()
time.sleep(1)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="survey_q1a1"]'))).click()
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="survey_q2a3"]'))).click()
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="survey_q3a1"]'))).click()
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="survey_q4a1"]'))).click()
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="survey_q5a1"]'))).click()
last_submit_btn = driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
time.sleep(4)
driver.close()
