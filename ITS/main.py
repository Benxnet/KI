import base64
import hashlib
from operator import xor
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from requests import get


def auf1():
    index = 16
    file = open("c1.dat", "r").read()
    key = hashlib.sha256("dun2018".encode('utf-8')).digest()[0:16]
    base = base64.b64decode(file)
    text = base[index:len(base)]
    iv = base[0:index]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ret = unpad(cipher.decrypt(text), AES.block_size)
    print(ret)


def xor(var, key):
    return bytes(a ^ b for a, b in zip(var, key))

def aufg2():
    file = open("c2.dat", "r")
    c2 = base64.b64decode(file.read())
    key = c2[0:16]
    befehl = c2[16:25]
    text = c2[25:len(c2)]
    speichern = b"SPEICHERN"
    print(speichern)
    drucke = b"DRUCKE   "
    befehlxspeichern = xor(befehl, speichern)
    neuerbefehl = xor(befehlxspeichern, drucke)
    sender = base64.b64encode(key+neuerbefehl+text)
    print(sender)
    send(sender)

def send(cipher):
    r = get("http://fb02itssebastian.fh-muenster.de:31337/",
            headers={"ciphertext": cipher})
    print(r.text)


auf1()
aufg2()

