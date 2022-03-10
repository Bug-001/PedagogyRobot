def split(s: str) -> list:
    import re
    ret = re.split(r'[;,\s，；]\s*', s)
    return list(filter(lambda x: x != '', ret))

def checkListAns(ans: list, slt: list) -> list:
    max_len = min(len(ans), len(slt))
    scores = [False] * len(slt)
    for i in range(max_len):
        scores[i] = ans[i] == slt[i]
    return scores


def fillInTheBlanks(max_score, weight=None):
    def decorator(checker):
        def check(ans):
            lst = split(ans)
            slt = checker(ans)
            # TODO: ans checker
            checked = checkListAns(lst, slt)
            if weight is None:
                return sum(checked) / len(checked) * max_score
            else:
                raise ValueError("TODO: Weight for fillInTheBlanks")
        return check
    return decorator