import ctypes
import numpy as np

# Load the shared library
mycode = ctypes.CDLL('./2.so')  # Update the path if necessary

# Define the argument types of the function
mycode.multiply_array.argtypes = (np.ctypeslib.ndpointer(
    dtype=np.int32), ctypes.c_int, ctypes.c_int)

# Create an array
array = np.array([1, 2, 3, 4, 5], dtype=np.int32)

# Call the C function
mycode.multiply_array(array, len(array), 2)

# Print the modified array
print(array)  # Output: [2 4 6 8 10]
