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

    
    DownloadButton =  driver.find_element(By.CLASS_NAME, "captcha_play_button")
    link = DownloadButton.get_attribute('href')
    driver.execute_script("window.open('" + link + "', 'new_window')")
    
    timestr = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    os.chdir(withnoise_directory)
    sleep(15)
    newest = max(glob.iglob('*.[Ww][Aa][Vv]'), key=os.path.getctime)
    os.rename(newest , 'captcha' + timestr + '.wav')
    #noiseReduce('captcha' + timestr)
    os.chdir("..")

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
            EC.presence_of_element_located((By.ID, "captcha_code"))
        )

        for letter in content:
            InputText.send_keys(letter)


        driver.find_element_by_xpath("//input[@type='submit']").click()
        ResultText = driver.find_elements_by_class_name('error')[1]
        print (ResultText.text)
        if "Incorrect security code entered" not in ResultText.text :
            accepted = "Accepted"
        else:
            accepted = "NotAccepted"

        solve_end = time()
        fields = [(timestr + '.wav'), accent, ('\'' + content + '\''), accepted,
                  ('\'' + str(round(solve_end - solve_start, 5)) + '\'s')]
        print(fields)

        with open(r'SecureImageGoogleUK.csv', 'a') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(fields)
        print("exiting")

i = 0
while i<100:
    
    url = 'http://securimage.byethost16.com/example_form.php'
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=blah blah black sheep")
    prefs = {"download.default_directory": withnoise_directory}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)

    mainWin = driver.current_window_handle

    i = i+1

    accent = 'Unknown'

    downloadAndSolve()
    print(i)
    i+=1
    wait_between(5, 7)
    sleep(1)
    driver.quit()
