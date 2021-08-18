import string
import random
import requests
from colorama import Fore
from multiprocessing import Pool, Lock
from mnemonic import Mnemonic
from random import choice
import urllib3

mnemo = Mnemonic("english")
words = mnemo.generate(strength=256)


def mygen(s: str, n: int):
    for _ in range(n):
        yield choice(s.split())


lst = mygen(words, 1)
word= []
word = lst



def get_sample(target_length):
    target_range = string.digits + string.ascii_letters
    return "".join(mygen(words, 1))


def generator(last_two_chars=""):
    url_prefix = "t.me/"
    url_prefix += get_sample(4)
    if last_two_chars:
        return f"{url_prefix}{get_sample(16)}{last_two_chars}"
    else:
        return f"{url_prefix}{get_sample(9)}"
     
     
if __name__ == "__main__":
    for _ in range(5):
        print(generator(""))
    for _ in range(5):
        print(generator("ab"))
        
        
url = "t.me/" # тут должна быть твоя ссылка которая сгенерировалась
valids = 0     

for i in url:
    try:
        requests.get(url, timeout=5) # Кидаем запрос. timeout, что бы лишний раз не ждать
        valids = 1 # Если всё прошло успешно, то valids будет равен 1
    except:
        pass # В ином случае, valids останется 0
    if valids == 1:
        print("ссылкa", url ,"валиднaя")
    else:
        print("Ссылка", url ,"не валидная")
        
while True:
    pass
    
    

