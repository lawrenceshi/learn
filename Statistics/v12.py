#大数定理
from random import randint
from numpy import arange
import matplotlib.pyplot as plt

def raitio(N):

    one_three = 0
    two_four_five_six =0

    for i in range(N):
        randomint_num = randint(1,6)
        if randomint_num in [1,3]:
            one_three += 1
        elif randomint_num in [2,4,5,6]:
            two_four_five_six += 1

    one_three_raitio = float(one_three)/N
    two_four_five_six_raitio = float(two_four_five_six)/N

    return [one_three_raitio,two_four_five_six_raitio]

#x = [1 , 2, 3, 4, 8, 10, 20, 40, 80, 160, 1000, 5000,10000,100000000]
x = arange(6, 3000, 6)
Y_1_3 = []
Y_2_4_5_6 = []
for N in x:

    raitio_return = raitio(N)
    print("得出结果",raitio_return)
    
    Y_1_3.append(raitio_return[0])
    Y_2_4_5_6.append(raitio_return[1])


print(x)

Z = [0.333]*len(x)
B = [0.667]*len(x)

print(Z)

plt.figure(figsize=(8, 5))
plt.plot(x, Y_1_3, color='blue', linewidth=2 , marker="o")
plt.plot(x, Y_2_4_5_6, color='GREEN', linewidth=2 , marker="o")
plt.plot(x, Z, color='red', linestyle='-') # 画一条标准0.5的线
plt.plot(x, B, color='red', linestyle='-') # 画一条标准0.667的线

plt.grid(True)
plt.show()

