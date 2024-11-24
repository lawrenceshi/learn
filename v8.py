from random import randint

def flip_coin_raitio(N):

    front = 0

    for i in range(N):
        randomint_num = randint(1, 2)
        if randomint_num == 1:
            front+=1

    return front*1.0/N

x = [1, 2, 3, 4, 8, 10, 20, 40, 80, 160, 1000, 5000,10000]
Y = []
for N in x:

    Y.append(flip_coin_raitio(N))



print(Y)




