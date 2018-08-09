alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
y=0
a=[]
x=[]
import random
# for i in range()
# x=[random.choice(alpha),random.choice(alpha),random.choice(alpha),random.choice(alpha)]
z=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
for i in range(6):
    y=random.choice(z)
    while(y==0 or y in a ):
        y=random.choice(z)

    a.append(y)

    x.append(alpha[y])

    z[y]=0
print(x)
inp=[]
inp1=inp
same=0
diff=0
while same!=6:
    same=0
    diff=0
    inp=input();
    for i in range(6):
        if x[i]==inp[i]:
            same=same+1
        else:
            for j in range(6):
                if x[i]==inp[j]:
                    diff=diff+1
    print("diff",diff)
    print("same",same)
