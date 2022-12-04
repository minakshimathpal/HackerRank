import random
n = int(input("enter the number"))
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    choice=[]
    choice= input().split()
    try:
        if choice[0]=="pop":
            s.pop()
        elif choice[0]=="remove":
            s.remove(int(choice[1]))
        elif choice[0]=="discard":
            s.discard(int(choice[1]))
    except:
        print(f"element {choice[1]} is not present to {choice[0]}")
        i-=1
        
print(sum(s))   