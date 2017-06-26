import urllib, urllib.request ,re , csv, sys, contextlib, datetime, pydub, ssl
from urllib.parse import urljoin
from time import sleep, time
from random import uniform, randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Naked.toolshed.shell import execute_js, muterun_js
from pydub import AudioSegment


withnoise_directory = 'CAPTCHA_SAVED/'

def wait_between(a, b):
    rand = uniform(a, b)
    sleep(rand)

i = 0
while i<1000:

    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'http://captchasnet.byethost14.com'
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=blah blah black sheep")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)


    # driver.add_cookie(cookie)

    mainWin = driver.current_window_handle

    i = i+1
    DownloadButton =  driver.find_element_by_link_text("Phonetic spelling (mp3)")
    accent = 'Unknown'
    solve_start = time()
    link = DownloadButton.get_attribute('href')
    complete_url = urljoin(url, link)

    timestr = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # download the captcha
    urllib.request.urlretrieve(complete_url, withnoise_directory + 'captcha' + timestr + '.mp3')
    #AudioSegment.converter = "C:/ffmpeg/bin/ffmpeg.exe"
    print(withnoise_directory + 'captcha' + timestr)
    sound = AudioSegment.from_mp3(withnoise_directory + 'captcha' + timestr + '.mp3')
    filename = withnoise_directory + 'captcha' + timestr
    sound.export(withnoise_directory + 'captcha' + timestr + '.wav', format="wav")


    # wait on node js to get result
    success = execute_js('index.js', withnoise_directory + 'captcha' + timestr + '.wav')
    print(success)
    success = execute_js('gettranscription.js', withnoise_directory + 'captcha' + timestr + '.txt')
    print(success)

    with open(withnoise_directory + 'captcha' + timestr + '.txt', 'r') as content_file:
        content = content_file.read()
        words = content.split()
        result = ""
        for word in words:
            word = word.lower()
            result = result + word[0]

    print(result)

    # input result
    if success:
        InputText = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        for letter in result:
            InputText.send_keys(letter)

        InputText = WebDriverWait(driver, 10).until(

            EC.presence_of_element_located((By.NAME, "message"))
        )

        message = "hey"

        for letter in message:
            InputText.send_keys(letter)

        driver.find_element_by_xpath("//input[@type='submit' and @value='Submit']").click()
        ResultText = driver.find_element_by_tag_name('body')
        if "You entered the wrong password." not in ResultText.text :
            accepted = "Accepted"
        else:
            accepted = "NotAccepted"

        solve_end = time()
        fields = [(timestr + '.wav'), accent, ('\'' + result + '\''), accepted,
                  ('\'' + str(round(solve_end - solve_start, 5)) + '\'s')]
        print(fields)   

        with open(r'Wit.csv', 'a') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(fields)
        print("exiting")

    driver.quit()


