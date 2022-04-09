# Ore2BASIC Consts v0.1.0 - 2022/04/08
import re
syntaxRegex = re.compile('\s?(' + '|'.join([
    'if', 'while', 'return', 'break',
    'then', 'else', 'end',
    'print', 'return', 'break',
    'true', 'false', 
    '\+', '-', '\*', '/', '%',
    '!=', '==', '<=?', '>=?', '=',
    '\(.+\)', '\'[.+]*\'',
    '[a-zA-Z]+[a-zA-Z0-9]*',
    '[0-9]+\.[0-9]+', '[0-9]+',
    '\'.*?\'', '\".*?\"'
]) + ')')

floatRegex = re.compile('[0-9]+\.[0-9]+')
intRegex = re.compile('[0-9]+')
varRegex = re.compile('[a-zA-Z]+[a-zA-Z0-9]*')

def SyntaxError(message: str) -> None:
    print(f'\033[31m[Syntax Error] {message}\033[0m')
    return