import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from exceptions import LoginFailed
import urls

class Robot:
    __slots__ = ['driver']

    def __init__(self) -> None:
        caps = DesiredCapabilities.CHROME
        caps['loggingPrefs'] = {'performance': 'ALL'}
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        opt.add_argument('log-level=3')
        self.driver = webdriver.Chrome(options=opt, desired_capabilities=caps)

    def login(self, username, password):
        self.driver.delete_all_cookies()
        self.driver.get(urls.loginUrl)
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_xpath(urls.usernameInputXPath).send_keys(username)  # Send username
        self.driver.find_element_by_xpath(urls.passwordInputXPath).send_keys(password)  # Send password
        self.driver.find_element_by_xpath(urls.loginButtonXPath).click()  # Submit
        time.sleep(0.5)

        if self.driver.current_url.startswith(urls.SHomeUrl) or self.driver.current_url.startswith(urls.THomeUrl):
            print("Login Successfully!")
        else:
            raise LoginFailed("Please check your chrome driver")

    def autoJudge(self, config):
        urls.OpenHomeworkInterface(self.driver)
        try:
            while True:
                time.sleep(3)
                for id, judger in config.items():
                    ans = self.driver.find_element_by_xpath(urls.getAnswerXPath(id)).text
                    score = judger(ans)
                    print(urls.getJudgeButtonXPath(id))
                    try:
                        # In case that some problem has been judged
                        self.driver.find_element_by_xpath(urls.getJudgeButtonXPath(id)).click()
                        self.driver.find_element_by_xpath(urls.scoreInputXPath).send_keys(score)
                        self.driver.find_element_by_xpath(urls.confirmScoreButtonXPath).click()
                    except:
                        pass
                self.driver.find_element_by_xpath(urls.nextStudentButtonXPath).click()
                self.driver.implicitly_wait(10)
        except:
            pass