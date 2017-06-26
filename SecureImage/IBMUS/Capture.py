import urllib, urllib.request ,re , csv, sys, contextlib, datetime, glob, os
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Naked.toolshed.shell import execute_js, muterun_js


withnoise_directory = 'CAPTCHA_SAVED/'

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

    accent = 'US'
    solve_start = time()

    # download the captcha
    DownloadButton =  driver.find_element(By.CLASS_NAME, "captcha_play_button")
    link = DownloadButton.get_attribute('href')
    driver.execute_script("window.open('" + link + "', 'new_window')")

    timestr = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    os.chdir(withnoise_directory)
    sleep(15)
    newest = max(glob.iglob('*.[Ww][Aa][Vv]'), key=os.path.getctime)
    os.rename(newest,'captcha' + timestr + '.wav')
    #noiseReduce('captcha' + timestr)
    os.chdir("..")
    # wait on node js to get result
    success = execute_js('index.js', withnoise_directory + 'captcha' + timestr + '.wav')
    
    success = execute_js('gettranscription.js', withnoise_directory + 'captcha' + timestr + '_alt.txt')

    with open(withnoise_directory + 'captcha' + timestr + '.txt', 'r') as content_file:
        content = content_file.read()
    print(content)
    # input result
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

        with open(r'IBMWatsonUS.csv', 'a') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(fields)

        driver.quit()
        print("exiting")