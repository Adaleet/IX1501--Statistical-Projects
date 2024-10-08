import numpy as np
from numpy import random

sample = arr[observations]

#Set parameters: 
Integer a = lower constraint
Integer b = upper constraint
Integer sampleSize = length(sample)
Integer sampleAmount = number of samples to randomize
result = arr[] #Empty list to store bootstrap sample means
probabilityCounter = 0 #Counter to increment everytime the condition is fulfilled

#Calculate the mean of the original sample
mean = calculateMean(sample)

FOR i = 1 to sampleAmount 
    #Generate a random sample with replacement
    randomizedSample = randomChoice(sample, sampleSize) 

    #Calculate the mean of the random sample
    randomizedSampleMean = calculateMean(randomizedSample) 

    #Add randomizedSampleMean to result
    result.append(randomizedSampleMean)

    IF (a < (randomizedSampleMean - mean) < b then)
        probabilityCounter = probabilityCounter + 1

#Calculate the confidence interval using percentiles from the result 
confidenceInterval = calculate_percentiles(result, [2.5, 97.5])

#Calculate the probability of fulfilling the given condition: 
probability = probabilityCounter / sampleAmount