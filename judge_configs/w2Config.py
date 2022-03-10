from utils import fillInTheBlanks

@fillInTheBlanks
def W2_1(ans: str):
    return ['6','9']

@fillInTheBlanks
def W2_8(ans: str):
    return ['21','86','3.25','3','0.5','1.0']

@fillInTheBlanks
def W2_9(ans: str):
    return ['True']

@fillInTheBlanks
def W2_10(ans: str):
    return ['True','False','True']

def W2_11(ans: str):
    return int(input('11: '))

def W2_12(ans: str):
    return int(input('12: '))

W2Config = {
    1: W2_1,
    8: W2_8,
    9: W2_9,
    10: W2_10,
    11: W2_11,
    12: W2_12
}