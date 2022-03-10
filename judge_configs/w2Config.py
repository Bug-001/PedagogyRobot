from judge_configs.utils import fillInTheBlanks

@fillInTheBlanks(5)
def W2_1(ans: str):
    return ['6','9']

@fillInTheBlanks(5)
def W2_8(ans: str):
    return ['21','86','3.25','3','0.5','1.0']

@fillInTheBlanks(5)
def W2_9(ans: str):
    return ['True']

@fillInTheBlanks(5)
def W2_10(ans: str):
    return ['True','False','True']

def W2_11(ans: str):
    if len(ans) < 10: return 0
    else: return 5

def W2_12(ans: str):
    if len(ans) < 10: return 0
    else: return 5

W2Config = {
    1: W2_1,
    8: W2_8,
    9: W2_9,
    10: W2_10,
    11: W2_11,
    12: W2_12
}