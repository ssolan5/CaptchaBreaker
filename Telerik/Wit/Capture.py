import urllib, urllib.request ,re , csv, sys, contextlib, datetime, pydub, os
from urllib.parse import urljoin
from time import sleep, time
from random import uniform, randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Naked.toolshed.shell import execute_js



withnoise_directory = 'CAPTCHA_SAVED/'

DownloadButton = None

def downloadAndSolve():

    solve_start = time()
    AudioButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "audio"))
    )

    # Click the audio icon and save as
    timestr = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    urllib.request.urlretrieve(AudioButton.get_attribute('src'),
                               withnoise_directory + 'captcha' +timestr + '.wav')


    # wait on nowde js to get result
    accent = 'Unknown'
    success = execute_js('index.js', withnoise_directory + 'captcha' + timestr + '.wav')
    print(success)
    success = execute_js('gettranscription.js', withnoise_directory + 'captcha' + timestr + '.txt')
    print(success)
    with open(withnoise_directory + 'captcha' + timestr + '.txt', 'r') as content_file:
        content = content_file.read()
    print(content)

    # input result
    if success:
        InputText = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceholder1_rcTextBox1"))
        )

        for letter in content:
            InputText.send_keys(letter)

        VerifyButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceholder1_Button1"))
        )

        VerifyButton.click()

        driver.switch_to.window(mainWin)
        accepted = "Accepted"
        ResultText = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceholder1_lblErrorMessage"))
        )
        if "successfully" not in ResultText.text:
            accepted = ("NotAccepted")

        solve_end = time()
        fields = [(timestr + '.wav'), accent, ('\'' + content + '\''), accepted, ('\'' + str(round(solve_end-solve_start, 5))  + '\'s')]
        print(fields)

        with open(r'TelerikWit.csv', 'a') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(fields)
        print("exiting")

i = 0
while i<5:

    url = 'http://demos.telerik.com/aspnet-ajax/captcha/examples/captchaaudiocode/defaultcs.aspx'
    options = webdriver.ChromeOptions()
    #timestr = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    #options.add_argument("user-agent="+timestr+"lol")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)

    mainWin = driver.current_window_handle
    downloadAndSolve()
    print(i)
    i+=1
    driver.quit()
