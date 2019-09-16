from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def closeBrowser(self):
        self.bot.close()

    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = bot.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem = bot.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        time.sleep(3)
        passworword_elem = bot.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        time.sleep(2)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)


    def like_photo(self, hashtag):
        bot = self.bot
        bot.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        #gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                #get tags
                hrefs_in_view = bot.find_elements_by_tag_name('a')
                #finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                #building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                #print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        #Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            bot.get(pic_href)
            time.sleep(2)
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: bot.find_element_by_xpath('//span[@aria-label="Like"]').click()
                like_button().click()
                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line("" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(1)
            except Exception as e:
                time.sleep(2)
            unique_photos -= 1

if __name__ == "__main__":

    username = "username"
    password = "password"

    ig = InstagramBot('username', 'password')
    ig.login()

    hashtags = ['software', 'webdeveloper' ,'coding', 'python', 'coder', 'softwareengineer',
                'webdesigner', 'android', 'hack', 'programmers', 'smart', 'programmer', 'web', 'technology',
                'media', 'inovasi']

    while True:
        try:
            #Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            print(tag)
            ig.like_photo(tag)

        except Exception:
            ig.closeBrowser()
            time.sleep(60)
            ig = InstagramBot('username', 'password')
            ig.login()
