from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import random


class InstaBot:
    def __init__(self, username, password):

        self.username = username

        # Paths & urls
        insta_url = "https://www.instagram.com/accounts/emailsignup/"
        login_btn_path = "//a[contains(text(), 'Log in')]"
        username_field_path = "//input[@name=\"username\"]"
        password_field_path = "//input[@name=\"password\"]"
        signin_btn_path = "//button[@type=\"submit\"]"
        not_now_btn1 = "//button[contains(text(), 'Not Now')]"
        not_now_btn2 = "//button[contains(text(), 'Not Now')]"

        # Headless Chrome - if you want to visualize
        option = webdriver.ChromeOptions()
        option.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=option)

        # Regular Chrome
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())

        # Go to Instagram
        self.driver.get(insta_url)
        sleep(random.randint(3, 7))

        # Click Instagram login page link
        self.driver.find_element_by_xpath(login_btn_path).click()
        sleep(random.randint(3, 7))

        # Fill in username and password
        self.driver.find_element_by_xpath(username_field_path).send_keys(username)
        self.driver.find_element_by_xpath(password_field_path).send_keys(password)
        sleep(random.randint(3, 7))

        # Click sign in button
        self.driver.find_element_by_xpath(signin_btn_path).click()
        sleep(random.randint(3, 7))

        # Try to click the 'Not Now' button from saving login info
        try:
            self.driver.find_element_by_xpath(not_now_btn1).click()
        except NoSuchElementException:
            sleep(1)

        sleep(random.randint(3, 7))

        # Try to click the 'Not Now' button from turning on notifications
        try:
            self.driver.find_element_by_xpath(not_now_btn2).click()
        except NoSuchElementException:
            sleep(1)

        sleep(random.randint(3, 7))

    def get_post(self, hashtag):
        # Paths
        search_field_path = "//input[@placeholder=\"Search\"]"
        link_to_hashtag = "//a[@href=\"/explore/tags/" + hashtag + "/\"]"
        first_most_recent_post = "//*[@id=\"react-root\"]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]/div[2]"

        # Enter hashtag into search field
        self.driver.find_element_by_xpath(search_field_path).send_keys('#' + hashtag)
        sleep(random.randint(3, 7))

        # Click on the link to the hashtag
        self.driver.find_element_by_xpath(link_to_hashtag).click()
        sleep(random.randint(3, 7))

        # Open first post in most recent section
        self.driver.find_element_by_xpath(first_most_recent_post).click()
        sleep(random.randint(3, 7))

    def like_photos(self, number_of_photos):
        # Paths
        like_btn_path = '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button'
        next_photo_btn_path = "//a[contains(text(), 'Next')]"

        # Go through x amount of photos and like them
        i = 0
        while i < number_of_photos:
            # skip is a random variable 0-5. If skip equals 0 it wont like the photo.
            # This adds some randomness so it looks less like a bot.
            skip = random.randint(0, 5)
            if skip == 0:
                i -= 1
            else:
                try:
                    self.driver.find_element_by_xpath(like_btn_path).click()
                except NoSuchElementException:
                    sleep(5)
                sleep(random.randint(1, 3))

            if i < (number_of_photos - 1):
                self.driver.find_element_by_xpath(next_photo_btn_path).click()
                sleep(random.randint(1, 3))

            i += 1

    def signout(self):
        # Paths & urls
        profile_url = "https://www.instagram.com/" + self.username
        settings_btn_path = "//*[@id=\"react-root\"]/section/main/div/header/section/div[1]/div/button"
        logout_btn_path = "//button[contains(text(), 'Log Out')]"

        # Go to users profile
        self.driver.get(profile_url)
        sleep(random.randint(3, 7))

        # Click settings button
        self.driver.find_element_by_xpath(settings_btn_path).click()
        sleep(random.randint(3, 7))
        
        # Click logout button
        self.driver.find_element_by_xpath(logout_btn_path).click()
        sleep(random.randint(3, 7))
        
        # Quit Chrome
        self.driver.quit()
