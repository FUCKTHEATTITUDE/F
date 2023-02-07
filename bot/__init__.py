import os
from telegram.ext import Updater
import threading
from config import Config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options



try:

	updater = Updater(token = Config.BOT_TOKEN, use_context=True)
	dp = updater.dispatcher
	options = webdriver.ChromeOptions()
	desired_cap = {

		# Configure ChromeOptions to pass fake media stream
		'chromeOptions': {
			'args': ["--use-fake-device-for-media-stream", "--use-fake-ui-for-media-stream"]
		}
	}
	user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.74 Safari/537.36"
	options.headless = True
	options.add_argument(f'user-agent={user_agent}')
	options.add_experimental_option("detach", True)
	options.add_argument("--window-size=1920,800")
	options.add_argument("--allow-file-access-from-files")
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument('--use-fake-device-for-media-stream')
	options.add_argument('--use-fake-ui-for-media-stream')
	options.add_argument("--disable-infobars")
	options.add_argument('--ignore-certificate-errors')
	options.add_argument('--allow-running-insecure-content')
	options.add_argument("--disable-extensions")
	options.add_argument("--proxy-server='direct://'")
	options.add_argument("--proxy-bypass-list=*")
	options.add_argument("--disable-infobars")
	#browser = webdriver.Chrome(options=options,desired_capabilities = desired_cap)
	browser = webdriver.Chrome(options=options,desired_capabilities = desired_cap)
	#browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
except Exception as e:
	print(e)
