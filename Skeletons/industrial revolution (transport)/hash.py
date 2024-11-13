def getHash(filename:str):    
    with open(filename, "r") as f_og:
        string = f_og.read()
        hashsum = 0
        for line in string.split('\n'):
            for i in range(len(line)):
                hashsum += ord(line[i])*i
    return hashsum
