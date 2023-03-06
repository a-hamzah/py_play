import math
import argparse

parser = argparse.ArgumentParser(description='Calculate area')
parser.add_argument('length', type=int, help='Length of rectangle')
parser.add_argument('width', type=int, help='Width of rectangle')
args = parser.parse_args()

def area_func(length, width):
    area = length * width
    return area
if __name__ == '__main__':
    print (area_func(args.length, args.width))
