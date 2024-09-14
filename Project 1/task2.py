import random
import matplotlib.pyplot as mplot
import numpy as np

#Creates a probability mass function for each die 

d4 = np.ones(4) / 4
d6 = np.ones(6) / 6
d8 = np.ones(8) / 8
d12 = np.ones(12) / 12
d20 = np.ones(20) / 20
# Calculates the discrete convolution
result = np.convolve(d4, d6)
result = np.convolve(result, d8)
result = np.convolve(result, d12)
result = np.convolve(result, d20)

# Winning if S <= 10(inclusive)
S_leq_10 = np.sum(result[:6])  

# Second condition, if S >= 45, Sums from 45 to 50 correspond to indices 40 to 45 (inclusive)
S_geq_45 = np.sum(result[40:]) 

# Total probability of winning the game:
winning_probability = S_leq_10 + S_geq_45

#Prints the probability of each sum
for i in range(0, 46):
    print("S:", i+5 , ", P:", round(result[i],4))


