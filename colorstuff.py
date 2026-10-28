red = "\033[31m"
blue = "\033[34m"
yellow = "\033[33m"
green = "\033[32m"
lime = "\033[92m"
cyan = "\033[36m"
pink = "\033[35m"
bold = "\033[1m"
italic = "\033[3m"
underline = "\033[4m"
warning = "\033[31;1m"
info = "\033[36;3m"
reset = "\033[0m"

def b(boldwhat):
    return f"\033[1m{boldwhat}\033[0m"

def i(italicwhat):
    return f"\033[3m{italicwhat}\033[0m"

def u(underlinewhat):
    return f"\033[4m{underlinewhat}\033[0m"


def warn(warnwhat):
    return f"\033[31;1m{warnwhat}\033[0m"

def inform(infowhat):
    return f"\033[36;3m{infowhat}\033[0m"

