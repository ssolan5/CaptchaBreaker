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


DownloadButton = None
#attempt = 0

def wait_between(a, b):
    rand = uniform(a, b)
    sleep(rand)


def downloadAndSolve():
    #sleep(8)

    # Find the Audio URL
    driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])

    DownloadButton = driver.find_element(By.ID, "c_captchademo_samplecaptcha_SoundLink")
    link = DownloadButton.get_attribute('href')
    complete_url = urljoin('https://captcha.com', link)
    timestr = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # download the captcha
    filename = 'captcha' + timestr
    urllib.request.urlretrieve(complete_url, 'CAPTCHA_SAVED/' + filename + '.wav')
    solve_start = time()

    sound = AudioSegment.from_wav('CAPTCHA_SAVED/' + filename + '.wav')
    # filename = filename[:-3]
    sound.export('CAPTCHA_SAVED/' + filename + '.flac', format="flac")

    info = mediainfo('CAPTCHA_SAVED/' + filename + ".flac")
    print(info['sample_rate'])

    content = GoogleSolver.transcribe('CAPTCHA_SAVED/' + filename + ".flac", info['sample_rate'])
    print(content)

    # input result
    accent = 'US'
    InputText = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "CaptchaCodeTextBox"))
    )

    for letter in content:
        InputText.send_keys(letter)

    driver.find_element_by_xpath("//input[@type='submit' and @value='Validate']").click()
    ResultText = driver.find_elements_by_class_name('validationDiv')[0].get_attribute('innerHTML')
    print(ResultText)
    if "Incorrect!" not in ResultText:
        accepted = "Accepted"
    else:
        accepted = "NotAccepted"

    # Record results
    solve_end = time()
    fields = [(filename + '.wav'), accent, ('\'' + content + '\''), accepted,
              ('\'' + str(round(solve_end - solve_start, 5)) + '\'s')]
    print(fields)

    with open(r'GoogleUS.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(fields)
    print("exiting")

i = 0
while i<1000:
    
    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://captcha.com/demos/features/captcha-demo.aspx'
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    timestr = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    options.add_argument("user-agent="+timestr+"lol")
    prefs = {"download.default_directory": 'CAPTCHA_SAVED/'}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    wait_between(2.0, 2.5)
    downloadAndSolve()
    print(i)
    i+=1
    wait_between(5, 7)
    sleep(1)
    driver.quit()
