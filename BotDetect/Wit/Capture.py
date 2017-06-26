import urllib, urllib.request ,re , csv, sys, contextlib, datetime, pydub, os, time, base64, ssl
from urllib.parse import urljoin
from time import sleep, time
from random import uniform, randint
from pydub import AudioSegment
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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

DownloadButton = None
withnoise_directory = "CAPTCHA_SAVED/"

def wait_between(a, b):
    rand = uniform(a, b)
    sleep(rand)


def downloadAndSolve():

    sleep(8)

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

    # Solve the CAPTCHA
    accent = 'Unknown'
    success = execute_js('index.js', withnoise_directory + filename + '.wav')
    success = execute_js('gettranscription.js',
                         withnoise_directory + filename + '.txt')
    with open('CAPTCHA_SAVED/' + filename + '.txt', 'r') as content_file:
        content = content_file.read()
    print(content)

    # input result
    if success:
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

    with open(r'Wit.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(fields)
    print("exiting")


i = 0
while i<1000:
    ssl._create_default_https_context =  ssl._create_unverified_context
    url = 'https://captcha.com/demos/features/captcha-demo.aspx'
    options = webdriver.ChromeOptions()
    timestr = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    options.add_argument("user-agent="+timestr+"lol")
    options.add_argument("--incognito")
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    wait_between(2.0, 2.5)
    downloadAndSolve()
    print(i)
    i+=1
    wait_between(5, 7)
    sleep(1)
    driver.quit()
