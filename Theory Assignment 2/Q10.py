import numpy as np

def normalize(array):
    mean = np.mean(array)
    stdDev = np.std(array)
    
    normalizedArray = (array - mean) / stdDev
    return normalizedArray

sampleArray = np.array([10, 20, 30, 40, 50])

normalizedSample = normalize(sampleArray)

print("Original array:", sampleArray)
print("Normalized array:", normalizedSample)
