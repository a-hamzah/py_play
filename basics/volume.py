# -------------Simple

# import math

# def volume(r, h):
#     vol = (math.pi) * (r ** 2) * h
#     return vol
# if __name__ == '__main__':
#     print (volume(2, 4))


#---------------Using argparse

import math
import argparse

parser = argparse.ArgumentParser(description='Calculate voulme of a cylinder')
parser.add_argument('r', type=int, help='Radius of Cylinder')
parser.add_argument('h', type=int, help='Height of Cylinder')
args = parser.parse_args()

def volume(r, h):
    vol = (math.pi) * (r ** 2) * h
    return vol
if __name__ == '__main__':
    print (volume(args.r, args.h))
