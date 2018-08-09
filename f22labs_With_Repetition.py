
alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

x=[]
count=0
ct=0
import random

for i in range(6):
    y=random.choice(alpha)
    x.append(y)

print(x)
for i in range(6):
    for j in range(i+1,6):
        if x[i]==x[j]:
            count=count+1
print(count)
print(x)
inp=[]
guess=20
inp1=inp
same=0
diff=0
print("Welcome to the F22Labs Game")
print("There is a 6 letter word selected by me,Try to Guess the word (Capital letters only)")
while same!=6 and guess>0:
    same=0
    diff=0

    inp=input();
    while(len(inp)>6 or len(inp)<6):
        print("Enter the Word with length of 6 characters")
        inp=input()
    for i in range(6):
        for j in range(i+1,6):
            if x[i]==x[j]:
                ct=ct+1
    for i in range(6):
        if x[i]==inp[i]:
            same=same+1
        else:
            for j in range(6):
                if x[i]==inp[j]:
                    diff=diff+1
                    break
    if ct==count:
        print("\nNumber of characters that are correct, but in the wrong place are ",diff-ct)
        print("Number of characters that are correct and in the correct place are",same)
    else:
        print("\nNumber of characters that are correct, but in the wrong place are ",diff)
        print("Number of characters that are correct and in the correct place are",same)

    if same==6:
        print("Congratulations you found the string")
        break;
    guess=guess-1
    if guess==0:
        print("Game Over")
        break;
    print("Guesses remaining:",guess)
    print("Please try again\n")
    print("Guess the word")
