from robot import Robot
from judge_configs.w2Config import W2Config
import userinfo

if __name__ == '__main__':
    r = Robot()
    r.login(userinfo.username, userinfo.password)
    r.autoJudge(W2Config)
