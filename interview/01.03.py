def replaceSpaces(S: str, length: int) -> str:
    res = ""
    for i in range(length):
        if S[i] == ' ':
            res += "%20"
        else:
            res += S[i]
    return ''.join(res)