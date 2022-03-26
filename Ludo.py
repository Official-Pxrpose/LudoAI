import random
def roll():
    x=random.randint(1,6)
    return x
def SnakeLadder(p):
    SnakeList=[98,96,93,82,73,62,55,44,38,29]
    SnakeFall=[48,17,43,60,52,40,11,14,20,7]
    LadderList=[3,4,15,24,30,31,49,60,63,72,77]
    LadderJump=[21,36,48,94,75,70,90,79,99,91,97]
    if p in SnakeList:
        x=SnakeList.index(p)
        p=SnakeFall[x]
        return p
    if p in LadderList:
        p=LadderJump[LadderList.index(p)]
        return p
    else:
        return p

p1=p2=p3=p4=0
t1=t2=t3=t4=0
while p1!=1:
    x=roll()
    t1+=1
    if x==1:
        p1=1
        print("Player 1 has started")
        break
while p1<=94:
    p1+=roll()
    t1+=1
    p1=SnakeLadder(p1)
    print("Player 1 now : ",p1)
if p1!=100:
    print("Player 1 needs ",str(100-p1)," to win")
else:
    print('Player 1 haas won.') 
while p1!=100:
    x=roll()
    t1+=1
    if (p1+x)==100:
        p1=100
        print('Player 1 has won')


while p2!=1:
    x=roll()
    t2+=1
    if x==1:
        p2=1
        print("Player 2 has started")
        break
while p2<=94:
    p2+=roll()
    t2+=1
    p2=SnakeLadder(p2)
    print("Player 2 now : ",p2)
if p2!=100:
    print("Player 2 needs ",str(100-p2)," to win")
else:
    print('Player 2 has won.')
while p2!=100:
    x=roll()
    t2+=1
    if (p2+x)==100:
        p2=100
        print('Player 2 has won')


while p3!=1:
    x=roll()
    t3+=1
    if x==1:
        p3=1
        print("Player 3 has started")
        break
while p3<=94:
    p3+=roll()
    t3+=1
  
    p3=SnakeLadder(p3)
    print("Player 3 now : ",p3)
if p3!=100:
    print("Player 3 needs ",str(100-p3)," to win")
else:
    print('Player 3 has won.')
while p3!=100:
    x=roll()
    t3+=1
    if (p3+x)==100:
        p3=100
        print('Player 3 has won')

while p4!=1:
    x=roll()
    t4+=1
    if x==1:
        p4=1
        print("Player 4 has started")
        break
while p4<=94:
    p4+=roll()
    t4+=1
    p4=SnakeLadder(p4)
    print("Player 4 now : ",p4)
if p4!=100:
    print("Player 4 needs ",str(100-p4)," to win")
else:
    print('Player 4 has won.')
while p4!=100:
    x=roll()
    t4+=1
    if (p4+x)==100:
        p4=100
        print('Player 4 has won')
turn=[t1,t2,t3,t4]
print(''' 


''')
print(turn)
Minimum=min(turn)
PlayerIndex=turn.index(Minimum)+1
print("Player ",str(PlayerIndex),"is the winner ")

