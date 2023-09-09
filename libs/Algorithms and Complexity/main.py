import ctypes

#  gcc -fPIC -shared -o add.so add.c
libs = ctypes.CDLL('./libs/Algorithms and Complexity/libs.so')

libs.insertionSort.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)
libs.insertionSort.restype = ctypes.POINTER(ctypes.c_int)

arr = [12, 11, 13, 5, 6]

arr_c = (ctypes.c_int * len(arr))(*arr)

sorted_arr_c = libs.insertionSort(arr_c, len(arr))

sorted_arr = [sorted_arr_c[i] for i in range(len(arr))]

print("Arreglo ordenado:", sorted_arr)