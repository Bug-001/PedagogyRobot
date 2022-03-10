def split(s: str) -> list:
    import re
    ret = re.split(r'[;,\s，；]\s*', s)
    return list(filter(lambda x: x != '', ret))

def checkListAns(ans: list, slt: list) -> list:
    max_len = min(ans, slt)
    scores = [False] * len(slt)
    for i in range(max_len):
        scores[i] = ans[i] == slt[i]
    return scores

def fillInTheBlanks(checker):
    def check(ans):
        lst = split(ans)
        slt = checker()
        return checkListAns(lst, slt)
    
    return check