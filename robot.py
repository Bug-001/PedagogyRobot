import logging
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from exceptions import LoginFailed
import urls
import userinfo

class Robot:
    __slots__ = ['driver']

    def __init__(self) -> None:
        caps = DesiredCapabilities.CHROME
        caps['loggingPrefs'] = {'performance': 'ALL'}
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        opt.add_argument('log-level=3')
        self.driver = webdriver.Chrome(options=opt, desired_capabilities=caps)
        logging.basicConfig(format='[%(asctime)s]%(levelname)s: %(message)s', 
                            datefmt='%m/%d %H:%M:%S',
                            filename='log.txt', 
                            level=logging.INFO)

    def login(self, username, password):
        self.driver.delete_all_cookies()
        self.driver.get(urls.loginUrl)
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_xpath(urls.usernameInputXPath).send_keys(username)  # Send username
        self.driver.find_element_by_xpath(urls.passwordInputXPath).send_keys(password)  # Send password
        self.driver.find_element_by_xpath(urls.loginButtonXPath).click()  # Submit
        time.sleep(0.5)

        if self.driver.current_url.startswith(urls.SHomeUrl) or self.driver.current_url.startswith(urls.THomeUrl):
            logging.info("Login Successfully!")
        else:
            logging.critical("Login failed, please check your chrome driver")
            raise LoginFailed("Please check your chrome driver")

    def getAnswer(self, pid):
        ans = self.driver.find_element_by_xpath(urls.getAnswerXPath(pid)).text
        return ans.replace('【答题内容】', '')

    def autoJudge(self, config):
        urls.OpenHomeworkInterface(self.driver)
        try:
            while True:
                time.sleep(3)
                for i, judger in config.items():
                    sid = self.driver.find_element_by_xpath(urls.sidXPath).text
                    ans = self.getAnswer(i)
                    score_num = judger(ans)
                    if score_num < 5:
                        logging.warning("{} Problem {}: {:.2f}/5".format(sid, i, score_num))
                        logging.warning("Answer: {}".format(ans))
                    score = '{:.2f}'.format(score_num)
                    try:
                        # In case that some problem has been judged
                        self.driver.find_element_by_xpath(urls.getJudgeButtonXPath(i)).click()
                        self.driver.find_element_by_xpath(urls.scoreInputXPath).send_keys(score)
                        self.driver.find_element_by_xpath(urls.confirmScoreButtonXPath).click()
                    except:
                        logging.INFO('Judgement of {} completed, score {:.2f}/5'.format(sid, score_num))
                self.driver.find_element_by_xpath(urls.nextStudentButtonXPath).click()
                self.driver.implicitly_wait(10)
        except:
            logging.info('Judge Completed')

if __name__ == '__main__':
    r = Robot()
    r.login(userinfo.username, userinfo.password)
    urls.OpenHomeworkInterface(r.driver)