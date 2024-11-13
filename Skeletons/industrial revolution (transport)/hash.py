def getHash(filename:str):    
    with open(filename, "r") as f_og:
       string = f_og.read()
    return hash(string)