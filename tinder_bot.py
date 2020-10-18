from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from secrets import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(4)
        try:
            more_options_btn = self.driver.find_element_by_xpath('//*[text()= "More Options"]')
            print("more_options_btn btn is: ", more_options_btn)
            more_options_btn.click()
            sleep(6)
            login_btn_opener = self.driver.find_element_by_xpath('//*[text()= "log in"]')
            login_btn_opener.click()
            sleep(2)
            fb_btn = self.driver.find_element_by_xpath('//*[text()= "Log in with Facebook"]')
            fb_btn.click()

            self.continute_login()

        except Exception:
            login_btn_opener = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
            login_btn_opener.click()
            sleep(2)
            fb_btn = self.driver.find_element_by_xpath('//*[text()= "Log in with Facebook"]')
            fb_btn.click()
            self.continute_login()

    def continute_login(self):
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)
        sleep(4)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()
        sleep(4)

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()
        sleep(4)

        popup_cookies = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
        sleep(4)

        self.auto_swipe()

    def close_super_like_popup(self):
        close_super_like_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button[2]')
        close_super_like_button.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        self.close_super_like_popup()

    def close_boost_popup(self):
        popup_boost = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[5]/button[2]')
        popup_boost.click()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        try:
            match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
            match_popup.click()
        except Exception:
            self.close_boost_popup()

bot = TinderBot()
bot.login()
