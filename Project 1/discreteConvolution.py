import random
import matplotlib.pyplot as mplot
import numpy as np
 
#TASK 1
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

#Prints the probability of each sum
for i in range(0, 46):
    print("S:", i+5 , ", P:", round(result[i],4))

#TASK 2
# Adds the probability of the sum S <= 10
probabilityOfWinning = 0
for i in range(0,6):
    probabilityOfWinning = probabilityOfWinning + result[i]

# Adds the probability of the sum S >= 45
for i in range(40,46):
    probabilityOfWinning = probabilityOfWinning + result[i]

# Prints the result
print("The exact probability of winning the game is: ", probabilityOfWinning)