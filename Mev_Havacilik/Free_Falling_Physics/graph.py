import cmath
import math
from cv2 import _OUTPUT_ARRAY_DEPTH_MASK_16F
from matplotlib import pyplot as plt
import numpy as np
 
#Formul sabit degerleri
e = 2.7182818284590552353
g = 9.80665
Cd = 0.48		
p = 1.15923			
A = 0.0044178646640625
m = 0.145;			

k = (Cd * A * p) / 2
kok = ((g * k * m)**(1/2))
lnustu = ((-2)*kok)/m
total = [[]]
h=35.0
input = []

for i in range(1500):
    input.append(i/100)

output = np.subtract(np.divide(((np.add(np.multiply(np.log(np.add(np.exp(np.multiply(input,lnustu)),1)),m),np.multiply(input,kok)))),k),81.7709753166429) 
print(type(output[2]))
outputlist = getattr(output, "tolist", lambda: output)()
istektime=[]
istekyuk = []
for i in outputlist:
    if outputlist[int(i)]-h<1.25:
        if outputlist[int(i)]-h>-1.25:
            print(outputlist[int(i)])
            print(input[int(i)])
            istekyuk.append(outputlist[int(i)])
            istektime.append(input[int(i)])


plt.plot(istektime,istekyuk,
         color='green', marker="o") 
plt.title("Vertical Displace")
plt.xlabel("input")
plt.ylabel("output")
plt.show()