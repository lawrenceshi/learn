from random import randint

def flip_coin_raitio(N):

    front = 0

    for i in range(N):
        randomint_num = randint(1, 2)
        if randomint_num == 1:
            front+=1

    return front*1.0/N

print(flip_coin_raitio(100))