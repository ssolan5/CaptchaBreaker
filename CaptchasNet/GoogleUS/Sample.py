import urllib, urllib.request ,re , csv, sys, contextlib, datetime, pydub, os, time, GoogleSolver,glob, ssl
from urllib.parse import urljoin
from time import sleep, time
from random import uniform, randint
from pydub import AudioSegment
from pydub.utils import mediainfo
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Naked.toolshed.shell import execute_js, muterun_js


def write_stat(loops, time):
    with open('stat.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([loops, time])


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def wait_between(a, b):
    rand = uniform(a, b)
    sleep(rand)


withnoise_directory = 'CAPTCHA_SAVED/'
DownloadButton = None
#attempt = 0



def downloadAndSolve():
    #sleep(8)

    
    DownloadButton =  driver.find_element_by_link_text("Phonetic spelling (mp3)")
    accent = 'US'
    solve_start = time()
    link = DownloadButton.get_attribute('href')
    complete_url = urljoin(url, link)

    timestr = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    # download the captcha
    urllib.request.urlretrieve(complete_url, 'CAPTCHA_SAVED/captcha'+timestr+'.mp3')
    #AudioSegment.converter = "C:/Program Files/ffmpeg/bin/ffmpeg.exe"
    sound = AudioSegment.from_mp3('CAPTCHA_SAVED/captcha' + timestr + '.mp3')
    filename = 'CAPTCHA_SAVED/captcha' + timestr
    sound.export(filename + '.flac', format="flac")

    info = mediainfo(filename + ".flac")
    print(info['sample_rate'])
    accent = 'US'
    content = GoogleSolver.transcribe(filename + ".flac", info['sample_rate'])
    print(content)

    success = True
    # input result
    if success:
        InputText = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        for letter in content:
            InputText.send_keys(letter)

        InputText = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "message"))
        )

        message = "hey"

        for letter in message:
            InputText.send_keys(letter)

        driver.find_element_by_xpath("//input[@type='submit' and @value='Submit']").click()
        ResultText = driver.find_element_by_tag_name('body')
        print (ResultText.text)
        if "You entered the wrong password." not in ResultText.text :
            accepted = "Accepted"
        else:
            accepted = "NotAccepted"

        solve_end = time()
        fields = [(timestr + '.wav'), accent, ('\'' + content + '\''), accepted,
                  ('\'' + str(round(solve_end - solve_start, 5)) + '\'s')]
        print(fields)

        with open(r'GoogleUS.csv', 'a') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(fields)
        print("exiting")


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
    

    downloadAndSolve()
    print(i)
    i+=1
    wait_between(5, 7)
    sleep(1)
    driver.quit()
