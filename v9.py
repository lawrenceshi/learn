#大数定理
from random import randint
import numpy as np
import matplotlib.pyplot as plt

def flip_coin_raitio(N):

    front = 0

    for i in range(N):
        randomint_num = randint(1, 2)
        if randomint_num == 1:
            front+=1

        return front*1.0/N

# x = [1, 2, 3, 4, 8, 10, 20, 40, 80, 160, 1000, 5000,10000]
x = np.arange(2, 10000, 100)
Y = []

for N in x:

    Y.append(flip_coin_raitio(N)) 

print(Y)
print(x)

Z = [0.5]*len(x)

print(Z)

plt.figure(figsize=(8, 5))
plt.plot(x, Y, color='blue', linewidth=2 , marker="o")
plt.plot(x, Z, color='red', linestyle='-') # 画一条标准0.5的线
plt.grid(True)
plt.show()

