import urllib, urllib.request ,re , csv, sys, contextlib, datetime, pydub, os, time, GoogleSolver,glob
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


withnoise_directory = 'CAPTCHA_SAVED/'
DownloadButton = None
#attempt = 0

def wait_between(a, b):
    rand = uniform(a, b)
    sleep(rand)


def downloadAndSolve():
    #sleep(8)

    solve_start = time()
    AudioButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "audio"))
    )

    # Click the audio icon and save as
    timestr = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    urllib.request.urlretrieve(AudioButton.get_attribute('src'),
                               withnoise_directory + 'captcha' +timestr + '.wav')

    filename = 'captcha' +timestr;
    
    solve_start = time()

    sound = AudioSegment.from_wav('CAPTCHA_SAVED/' + filename + '.wav')
    # filename = filename[:-3]
    sound.export('CAPTCHA_SAVED/' + filename + '.flac', format="flac")

    info = mediainfo('CAPTCHA_SAVED/' + filename + ".flac")
    print(info['sample_rate'])
    accent = 'UK'
    content = GoogleSolver.transcribe('CAPTCHA_SAVED/' + filename + ".flac", info['sample_rate'])
    print(content)
    success = True
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

        
        accepted = "Accepted"
        ResultText = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceholder1_lblErrorMessage"))
        )
        if "successfully" not in ResultText.text:
            accepted = ("NotAccepted")

        solve_end = time()

    # Record results
    fields = [(filename + '.wav'), accent, ('\'' + content + '\''), accepted,
              ('\'' + str(round(solve_end - solve_start, 5)) + '\'s')]
    print(fields)

    with open(r'GoogleUK.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(fields)
    print("exiting")

i = 0
while i<100:
    url = 'http://demos.telerik.com/aspnet-ajax/captcha/examples/captchaaudiocode/defaultcs.aspx'
    options = webdriver.ChromeOptions()
    timestr = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    options.add_argument("user-agent="+timestr+"lol")
    prefs = {"download.default_directory": 'CAPTCHA_SAVED/'}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    wait_between(2.0, 2.5)
    mainWin = driver.current_window_handle
    downloadAndSolve()
    print(i)
    i+=1
    wait_between(5, 7)
    sleep(1)
    driver.quit()
