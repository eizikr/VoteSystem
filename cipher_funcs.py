import socket
from tinyec import registry
import secrets
import pickle
from Crypto.Cipher import AES

def compress(pubKey):
    # Compress the key to hexa 27 characters
    return (hex(pubKey.x) + hex(pubKey.y % 2)[2:])[2:29]

def encrypt(data, sharedKey):
    # Encrypt data
    try:
        cipher = AES.new(bytes(sharedKey, 'utf-8'), AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(data.encode())
        return pickle.dumps((nonce, ciphertext, tag))

    except Exception as err:
        print(err)

def decrypt(load, sharedKey):
    # Decrypt data
    nonce, ciphertext, tag = pickle.loads(bytes.fromhex(load))
    cipher = AES.new(bytes(sharedKey, 'utf-8'), AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(ciphertext).decode()