import ctypes
import os
from typing import List

from libs.compiler import compile

def compile_c():
    c_file = os.path.join(os.getcwd(), "libs", "Algorithms_and_Complexity", "libs.c")
    return compile(c_file=c_file)

def Insertion_Sort(arr: List[int], ):
    c_file = compile_c()
    libs = ctypes.CDLL(f'{c_file}')

    libs.insertionSort.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)
    libs.insertionSort.restype = ctypes.POINTER(ctypes.c_int)

    arr_c = (ctypes.c_int * len(arr))(*arr)

    sorted_arr_c = libs.insertionSort(arr_c, len(arr))

    sorted_arr = [sorted_arr_c[i] for i in range(len(arr))]
    return sorted_arr
