import json
from difflib import get_close_matches
import msvcrt
import sys

data = json.load(open("data.json"))


# read mode in default
# data becomes a python dictionary
def meaning(a):
    w = a.lower()
    if w in data:
        return str(data[w]).strip("[],''")
    elif w.title() in data:
        return str(data[w.title()]).strip("[],''")
    elif w.upper() in data:
        return str(data[w.upper()]).strip("[],''")
    elif get_close_matches(w, data.keys(), 1, 0.8):
        matches = str(get_close_matches(w, data.keys(), 1, 0.8)).strip("[],''")
        nw = input('Did you mean:' + " " + matches + " ? Enter Y if yes, or N if no:")
        if nw == "Y":
            return str(data[matches]).strip("[],''")
        else:
            return 'Sorry the word does not exist in the current dictionary'
    else:
        return "Does not exist, please check again"


while 1:
    word = input("Type your word: ")
    print(meaning(word))
    if msvcrt.kbhit():
        if ord(msvcrt.getch()) == 27:
            sys.exit(-1)
