# Ore2BASIC Parser v0.1.0 - 2022/04/08
from collections import deque
import re

from numpy import var
from lib import consts

# パース位置保存用
index = 0

# 演算子のスタック
opelators = deque()
# 被演算子のスタック
operands = deque()
# 変数
vars = {}


def run(code: str) -> None:
    re.sub('^    ', '', code)
    re.sub('\r?\n', '', code)
    token = consts.syntaxRegex.findall(code)
    return





def getvar(t: list[str]) -> None:
    global index, vars
    k = t[index]
    index += 1
    try:
        return vars[k]
    except:
        consts.SyntaxError(f'Variable isn\'t initialized. You have to initialize the variable before using it.')


def setvar(t: list[str]) -> None:
    global index, vars
    k = t[index]
    index += 1
    if consts.varRegex.match(k):
        vars[k] = t[index]
        index += 1
    else:
        consts.SyntaxError(f'Invalid Syntax at {k}: Illegal character in variable name')
    return


def string(t: list[str]) -> str:
    global index
    v = t[index]
    index += 1
    return v


def bool(t: list[str]) -> bool:
    global index
    v = t[index]
    index += 1
    if v == 'true':
        return True
    else:
        return False


def number(t: list[str]) -> int | float:
    global index
    v = t[index]
    index += 1
    if consts.floatRegex.match(v):
        return float(v)
    else:
        return int(v)
