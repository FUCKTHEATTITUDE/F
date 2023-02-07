import logging
from config import Config
import threading
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from bot import updater, browser, restricted
from telegram.ext import run_async
from telegram import ChatAction
import os
import pickle
import time
from os import execl
from sys import executable

proxylist = [
    "192.99.101.142:7497",
    "198.50.198.93:3128",
    "52.188.106.163:3128",
    "20.84.57.125:3128",
    "172.104.13.32:7497",
    "172.104.14.65:7497",
   "165.225.220.241:10605",
    "165.225.208.84:10605",
    "165.225.39.90:10605",
    "165.225.208.243:10012",
    "172.104.20.199:7497",
    "165.225.220.251:80",
    "34.110.251.255:80",
    "159.89.49.172:7497",
    "165.225.208.178:80",
    "205.251.66.56:7497",
    "139.177.203.215:3128",
    "64.235.204.107:3128",
    "165.225.38.68:10605",
    "165.225.56.49:10605",
    "136.226.75.13:10605",
    "136.226.75.35:10605",
    "165.225.56.50:10605",
    "165.225.56.127:10605",
    "208.52.166.96:5555",
    "104.129.194.159:443",
    "104.129.194.161:443",
    "165.225.8.78:10458",
    "5.161.93.53:1080",
    "165.225.8.100:10605",
]


fake = Faker('en_IN')

count = 0

userId = Config.USERID

n = 0
def joinZoom(context, url_meet, passStr,n,count):

    def students(context):
        print("Running")

        browser.find_element_by_xpath('//*[@id="wc-container-left"]/div[4]/div/div/div/div[1]').click()
        number = WebDriverWait(browser, 2400).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wc-footer"]/div/div[2]/button[1]/div/div/span'))).text
        print(number)
        if(int(number) <10):
            context.bot.send_message(chat_id=userId, text="Your Class has ended!")
            browser.quit()
            execl(executable, executable, "chromium.py")
    try:
        p = proxylist[count]
                 options.add_argument(f"--proxy-server={p}")
        browser = webdriver.Chrome(options=options,desired_capabilities = desired_cap)
        browser.get('https://zoom.us')
        browser.get('https://zoom.us/wc/join/'+ url_meet)
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#inputname"))).click()
        try:
            elem = browser.find_element(
                by='id', value='onetrust-accept-btn-handler')
            elem.click()
            time.sleep(1)
        except NoSuchElementException:
            pass
        for i in range(0, 20):
            browser.find_element(By.CSS_SELECTOR, "#inputname").send_keys(Keys.BACK_SPACE)
        browser.find_element(By.CSS_SELECTOR, "#inputname").send_keys(fake)
        time.sleep(10)
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#inputpasscode"))).click()
        time.sleep(10)
        browser.find_element(By.CSS_SELECTOR, "#inputpasscode").send_keys(Keys.BACK_SPACE)
        time.sleep(10)
        browser.find_element(By.CSS_SELECTOR, "#inputpasscode").send_keys(passStr)
        time.sleep(10)
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#joinBtn"))).click()
        time.sleep(10)
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#preview-audio-control-button"))).click()
        time.sleep(10)
        try:
            WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#preview-audio-control-button > svg:nth-child(1) > path:nth-child(1)"))).click()
            time.sleep(20)
        except NoSuchElementException:
            pass
        try:
            WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#preview-audio-control-button"))).click()
        except NoSuchElementException:
            pass
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".preview-join-button"))).click()
        print("Clicked on join button")
        time.sleep(3)
        browser.save_screenshot("ss.png")
        context.bot.send_chat_action(chat_id=userId, action=ChatAction.UPLOAD_PHOTO)
        mid  = context.bot.send_photo(chat_id=userId, photo=open('ss.png', 'rb'), timeout = 120).message_id
        os.remove('ss.png')
        context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING)
        context.bot.send_message(chat_id=userId, text="joined")
        logging.info("STAAAAPH!!")
        count += 1
        if count == 30:
           count = 0
        # n+=1
        # time.sleep(2)


    except Exception as e:
        browser.save_screenshot("ss.png")
        context.bot.send_chat_action(chat_id=userId, action=ChatAction.UPLOAD_PHOTO)
        mid  = context.bot.send_photo(chat_id=userId, photo=open('ss.png', 'rb'), timeout = 120).message_id
        os.remove('ss.png')
        context.bot.send_message(chat_id=userId, text="Got some error, forward this to telegram group along with pic")
        context.bot.send_message(chat_id=userId, text=str(e))

    j = updater.job_queue
    j.run_repeating(students, 20, 1000)
    
    
while n < number:
    a = threading.Thread(target=fun, args=(n, count,))
    a.start()
    n += 1
    time.sleep(20)

input()

@run_async
def zoom(update, context):
    logging.info("DOING")

    context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING)

    url_meet = update.message.text.split()[1]
    passStr = update.message.text.split()[2]
    number = update.message.text.split()[3]
    joinZoom(context, url_meet, passStr)
