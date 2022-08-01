# -*- coding:utf-8 -*-
from ctypes import util
import pandas as pd
import time
from BotHelper import JsonSearch, get_sheet_with_pd, set_sheet_with_pd, line_push, writeSheet
from BotHelper.util_driver import compose_driver, twitter_login, ouath_twitter_not_login, http_check, wifi_reboot, check_ip, s3_img
from BotHelper.util_driver import moji_hikaku, page_load, myClick, exe_click, mySendkey, slowClick, my_emojiSend, emoji_convert, add_ifin, send_gmail, mail_what, s3_img
import pysnooper
from importlib import reload
import os
from contextlib import contextmanager

from dotenv import load_dotenv
import logging

import util_login
import ik_helper

#-----------debug-----
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        ElementNotInteractableException,
                                        InvalidArgumentException,
                                        JavascriptException,
                                        NoAlertPresentException,
                                        NoSuchElementException,
                                        StaleElementReferenceException,
                                        TimeoutException)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager



from BotHelper.util_driver import page_load, myClick, exe_click, mySendkey
#-----debug---------



logging.config.fileConfig('logconf.ini')
lg = logging.getLogger(__name__)



# 環境変数を参照
load_dotenv()
API_URL = os.getenv('API_URL')
CHROME_PROFILE_DIR = os.getenv('CHROME_PROFILE_DIR')
SHEET_NAME = os.getenv('SHEET_NAME')



@contextmanager
def driver_set(prox=False, profdir=None, prof_name=None, ua_name=None):

    driver = compose_driver(proxy_info=prox, userdata_dir=profdir, use_profile=prof_name, use_ua=ua_name)
    try:
        yield driver
    finally:
        driver.quit()

        



if __name__ == "__main__":
    df = get_sheet_with_pd(sheetname=SHEET_NAME)
    #イククルのIDのあるアカウントだけ
    df.dropna(subset=['cnm'], inplace=True)
    ik_index = df.loc[~df['ik'].isnull()].index
    # img = s3_img()
    # import pdb;pdb.set_trace()
    
    for loop_num, n in enumerate(ik_index):
        #テンプレ取得
        tem_ple = df.iloc[n,:]
        if tem_ple['cnm'] != 'hiroko':
            continue
        

