#уээуэуееуэууэаэуаэуе))
import random
def atack(q,enemyhealth,attack):
    q=random.randint(1,2)
    if q==1:
        enemyhealth=enemyhealth-attack
    return(enemyhealth)
def eattack(enemyattack,q,dhealth):
    q=random.randint(1,2)
    if q==1:
        dhealth=dhealth-enemyattack
    return(dhealth)
def heal(dhealth,enemyattack):
    dhealth=dhealth+((wave+enemyattack)//2)
    return(dhealth)
print('Напишите 1 для атаки, 2 для лечения. Ваша задача победить столько врагов сколько сможете.')
print("напишите a для авто игры")
auto=0
if input()=='а':
    auto=1
s=0
w=0
q=0
a1='слизень'
a2='рыцарь'
a3='дракон'
attack=20
health=100
power=1
dhealth=health
wave=0
index=0
enemyhealth=0
enemyattack=0
print('')
while 1:
    index=random.randint(1,7)
    if index==1 or index==2 or index==3 or index==4 or wave<3:
        enemyhealth=40+wave*2
        enemyattack=10+wave*2
        print("на вас напал "+a1+' '+str(enemyhealth)+' здоровья '+str(enemyattack)+' атк')
        s=a1
        while enemyhealth>0 and dhealth>0:
            if auto!=1:
                w=input()
            if w=='1' or auto==1:
                enemyhealth=atack(q,enemyhealth,attack)
            dhealth=eattack(enemyattack,q,dhealth)
            if w=='2':
                dhealth=heal(dhealth,enemyattack)
            print(dhealth,enemyhealth)
        health+=5*power
        attack+=5*power
        wave+=1
    elif index==5 or index==6:
        enemyhealth=80+wave*2
        enemyattack=20+wave*2
        print("на вас напал "+a2+' '+str(enemyhealth)+' здоровья'+' '+str(enemyattack)+' атк')
        s=a2
        while enemyhealth>0 and dhealth>0:
            if auto!=1:
                w=input()
            if w=='1' or auto==1:
                enemyhealth=atack(q,enemyhealth,attack)
            dhealth=eattack(enemyattack,q,dhealth)
            if w=='2':
                dhealth=heal(dhealth,enemyattack)
            print(dhealth,enemyhealth)
        health+=10*power
        attack+=10*power
        wave+=1
    elif index==7 and wave>10:
        enemyhealth=160+wave*2
        enemyattack=40+wave*2
        print("на вас напал "+a3+' '+str(enemyhealth)+' здоровья'+' '+str(enemyattack)+' атк')
        s=a3
        while enemyhealth>0 and dhealth>0:
            if auto!=1:
                w=input()
            if w=='1' or auto==1:
                enemyhealth=atack(q,enemyhealth,attack)
            dhealth=eattack(enemyattack,q,dhealth)
            if w=='2':
                dhealth=heal(dhealth,enemyattack)
            print(dhealth,enemyhealth)
        wave+=1
        health+=20*power
        attack+=20*power
    if wave==299:
        enemyhealth=400+wave*2
        enemyattack=200+wave
        print("на вас напал король слизней"+str(enemyhealth)+' здоровья'+' '+str(enemyattack)+' атк')
        s=a3
        while enemyhealth>0 and dhealth>0:
            if auto!=1:
                w=input()
            if w=='1' or auto==1:
                enemyhealth=atack(q,enemyhealth,attack)
            dhealth=eattack(enemyattack,q,dhealth)
            if w=='2':
                dhealth=heal(dhealth,enemyattack)
            print(dhealth,enemyhealth)
        wave+=1
        health+=50*power
        attack+=50*power
    if wave==299:
        print('Вы стали настолько сильны, что познали этот мир полностью. Переродиться?')
        if input()=='да':
            power+=1
            wave=0
        else:
            power=power
    if power==5:
        print('Поздравляем, вы стали настолько сильны что играть дальше для вас нет смысла. ВЫ ЛИКВИДИРОВАНЫ')
        dhealth=-99999999999999999999999999999
    if dhealth<=0:
        break
    dhealth=health
    print('вы убили '+s+', ваше здоровье равно '+str(health)+' а ваша атака равна '+str(attack))
    print()
wave=str(wave-1)
print('вы умерли,вы победили '+wave+' врагов')
