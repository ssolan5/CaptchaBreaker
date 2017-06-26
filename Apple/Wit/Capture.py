import urllib, urllib.request ,re , csv, sys, contextlib, datetime, pydub, os, time, base64
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
from selenium.webdriver.common import action_chains



DownloadButton = None
withnoise_directory = "CAPTCHA_SAVED/"

def wait_between(a, b):
    rand = uniform(a, b)
    sleep(rand)


def downloadAndSolve():

    sleep(2)

    # Enter values in other fields
    inputElement = driver.find_elements_by_tag_name("input")[3]
    inputElement.send_keys(Keys.NULL)
    sleep(2)
    randomtime = int(time());
    randomtimestr = str(randomtime)
    inputElement.send_keys('beepboop_'+randomtimestr+'@gmail.com')

    inputElement = driver.find_element_by_id("password")
    inputElement.send_keys(Keys.NULL)
    sleep(2)
    inputElement.send_keys('SmellyCat@567')

    inputElement = driver.find_elements_by_tag_name("input")[5]
    inputElement.send_keys(Keys.NULL)
    sleep(2)
    inputElement.send_keys('SmellyCat@567')

    inputElement = driver.find_elements_by_tag_name("input")[6]
    inputElement.send_keys(Keys.NULL)
    sleep(2)
    inputElement.send_keys('dxfcgvhj')

    inputElement = driver.find_elements_by_tag_name("input")[7]
    inputElement.send_keys(Keys.NULL)
    sleep(2)
    inputElement.send_keys('gfds')

    inputElement = driver.find_elements_by_tag_name("input")[8]
    inputElement.send_keys(Keys.NULL)
    sleep(2)
    inputElement.send_keys('01011950')

    select = Select(driver.find_elements_by_tag_name("select")[0])
    sleep(2)
    select.select_by_value('130')

    inputElement = driver.find_elements_by_tag_name("input")[9]
    inputElement.send_keys(Keys.NULL)
    sleep(4)
    inputElement.send_keys("ssss")

    select = Select(driver.find_elements_by_tag_name("select")[1])
    select.select_by_value('136')

    inputElement = driver.find_elements_by_tag_name("input")[10]
    inputElement.send_keys(Keys.NULL)
    sleep(3)
    inputElement.send_keys("gggg")

    select = Select(driver.find_elements_by_tag_name("select")[2])
    select.select_by_value('142')

    inputElement = driver.find_elements_by_tag_name("input")[11]
    inputElement.send_keys(Keys.NULL)
    sleep(2)
    inputElement.send_keys("wwww")
    wait_between(7,8)



    # Download the CAPTCHA from media-internals
    try:

        DownloadButton = driver.find_elements_by_class_name("button")[4]
        print(DownloadButton.text)
        DownloadButton.click()
    except TimeoutException as err:
        print("this did not work lol")


    solved = False
    i = 0
    while solved != True:

        sleep(2)
        solve_start = time()

        wait_between(4,5)
        driver.execute_script('''window.open('').focus();''');
        driver.switch_to_window(driver.window_handles[1])
        driver.get("chrome://media-internals")

        dataaudio = driver.find_elements_by_class_name("selectable-button")[1+i]
        i = i+1
        b64 = dataaudio.text.replace("data:audio/x-wav;base64,","")
        timestr = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = 'captcha' + timestr

        with open(r'CAPTCHA_SAVED/' + filename + '.wav', 'ab') as fh:
            fh.write(base64.decodebytes(bytes(b64, "utf-8")))

        driver.execute_script('''window.close()''');
        driver.switch_to.window(driver.window_handles[0])
        sleep(2)


        # Solve the CAPTCHA
        accent = 'US'
        success = execute_js('index.js', withnoise_directory + filename + '.wav')
        success = execute_js('gettranscription.js', withnoise_directory + filename + '.txt')
        with open('CAPTCHA_SAVED/' + filename + '.txt', 'r') as content_file:
            content = content_file.read()
        print(content)

        # Enter the result back in the text box and click Continue
        inputElement = driver.find_elements_by_tag_name("input")[15]
        inputElement.send_keys(Keys.NULL)
        sleep(2)
        for letter in content:
            inputElement.send_keys(letter)
        sleep(1)

        sleep(2)
        submitButton = driver.find_elements_by_tag_name("button")[9]
        #submitButton.click()
        ActionChains(driver).move_to_element(submitButton).click(submitButton).perform()
        # Wait for verification dialog box
        accepted = "NotAccepted"
        try:
            Verify = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "step-verify-code")))
            accepted = "Accepted"
            solved = True
        except TimeoutException as err:
            accepted = "NotAccepted"
            solved = True


        # Record results
        solve_end = time()
        fields = [(filename + '.wav'), accent, ('\'' + content + '\''), accepted,
              ('\'' + str(round(solve_end - solve_start, 5)) + '\'s')]
        print(fields)

        with open(r'AppleWit.csv', 'a') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(fields)

    print("exiting")

i = 0
while i<2:

    url = 'https://appleid.apple.com/account#!&page=create'
    options = webdriver.ChromeOptions()
    #options.add_argument("user-agent="+timestr+"lol")
    options.add_argument("--allow-file-access-from-files")
    options.add_argument("--disable-web-security")
    #options.add_argument('--user-agent=Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3')
    options.add_argument("--incognito")
    options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    wait_between(2.0, 2.5)
    downloadAndSolve()
    print(i)
    i+=1
    wait_between(5, 7)
    sleep(1)
    driver.quit()
