import math

def volume(r, h):
    vol = (math.pi) * (r ** 2) * h
    return vol
if __name__ == '__main__':
    print (volume(2, 4))