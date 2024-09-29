#https://stackoverflow.com/questions/22058048/hashing-a-file-in-python
import hashlib

BUF_SIZE = 65536
sha1 = hashlib.sha1()

def getHash(filename:str):
    with open(filename, 'rb') as f:
      while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        sha1.update(data)
    return sha1.hexdigest()
