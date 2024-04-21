import random
a='слизень'
b='рыцарь'
c='дракон'

q='водный'
w='огненный'
e='землянной'
wave=0
index=0

w=0

while 1:
    index=random.randint(1,7)
    if index==1 or index==2 or index==3 or index==7:
        print(a)
        
    if index==4 or index==5:
        print(b)
    if index==6:
        print(c)