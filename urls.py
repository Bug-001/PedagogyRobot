homeUrl = r"https://teaching.applysquare.com/"
SHomeUrl =  homeUrl + r"S/"
THomeUrl =  homeUrl + r"T/"
loginUrl = homeUrl + r"Home/User/login"

usernameInputXPath = r"/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/input"
passwordInputXPath = r'//*[@id="id_login_password"]'
loginButtonXPath = r'//*[@id="id_login_button"]'

enterCourseButton = r"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div"
openAfterClassListButton = r"/html/body/div[1]/div/div/div[1]/div/div/ul/li[3]/a"
enterHomeworkButton = r"/html/body/div[1]/div/div/div[1]/div/div/ul/li[3]/ul/li[1]/a"
enterCertainHomeworkButton = r"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div/div/div/div[5]/table/tbody/tr/td[7]/a"
startJudgeButtonXPath = r"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div/div[3]/div[4]/div[1]/div[3]/table/tbody/tr[1]/td[4]/a[1]"
def OpenHomeworkInterface(driver):
    driver.get(THomeUrl)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(enterCourseButton).click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(openAfterClassListButton).click()
    driver.find_element_by_xpath(enterHomeworkButton).click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(enterCertainHomeworkButton).click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(startJudgeButtonXPath).click()
    driver.implicitly_wait(10)
    driver.switch_to.window(driver.window_handles[-1])

problemJudgeButtonFormat = "/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div[{}]/div[4]/div[2]/a"
problemAnswerXPathFormat = "/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div[{}]/div[4]/div[1]/p[{}]"
def getJudgeButtonXPath(i):
    return problemJudgeButtonFormat.format(i + 5)
def getAnswerXPath(i, j):
    return problemAnswerXPathFormat.format(i + 5, j)
scoreInputXPath = r"/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/span[2]/input"
confirmScoreButtonXPath = r"/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/button[1]"
nextStudentButtonXPath = r"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div[5]/strong[2]/a"
sidXPath = r"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/table/tbody/tr[1]/td[2]"