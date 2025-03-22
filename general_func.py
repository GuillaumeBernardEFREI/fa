def set_to_str(s):
    if len(s) == 0: return ""  # "" is for empty transition ; [""] not correct , [] correct
    s = list(s)
    s.sort()
    _str = ""
    for i in range(0, len(s)-1):
        _str += s[i]+'.'
    _str += s[-1]
    if len(s) != 1:
        return "{"+_str+"}"
    return _str

