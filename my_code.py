import ctypes

# Load the shared library
mycode = ctypes.CDLL('./my_code.so')

# Define the arguments and return types of the function
mycode.add_numbers.argtypes = (ctypes.c_int, ctypes.c_int)
mycode.add_numbers.restype = ctypes.c_int

# Call the C function
result = mycode.add_numbers(3, 4)
print(result)
