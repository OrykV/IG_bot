import time
from time import sleep
from random import randint

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException


chrome_driver_path = '/Users/user/Desktop/development/chromedriver'


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        ig_username = input('Input your username: ')
        ig_password = input('Input your password: ')
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)

        username = self.driver.find_element(By.NAME, 'username')
        password = self.driver.find_element(By.NAME,'password')

        username.send_keys(ig_username)
        password.send_keys(ig_password)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(7)
        button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button')
        time.sleep(5)
        button.click()
        time.sleep(4)
        button2 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        time.sleep(4)
        button2.click()

    def find_followers(self, account):
        search = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(account)
        time.sleep(3)
        search.send_keys(Keys.ENTER)
        search.send_keys(Keys.ENTER)
        time.sleep(3)
        followers = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

    def follow(self):
        time.sleep(3)
        for i in range(0, 9230, 10):
            time.sleep(3)
            all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button")
            for button in all_buttons:
                if button.text == 'Follow':
                    try:
                        button.click()
                        sleep(randint(1, 7))
                    except ElementClickInterceptedException:
                        cancel_button = self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div[3]/button[2]')
                        cancel_button.click()


bot = InstaFollower(chrome_driver_path)
bot.login()
bot.find_followers('fortnite')
bot.follow()
