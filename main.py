#10 Coins puzzle
#1 represents head and O represents tail
import random
P1=[]
P2=[]
for i in range(5):
    P1.append(random.choice(('H','T')) )
print("P1",P1)
count1=0;
count0=0;
for i in P1:
    if(i=='T'):
        count0=count0+1
        # print(count0,' Tails')
    else:
        count1+=1
        # print(count1,' Heads')
for i in range(5-count0):
    P2.append('T')
for i in range(5-count1):
    P2.append('H')
print("P2",P2)

for i in range(5):
    if P2[i]=='T':
        P2[i]='H'
    else:
        P2[i]='T'
print("\nAfter flipping P2",P2,'\n')

cnt=0
for i in range(5):
    if P2[i]=='T':
        cnt+=1
print(P1,P2,"Number of heads in P1 and P2 are equal:", cnt==count0);


