import numpy as np
temp=[25,29,43,19,29,33,18]
t=np.array(temp)
print("temperatures:",np.array(temp))
print("slicing",temp[2:5])
print("slicing",temp[1::2])
print("maximum temperature is:",np.max(temp))
print("minimum temperature is:",np.min(temp))
print("average temperature is:",np.mean(temp))
print("standard deviation :",np.std(temp))
print(np.where(t>30,"hot","cool"))
