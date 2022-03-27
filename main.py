from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from random import randint
import time as timer

# Constants
USERNAME = "your_email"
PASSWORD = "your_password"
i = 0

ignored_list = []
for n in range(0, 5):
    number = randint(1, 49)
    if number not in ignored_list:
        ignored_list.append(number)
    else:
        number = randint(1, 49)
        ignored_list.append(number)


# Functions
def random_wait() -> int:
    """returns random integer in range 3 - 8 incl."""
    return randint(3, 8)


def main_function():
    global i
    try:
        # step- 0 initialising selenium
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # chrome_driver_path = "C:\Development\chromedriver.exe"
        # driver = webdriver.Chrome(executable_path=chrome_driver_path)
        driver.get("https://www.tinder.com")
        driver.maximize_window()

        # step - 1 click on 'I accept'
        timer.sleep(3)
        button = driver.find_element(By.XPATH,'//span [contains( text(), "I accept")]')
        button.click()

        # step - 2 click on Log in
        button = driver.find_element(By.XPATH,'//span [contains( text(), "Log in")]')
        button.click()

        # step - 3 selecting the option 'more options' or 'login with facebook' , whichever is available
        timer.sleep(2)
        try:
            button = driver.find_element(By.XPATH,'//button[normalize-space()="Log in with Facebook"]')
            button.click()
        except NoSuchElementException:
            button = driver.find_element(By.XPATH,'//button[normalize-space()="More Options"]')
            button.click()
            button = driver.find_element(By.XPATH,'//button[normalize-space()="Log in with Facebook"]')
            button.click()

        # step - 4 dividing the base window and facebook window
        timer.sleep(2)
        base_window = driver.window_handles[0]
        fb_login_window = driver.window_handles[1]

        # step - 5 switching to facebook window and entering id and password
        timer.sleep(2)
        driver.switch_to.window(fb_login_window)
        user_input = driver.find_element(By.XPATH,'//*[@id="email"]')
        user_input.send_keys(USERNAME)
        password_input = driver.find_element(By.XPATH,'//*[@id="pass"]')
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.RETURN)
        timer.sleep(3)

        # step - 7 switching back to main window
        driver.switch_to.window(base_window)

        # step 8 - enabling the location access
        timer.sleep(4)
        button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[3]/button[1]/span')
        button.click()

        # step - 9 disallowing the notification
        timer.sleep(2)
        button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[3]/button[2]/span')
        button.click()

        # step - 10 liking 100 profiles
        while i < 55:
            print(i)
            print(ignored_list)
            if i in ignored_list:
                try:
                    photo_div = driver.find_element(By.XPATH,'html/body/div[1]/div/div[1]/div/main/div['
                                                             '1]/div/div/div[1]/div/div/div[1]')
                    # finding contact photo element
                    action = webdriver.ActionChains(driver=driver)
                    # creates action object for webdriver
                    action.drag_and_drop_by_offset(source=photo_div, xoffset=-200, yoffset=0).perform()
                    # performs d&d action
                    print("Person DisLiked")
                    timer.sleep(random_wait())  # function call to return random wait time
                    i += 1
                except NoSuchElementException:
                    print("Photo div not found")
                    timer.sleep(3)

            else:
                try:
                    photo_div = driver.find_element(By.XPATH,'html/body/div[1]/div/div[1]/div/main/div['
                                                             '1]/div/div/div[1]/div/div/div[1]')
                    # finding contact photo element
                    action = webdriver.ActionChains(driver=driver)
                    # creates action object for webdriver
                    action.drag_and_drop_by_offset(source=photo_div, xoffset=200, yoffset=0).perform()
                    # performs d&d action
                    print("Person Liked")
                    timer.sleep(random_wait())  # function call to return random wait time
                    i += 1
                except NoSuchElementException:
                    print("Photo div not found")
                    timer.sleep(3)
    except NoSuchElementException or ElementClickInterceptedException or IndexError or StaleElementReferenceException:
        print('element failed to load, restarting')
        driver.quit()
        main_function()


main_function()
