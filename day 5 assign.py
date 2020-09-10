print("Question1")
def func(a,b):
    if b in a:
        return a.index(b)
    else:
        return -1
l=list(map(int,input().split()));q=0
m=[1,1,5]
for i in m:
    r=func(l,i)
    if r==-1:
        print("It's Gone");q=1;break
    else:l=l[r+1:]
if q==0:
    print("It's a Match")

print("Question2")
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:return True
l=list(range(1,2500))
print(list(filter(prime,l)))

print("Question3")
n=int(input("How many sentences you want to capitalize)
l=[input("Enter the sentence").strip().split(" ") for i in range(n)]
print(list(map(lambda x:" ".join([i.capitalize() for i in x]),l)))
