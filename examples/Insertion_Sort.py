import os
import sys

file_dir = __file__
current_dir = os.path.dirname(file_dir)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from libs.libs import Insertion_Sort

def main():
    array = [13, 12, 11, 6, 5]
    print("array: ", array)
    out = Insertion_Sort(array)
    print("Ordenado: ", out)

if __name__ == "__main__":
    main()