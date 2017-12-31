#coding:latin1
from random import randrange
print("#######JOGO DE PAR OU IMPAR######")
user=input("digite par ou impar para iniciar:")
cpu=randrange(0,11)
if user=="par":
    while True:
        try:
            jog1=int(input("vc jogou:"))
        except:
            exit()
        print("cpu jogo:",cpu)
        soma=jog1+cpu
        if soma%2==0:
            print("vc ganhou:",soma)
        else:
            print("vc perdeu:",soma)

if user=="impar":
    while True:
        jog1=int(input("vc jogou:"))
        print("cpu jogo:",cpu)
        soma=jog1+cpu
        if soma%2==1:
            print("vc ganhou:",soma)
        else:
            print("vc perdeu:",soma)
