import random
w=0
a1='слизень'
a2='рыцарь'
a3='дракон'
attack=20
health=100
dhealth=health
mastery=2
lvl=0
wave=0
index=0
enemyhealth=0
enemyattack=0
while dhealth>0:
    if wave==12:
        mastery=1
    index=random.randint(1,7)
    if index==1 or index==2 or index==3 or index==4 or wave<3:
        
        enemyhealth=40+wave*2
        enemyattack=10+wave*2
        print("на вас напал "+a1+' '+str(enemyhealth)+' здоровья'+' '+str(enemyattack)+' атк')
        while enemyhealth>0 and dhealth>0:
            w=input()
            if w=='attack':
                w=random.randint(1,mastery)
                if w==1:
                    enemyhealth=enemyhealth-attack
            dhealth-=enemyattack
            print(dhealth,enemyhealth)
        health+=5
        attack+=5
        wave+=1
        
    elif index==5 or index==6:
        enemyhealth=80+wave*2
        enemyattack=20+wave*2
        print("на вас напал "+a2+' '+str(enemyhealth)+' здоровья'+' '+str(enemyattack)+' атк')
        while enemyhealth>0 and dhealth>0:
            w=input()
            if w=='attack':
                w=random.randint(1,mastery)
                if w==1:
                    enemyhealth=enemyhealth-attack
            dhealth-=enemyattack
            print(dhealth,enemyhealth)
        health+=10
        attack+=10
        wave+=1
        
    elif index==7 and wave>10:
        enemyhealth=160+wave*2
        enemyattack=40+wave*2
        print("на вас напал "+a3+' '+str(enemyhealth)+' здоровья'+' '+str(enemyattack)+' атк')
        while enemyhealth>0 and dhealth>0:
            w=input()
            if w=='attack':
                w=random.randint(1,mastery)
                if w==1:
                    enemyhealth=enemyhealth-attack
            dhealth-=enemyattack
            print(dhealth,enemyhealth)
        wave+=1
        
        health+=20
        attack+=20
    if dhealth<=0:
        break
    dhealth=health
wave=str(wave)
print('вы умерли,вы пережили '+wave+' волн')