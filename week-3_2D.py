import numpy as np
a=[[1,2,3],[4,5,6]]
b=[[7,8,9],[10,11,12]]
a1=np.array(a)
b1=np.array(b)
print("2-d arrays:")
print(a1)
print(b1)
print("addition:",np.add(a1,b1))
print("subtraction:",np.subtract(a1,b1))
print("multiplication:",a1*b1)
print("division:",a1/b1)
print(a1[0:3])
print(np.where(a1%2==0,"even","odd") )
print("maximum element:",np.max(b1))
print("minimum:",np.min(b1))
print("concatenate:",np.concatenate((a1,b1)))
print("transpose of a1",np.transpose(a1))
