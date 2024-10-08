import numpy as np
import matplotlib.pyplot as plt
from numpy import random

# Constants and sample data
a = -4  # the lower constraint
b = 6   # the upper constraint
sample = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]  # the original sample observations
mean = np.mean(sample)  # the mean of the original sample
sampleSize = 10  # the size of each sample
sampleAmount = 1000  # the number of randomized samples to generate
result = []  # list to store the means of the randomized samples
probabilityCounter = 0  # counter for samples that fulfill the given conditions

# Bootstrap sampling
for i in range(sampleAmount):
    # Generate a random sample with replacement
    randomizedSample = random.choice(sample, sampleSize, replace=True)
    randomizedSampleMean = np.mean(randomizedSample)  # Calculate the mean of the randomized sample
    result.append(randomizedSampleMean)  # Store the mean in the result list
    # Check if the condition is satisfied
    if a < (randomizedSampleMean - mean) < b:
        probabilityCounter += 1

# Calculate the confidence interval using np.percentile
confidenceInterval = np.percentile(result, [2.5, 97.5])

# Calculate the probability of fulfilling the given conditions
probability = probabilityCounter / sampleAmount

print(confidenceInterval, probability)