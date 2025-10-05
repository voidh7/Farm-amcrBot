import os
import requests
import json
import random
from threading import Thread
import time
import string
from pyfiglet import figlet_format

url = "https://amoracoin-serve.vercel.app/mine?private_key=${privateKey}&seed=${seed}"

def gerarSeed():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(5))

def minerar(privatekey):
    params = {
        "private_key": privatekey,
        "seed": gerarSeed()
    }
    try:
        response = requests.get(url, params=params)
        print(f"[*]{response.text}")
    except Exception as e:
        print(f" [*] Erro ao minerar {e}")

print(figlet_format("farm amcr bot"))
print("by vøidh7")

privateKey = input("diga sua private key: ")

while True:
    thread1 = Thread(target=minerar, args=(privateKey,))
    thread2 = Thread(target=minerar, args=(privateKey,))
    thread3 = Thread(target=minerar, args=(privateKey,))

    thread1.start()
    thread2.start()
    thread3.start()
